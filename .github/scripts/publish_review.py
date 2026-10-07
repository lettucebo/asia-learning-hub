"""Validate the use-case-review output and publish it as a pull request review."""
import argparse
import html
import json
import os
import re
import secrets
import subprocess
import sys
from pathlib import Path
from typing import Callable

from review_common import RULES_FILE, parse_rule_ids, require_sha, sha256_hex

MARKER_PREFIX = "<!-- use-case-review:"
MAX_SUMMARY_CHARS = 30000
MAX_JOB_OUTPUT_CODE_UNITS = 900_000
FILE_BULLET = re.compile(
    r"^-\s+\*\*(Added|Modified|Deleted|Renamed)\*\*\s+`([^`]+)`\s+[—-]\s+(.+)$",
    re.MULTILINE,
)
CHECK_LINE = re.compile(r"^-\s+\[([A-Z]+-\d{2})\]\s+(PASS|FAIL|N/A)\s+[—-]\s+(.+)$")
STATUSES = {"A": "Added", "M": "Modified", "D": "Deleted", "R": "Renamed"}
RESULT_LABELS = {"PASS": "\u2705 PASS", "FAIL": "\u274c FAIL", "N/A": "\u2796 N/A"}


def cell(text: str) -> str:
    return html.escape(text).replace("|", r"\|")


def parse_checks(rules_text: str, rule_ids: list[str]) -> dict[str, tuple[str, str]]:
    checks: dict[str, tuple[str, str]] = {}
    for line in rules_text.splitlines():
        if not line.strip():
            continue
        match = CHECK_LINE.match(line.strip())
        if match is None:
            raise ValueError(f"Invalid rule check line: {line.strip()}")
        rule_id, result, reason = match.groups()
        if rule_id not in rule_ids:
            raise ValueError(f"Unknown rule check ID: {rule_id}")
        if rule_id in checks:
            raise ValueError(f"Duplicate rule check ID: {rule_id}")
        if result == "FAIL" and not re.search(r"`[^`]+`", reason):
            raise ValueError(f"FAIL result without a path: {rule_id}")
        checks[rule_id] = (result, reason.strip())
    missing = [rule_id for rule_id in rule_ids if rule_id not in checks]
    if missing:
        raise ValueError("Missing rule check IDs: " + ", ".join(missing))
    return checks


def file_rows(files_text: str, name_status: str) -> list[str]:
    descriptions = {}
    for match in FILE_BULLET.finditer(files_text):
        status, path, role = match.groups()
        if path in descriptions or not role.strip():
            raise ValueError(f"Duplicate or empty changed file: {path}")
        descriptions[path] = (status, role.strip())
    rows = []
    for entry in name_status.splitlines():
        parts = entry.split("\t")
        kind = parts[0][:1]
        if len(parts) < 2 or kind not in STATUSES:
            raise ValueError(f"Invalid changed-file entry: {entry}")
        path = parts[-1]
        if path not in descriptions:
            raise ValueError(f"AI summary missing changed file: {path}")
        status, role = descriptions.pop(path)
        if status != STATUSES[kind]:
            raise ValueError(f"Changed-file status mismatch: {path}")
        rows.append(f"| {status} | `{cell(path)}` | {cell(role)} |")
    if not rows or descriptions:
        raise ValueError("AI summary has missing or extra changed files")
    return rows


def render_review(summary: str, name_status: str, head_sha: str, rules: bytes,
                  base_sha: str, rules_changed: bool = False) -> str:
    require_sha(head_sha, "head")
    require_sha(base_sha, "base")
    rule_ids = parse_rule_ids(rules.decode("utf-8"))
    if not summary.strip():
        raise ValueError("AI summary is empty")
    if len(summary) > MAX_SUMMARY_CHARS or MARKER_PREFIX in summary:
        raise ValueError("Invalid AI summary size or marker")
    headings = list(re.finditer(r"^## (Purpose|Changed files|Rule check)\s*$",
                                summary, re.MULTILINE))
    if [heading.group(1) for heading in headings] != [
        "Purpose", "Changed files", "Rule check"
    ]:
        raise ValueError("Missing AI summary sections")
    verdict = re.search(r"^Verdict: (PASS|FAIL)\s*$", summary, re.MULTILINE)
    if verdict is None or summary[verdict.end():].strip():
        raise ValueError("Invalid Verdict line")
    purpose = summary[headings[0].end():headings[1].start()].strip()
    files_text = summary[headings[1].end():headings[2].start()].strip()
    rules_text = summary[headings[2].end():verdict.start()].strip()
    if not purpose:
        raise ValueError("Missing purpose")

    checks = parse_checks(rules_text, rule_ids)
    rows = file_rows(files_text, name_status)
    failed = [rule_id for rule_id in rule_ids if checks[rule_id][0] == "FAIL"]
    if (verdict.group(1) == "FAIL") != bool(failed):
        raise ValueError("Verdict disagrees with rule check results")

    heading = ("\U0001f7e1 Changes recommended \u2014 FAIL" if failed else
               "\U0001f7e2 All review checks passed \u2014 PASS")
    warning = (
        f"> [!WARNING]\n> This pull request changes `{RULES_FILE}`. This review used "
        "the base branch version of the rules.\n\n" if rules_changed else ""
    )
    check_rows = "\n".join(
        f"| {rule_id} | {RESULT_LABELS[checks[rule_id][0]]} | {cell(checks[rule_id][1])} |"
        for rule_id in rule_ids
    )
    provenance = (
        f"Reviewed against `{RULES_FILE}` @ `{base_sha[:7]}` "
        f"(sha256 `{sha256_hex(rules)[:12]}`)."
    )
    return (
        "## Copilot use case review\n\n"
        f"### {heading}\n\n"
        f"{html.escape(purpose)}\n\n"
        f"{warning}"
        "<details open>\n"
        f"<summary><strong>Review checks ({len(failed)} failed of {len(rule_ids)})"
        "</strong></summary>\n\n"
        "| Check | Result | Details |\n|---|---|---|\n"
        f"{check_rows}\n\n</details>\n\n"
        "<details>\n"
        f"<summary><strong>What changed in this PR ({len(rows)} files)</strong></summary>\n\n"
        "| Change | File | Purpose |\n|---|---|---|\n"
        + "\n".join(rows)
        + "\n\n</details>\n\n"
        f"{provenance} Generated by Copilot CLI; advisory, not an approval.\n\n"
        f"{MARKER_PREFIX}{head_sha} -->"
    )


