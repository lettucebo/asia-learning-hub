import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


PRODUCTS = {"Copilot", "Agent-Builder", "Copilot-Studio", "Foundry", "Fabric"}
SUPPORT_DIRS = {
    "Copilot": {"data-files"},
    "Agent-Builder": {"data-files"},
    "Copilot-Studio": {"data-files"},
    "Foundry": {"source"},
    "Fabric": {"notebook", "data"},
}


@dataclass(frozen=True)
class Issue:
    rule: str
    path: str
    message: str


def check_changed_use_cases(root: Path, changed_paths: list[str]) -> list[Issue]:
    candidates = set()
    for name in changed_paths:
        parts = Path(name).parts
        if len(parts) < 5 or parts[0] != "industry":
            continue
        product_index = 2 if parts[2] in PRODUCTS else 3 if parts[3] in PRODUCTS else 2
        if len(parts) < product_index + 3:
            continue
        folder = Path(*parts[: product_index + 2])
        if (root / folder).is_dir():
            candidates.add((folder, product_index))

    issues = []
    for folder, product_index in sorted(candidates):
        parts = folder.parts
        product = parts[product_index]
        use_case = parts[-1]
        relative = folder.as_posix()
        if product not in PRODUCTS:
            issues.append(Issue("STRUCT-01", relative, f"Invalid product folder: {product}"))
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", use_case):
            issues.append(Issue("STRUCT-02", relative, f"Use case must be kebab-case: {use_case}"))
        for required in ("README.md", "setup.md") if product in {"Copilot-Studio", "Foundry", "Fabric"} else ("README.md",):
            if not (root / folder / required).is_file():
                issues.append(Issue("STRUCT-03", f"{relative}/{required}", f"Missing {required}"))
        support = SUPPORT_DIRS.get(product, {"data-files"})
        for child in (root / folder).iterdir():
            if child.is_file() and child.name not in {"README.md", "setup.md"}:
                issues.append(Issue("STRUCT-04", f"{relative}/{child.name}",
                                    "Supporting file must be in " + ", ".join(sorted(support))))
            elif child.is_dir() and child.name not in support:
                issues.append(Issue("STRUCT-04", f"{relative}/{child.name}",
                                    "Unexpected supporting directory"))
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("base", help="Pull request base commit SHA")
    parser.add_argument("head", help="Pull request head commit SHA")
    args = parser.parse_args()
    result = subprocess.run(
        ["git", "diff", "--name-only", "-z", f"{args.base}...{args.head}"],
        check=True, capture_output=True,
    )
    changed = [os.fsdecode(path) for path in result.stdout.split(b"\0") if path]
    issues = check_changed_use_cases(Path.cwd(), changed)
    summary = ["## Structure check", f"{len(issues)} issue(s) in changed use cases."]
    for issue in issues:
        text = f"[{issue.rule}] {issue.path}: {issue.message}"
        print(f"::error file={issue.path}::{text.replace('%', '%25').replace(chr(10), '%0A')}")
        summary.append(f"- {text}")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as output:
            output.write("\n".join(summary) + "\n")
    else:
        print("\n".join(summary))
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
