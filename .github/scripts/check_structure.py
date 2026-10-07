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


def check_changed_use_cases(root: Path | None, changed_paths: list[str],
                            head_paths: set[str] | None = None) -> list[Issue]:
    def is_dir(path: Path) -> bool:
        if head_paths is not None:
            prefix = path.as_posix().rstrip("/") + "/"
            return any(candidate.startswith(prefix) for candidate in head_paths)
        return root is not None and (root / path).is_dir()

    def is_file(path: Path) -> bool:
        if head_paths is not None:
            return path.as_posix() in head_paths
        return root is not None and (root / path).is_file()

    def children(path: Path) -> set[tuple[str, bool]]:
        if head_paths is not None:
            prefix = path.as_posix().rstrip("/") + "/"
            result = set()
            for candidate in head_paths:
                if candidate.startswith(prefix):
                    remainder = candidate[len(prefix):]
                    first, separator, _ = remainder.partition("/")
                    result.add((first, bool(separator)))
            return result
        if root is None:
            return set()
        return {
            (child.name, child.is_dir())
            for child in (root / path).iterdir()
        }

    candidates = set()
    issues = []
    for name in changed_paths:
        parts = Path(name).parts
        if len(parts) < 3 or parts[0] != "industry":
            continue
        product_index = (
            2 if parts[2] in PRODUCTS else
            3 if len(parts) > 3 and (parts[3] in PRODUCTS or len(parts) >= 6) else
            2
        )
        if len(parts) <= product_index:
            continue
        if len(parts) == product_index + 2:
            product_folder = parts[product_index]
            path = Path(*parts)
            if (product_folder in PRODUCTS or product_index == 2) and is_file(path):
                issues.append(Issue(
                    "STRUCT-01", path.as_posix(),
                    "Use-case files must be inside a use-case directory",
                ))
            continue
        folder = Path(*parts[: product_index + 2])
        if is_dir(folder):
            candidates.add((folder, product_index))

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
            if not is_file(folder / required):
                issues.append(Issue("STRUCT-03", f"{relative}/{required}", f"Missing {required}"))
        support = SUPPORT_DIRS.get(product, {"data-files"})
        for child_name, is_directory in children(folder):
            if not is_directory and child_name not in {"README.md", "setup.md"}:
                issues.append(Issue("STRUCT-04", f"{relative}/{child_name}",
                                    "Supporting file must be in " + ", ".join(sorted(support))))
            elif is_directory and child_name not in support:
                issues.append(Issue("STRUCT-04", f"{relative}/{child_name}",
                                    "Unexpected supporting directory"))
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("base", help="Pull request base commit SHA")
    parser.add_argument("head", help="Pull request head commit SHA")
    args = parser.parse_args()
    result = subprocess.run(
        ["git", "diff", "--name-only", "--no-renames", "-z",
         f"{args.base}...{args.head}", "--", "industry/"],
        check=True, capture_output=True,
    )
    changed = [os.fsdecode(path) for path in result.stdout.split(b"\0") if path]
    tree = subprocess.run(
        ["git", "ls-tree", "-r", "-z", "--name-only", args.head, "--", "industry/"],
        check=True, capture_output=True,
    )
    head_paths = {os.fsdecode(path) for path in tree.stdout.split(b"\0") if path}
    issues = check_changed_use_cases(None, changed, head_paths)
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
