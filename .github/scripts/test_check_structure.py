import re
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


class RuleIdDrift(unittest.TestCase):
    def test_structure_rule_ids_are_defined_in_contributing(self):
        scripts = Path(__file__).resolve().parent
        used = set(re.findall(r'Issue\("([A-Z]+-\d{2})"',
                              (scripts / "check_structure.py").read_text(encoding="utf-8")))
        defined = set(parse_rule_ids(
            (scripts.parents[1] / "CONTRIBUTING.md").read_text(encoding="utf-8")))
        self.assertTrue(used)
        self.assertLessEqual(used, defined)


if __name__ == "__main__":
    unittest.main()
