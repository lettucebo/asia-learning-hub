import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

from prepare_review import prepare

RULES = """# Contributing

## Review checks

| ID | Check |
| --- | --- |
| STRUCT-01 | Product folder. |
| CONTENT-01 | README content. |
"""
CASE = "industry/FSI/Agent-Builder/demo-case"


class PrepareReviewTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.repo = Path(temp.name) / "repo"
        self.repo.mkdir()
        self.env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.com",
                    "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.com"}
        self.git("init", "-q", "-b", "main")
        self.git("config", "core.autocrlf", "false")

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.repo, env=self.env, check=True,
                              capture_output=True, text=True).stdout.strip()

    def write(self, path, text):
        file = self.repo / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(text, encoding="utf-8", newline="\n")

    def commit(self, message):
        self.git("add", "-A")
        self.git("commit", "-q", "-m", message)
        return self.git("rev-parse", "HEAD")

    def run_prepare(self, base, head):
        return prepare(base, head, self.repo / ".review", self.repo)

    def test_prompt_embeds_full_base_rules_and_lists_head_files(self):
        self.write("CONTRIBUTING.md", RULES)
        self.write("industry/README.md", "Industries")
        base = self.commit("base")
        self.write(f"{CASE}/README.md", "Scenario and demo steps")
        (self.repo / f"{CASE}/data-files").mkdir(parents=True)
        (self.repo / f"{CASE}/data-files/demo.zip").write_bytes(b"PK\0\0binary")
        head = self.commit("head")

        result = self.run_prepare(base, head)
        review = self.repo / ".review"
        prompt = (review / "prompt.md").read_text(encoding="utf-8")
        self.assertFalse(result["skipped"])
        self.assertIn(RULES.rstrip(), prompt)
        self.assertIn("STRUCT-01, CONTENT-01", prompt)
        self.assertIn(f"`.review/head/{CASE}/README.md`", prompt)
        self.assertEqual("Scenario and demo steps",
                         (review / "head" / CASE / "README.md").read_text(encoding="utf-8"))
        self.assertFalse((review / "head" / CASE / "data-files/demo.zip").exists())
        self.assertEqual(f"A\t{CASE}/README.md\nA\t{CASE}/data-files/demo.zip\n",
                         (review / "changed-files.txt").read_text(encoding="utf-8"))
        self.assertFalse(result["rules_changed"])

    def test_rules_are_taken_from_base_and_change_is_flagged(self):
        self.write("CONTRIBUTING.md", RULES)
        base = self.commit("base")
        self.write("CONTRIBUTING.md", RULES + "| STRUCT-99 | Injected. |\n")
        self.write(f"{CASE}/README.md", "Scenario")
        head = self.commit("head")

        result = self.run_prepare(base, head)
        prompt = (self.repo / ".review/prompt.md").read_text(encoding="utf-8")
        self.assertTrue(result["rules_changed"])
        self.assertNotIn("STRUCT-99", prompt)

    def test_skips_without_industry_changes(self):
        self.write("CONTRIBUTING.md", RULES)
        base = self.commit("base")
        self.write("docs/notes.md", "Notes")
        head = self.commit("head")

        result = self.run_prepare(base, head)
        self.assertTrue(result["skipped"])
        self.assertIn("industry/", result["reason"])
        self.assertFalse((self.repo / ".review/prompt.md").exists())

    def test_skips_when_base_has_no_rules(self):
        self.write("README.md", "Hub")
        base = self.commit("base")
        self.write(f"{CASE}/README.md", "Scenario")
        head = self.commit("head")

        result = self.run_prepare(base, head)
        self.assertTrue(result["skipped"])
        self.assertIn("CONTRIBUTING.md", result["reason"])

    def test_refuses_to_reuse_a_foreign_output_directory(self):
        self.write("CONTRIBUTING.md", RULES)
        base = self.commit("base")
        self.write(".review/keep.txt", "user file")
        with self.assertRaisesRegex(ValueError, "not created by this script"):
            self.run_prepare(base, base)
        self.assertTrue((self.repo / ".review/keep.txt").exists())

    def test_rerun_replaces_previous_output(self):
        self.write("CONTRIBUTING.md", RULES)
        base = self.commit("base")
        self.write(f"{CASE}/README.md", "Scenario")
        head = self.commit("head")
        self.run_prepare(base, head)
        result = self.run_prepare(base, head)
        self.assertFalse(result["skipped"])
        json.dumps({k: v for k, v in result.items()})


if __name__ == "__main__":
    unittest.main()
