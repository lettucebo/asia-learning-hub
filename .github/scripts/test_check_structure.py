import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from check_structure import check_changed_use_cases
from review_common import parse_rule_ids


class StructureChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def add(self, path):
        file = self.root / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text("Example", encoding="utf-8")

    def test_compliant_agent_builder_use_case(self):
        readme = "industry/FSI/Agent-Builder/relationship-manager-assistant/README.md"
        self.add(readme)
        self.add("industry/FSI/Agent-Builder/relationship-manager-assistant/setup.md")
        self.add("industry/FSI/Agent-Builder/relationship-manager-assistant/data-files/demo.zip")
        self.assertEqual([], check_changed_use_cases(self.root, [readme]))

    def test_replayed_commit_reports_each_independent_violation(self):
        root = "industry/FSI/Agent builder/Relationship Manager Assistant"
        self.add(f"{root}/README.md")
        self.add(f"{root}/demo.zip")
        issues = check_changed_use_cases(self.root, [f"{root}/README.md", f"{root}/demo.zip"])
        self.assertEqual({"STRUCT-01", "STRUCT-02", "STRUCT-04"},
                         {issue.rule for issue in issues})

    def test_missing_readme_and_setup(self):
        file = "industry/FSI/Foundry/demo/source/code.py"
        self.add(file)
        issues = check_changed_use_cases(self.root, [file])
        self.assertEqual({"STRUCT-03"}, {issue.rule for issue in issues})
        self.assertEqual(2, len(issues))

    def test_deleted_use_case_is_ignored(self):
        self.assertEqual([], check_changed_use_cases(
            self.root, ["industry/FSI/Copilot/removed/README.md"]))

    def test_file_directly_under_product_folder_is_reported(self):
        path = "industry/FSI/Copilot/orphaned.xlsx"
        self.add(path)
        issues = check_changed_use_cases(
            self.root, [path])
        self.assertEqual(["STRUCT-01"], [issue.rule for issue in issues])

    def test_deleted_product_level_file_is_not_reported(self):
        issues = check_changed_use_cases(
            None,
            ["industry/FSI/Copilot/orphaned.xlsx"],
            set(),
        )
        self.assertEqual([], issues)

    def test_moved_product_level_file_is_not_reported_at_source(self):
        source = "industry/FSI/Copilot/orphaned.xlsx"
        destination = "industry/FSI/Copilot/use-case/data-files/orphaned.xlsx"
        issues = check_changed_use_cases(
            None,
            [source, destination],
            {destination, "industry/FSI/Copilot/use-case/README.md"},
        )
        self.assertEqual([], issues)

    def test_regional_product_file_directly_under_product_folder_is_reported(self):
        path = "industry/FSI/Taiwan/Copilot/orphaned.xlsx"
        self.add(path)
        issues = check_changed_use_cases(
            self.root, [path])
        self.assertEqual(["STRUCT-01"], [issue.rule for issue in issues])

    def test_head_tree_paths_can_be_checked_without_checkout(self):
        paths = {
            "industry/FSI/Copilot/old-case/data-files/example.csv",
            "industry/FSI/Copilot/new-case/README.md",
        }
        issues = check_changed_use_cases(
            None,
            ["industry/FSI/Copilot/old-case/README.md",
             "industry/FSI/Copilot/new-case/README.md"],
            paths,
        )
        self.assertIn(("STRUCT-03", "industry/FSI/Copilot/old-case/README.md"),
                      [(issue.rule, issue.path) for issue in issues])

    def test_renamed_readme_source_case_is_still_checked(self):
        source = "industry/FSI/Copilot/old-case"
        destination = "industry/FSI/Copilot/new-case"
        self.add(f"{source}/data-files/example.csv")
        self.add(f"{destination}/README.md")
        issues = check_changed_use_cases(
            self.root, [f"{source}/README.md", f"{destination}/README.md"])
        self.assertIn(("STRUCT-03", f"{source}/README.md"),
                      [(issue.rule, issue.path) for issue in issues])


class RuleIdDrift(unittest.TestCase):
    def test_structure_rule_ids_are_defined_in_contributing(self):
        scripts = Path(__file__).resolve().parent
        used = set(re.findall(r'Issue\("([A-Z]+-\d{2})"',
                              (scripts / "check_structure.py").read_text(encoding="utf-8")))
        defined = set(parse_rule_ids(
            (scripts.parents[1] / "CONTRIBUTING.md").read_text(encoding="utf-8")))
        self.assertTrue(used)
        self.assertLessEqual(used, defined)


class GitTreeStructureCheck(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.repo = Path(temp.name)
        self.env = {
            **os.environ,
            "GIT_AUTHOR_NAME": "test",
            "GIT_AUTHOR_EMAIL": "test@example.com",
            "GIT_COMMITTER_NAME": "test",
            "GIT_COMMITTER_EMAIL": "test@example.com",
        }
        self.git("init", "-q", "-b", "main")
        self.git("config", "core.autocrlf", "false")

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.repo, env=self.env,
                              check=True, capture_output=True, text=True).stdout.strip()

    def write(self, path, content):
        file = self.repo / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(content, encoding="utf-8")

    def commit(self, message):
        self.git("add", "-A")
        self.git("commit", "-q", "-m", message)
        return self.git("rev-parse", "HEAD")

    def test_main_checks_rename_source_without_checkout(self):
        old = "industry/FSI/Copilot/old-case"
        new = "industry/FSI/Copilot/new-case"
        self.write(f"{old}/README.md", "same content")
        self.write(f"{old}/data-files/example.csv", "example")
        base = self.commit("base")
        (self.repo / f"{old}/README.md").unlink()
        self.write(f"{new}/README.md", "same content")
        head = self.commit("rename readme")

        script = Path(__file__).with_name("check_structure.py")
        result = subprocess.run(
            [sys.executable, str(script), base, head],
            cwd=self.repo, env=self.env, capture_output=True, text=True,
        )
        self.assertEqual(1, result.returncode, result.stdout + result.stderr)
        self.assertIn(f"[STRUCT-03] {old}/README.md", result.stdout)


if __name__ == "__main__":
    unittest.main()