def find_existing(reviews: list[dict], marker: str) -> int | None:
    for review in reviews:
        if (review.get("user") or {}).get("login") == "github-actions[bot]" \
                and marker in review.get("body", ""):
            return review["id"]
    return None


def publish_review(body: str, repo: str, number: int, head_sha: str,
                   request: Callable[[str, str, dict | None], object]) -> int:
    endpoint = f"repos/{repo}/pulls/{number}"
    current = request("GET", endpoint)
    if current["head"]["sha"] != head_sha:
        raise ValueError("PR head changed during review")
    reviews = request("GET", f"{endpoint}/reviews?per_page=100")
    existing = find_existing(reviews, f"{MARKER_PREFIX}{head_sha} -->")
    if existing is None:
        result = request("POST", f"{endpoint}/reviews",
                         {"body": body, "event": "COMMENT", "commit_id": head_sha})
    else:
        result = request("PUT", f"{endpoint}/reviews/{existing}", {"body": body})
    return result["id"]


def gh_request(method: str, path: str, payload: dict | None = None):
    command = ["gh", "api", path]
    if method != "GET":
        command += ["--method", method, "--input", "-"]
    result = subprocess.run(
        command, input=json.dumps(payload, ensure_ascii=False) if payload else None,
        capture_output=True, text=True, encoding="utf-8", check=True,
    )
    return json.loads(result.stdout)


def append_file(variable: str, text: str) -> None:
    target = os.environ.get(variable)
    if target:
        with open(target, "a", encoding="utf-8") as handle:
            handle.write(text)


def multiline_output(name: str, value: str) -> str:
    delimiter = f"EOF_{secrets.token_hex(16)}"
    return f"{name}<<{delimiter}\n{value}\n{delimiter}\n"


def output_size_code_units(*values: str) -> int:
    return sum(len(value.encode("utf-16-le")) // 2 for value in values)


def env_flag(name: str) -> bool:
    value = os.environ.get(name, "false")
    if value not in ("true", "false"):
        raise ValueError(f"{name} must be true or false")
    return value == "true"


def validate_command(review_dir: Path) -> None:
    summary = (review_dir / "ai-summary.md").read_text(encoding="utf-8")
    changed = (review_dir / "changed-files.txt").read_text(encoding="utf-8")
    if output_size_code_units(summary, changed) > MAX_JOB_OUTPUT_CODE_UNITS:
        raise ValueError("Review outputs exceed the safe GitHub Actions job output limit")
    render_review(summary, changed, os.environ["HEAD_SHA"],
                  Path(RULES_FILE).read_bytes(), os.environ["BASE_SHA"],
                  env_flag("RULES_CHANGED"))
    append_file("GITHUB_OUTPUT", multiline_output("summary", summary)
                + multiline_output("changed_files", changed) + "ready=true\n")
    print("AI summary is valid.")


def publish_command() -> None:
    summary = os.environ.get("AI_SUMMARY", "")
    changed = os.environ.get("CHANGED_FILES", "")
    if not summary.strip() or not changed.strip():
        raise ValueError("Review output was not received from the generate job")
    head_sha = os.environ["EXPECTED_HEAD"]
    body = render_review(summary, changed, head_sha, Path(RULES_FILE).read_bytes(),
                         os.environ["BASE_SHA"], env_flag("RULES_CHANGED"))
    append_file("GITHUB_STEP_SUMMARY", body + "\n")
    review_id = publish_review(body, os.environ["GH_REPO"], int(os.environ["PR_NUMBER"]),
                               head_sha, gh_request)
    print(f"Published review {review_id}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    validate = commands.add_parser("validate", help="Validate the AI summary in CI")
    validate.add_argument("--dir", default=".review")
    commands.add_parser("publish", help="Publish the validated review")
    args = parser.parse_args()
    try:
        if args.command == "validate":
            validate_command(Path(args.dir))
        else:
            publish_command()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        append_file("GITHUB_STEP_SUMMARY",
                    f"## Use case review failed\n\n{html.escape(str(error))}\n")
        message = str(error).replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
        print(f"::error::{message}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())