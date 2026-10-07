import unittest
from pathlib import Path

from publish_review import (
    find_existing, output_size_code_units, publish_review, render_review,
)
from review_common import parse_rule_ids

SHA = "a" * 40
BASE = "c" * 40
RULES = b"""# Contributing

## Review checks

| ID | Check |
| --- | --- |
| STRUCT-01 | Product folder. |
| STRUCT-02 | Kebab-case. |
| CONTENT-01 | README content. |

## Next section
"""
BAD_PATH = "industry/FSI/Agent builder/Relationship Manager Assistant"
GOOD_PATH = "industry/FSI/Agent-Builder/relationship-manager-assistant"
FAIL_SUMMARY = f"""## Purpose

Adds a relationship-manager demo.

## Changed files

- **Added** `{BAD_PATH}/README.md` — describes the scenario and demo.
- **Added** `{BAD_PATH}/demo.zip` — binary knowledge-source package; contents not examined.

## Rule check

- [STRUCT-01] FAIL — `{BAD_PATH}/` uses the wrong product folder.
- [STRUCT-02] FAIL — `{BAD_PATH}/` is not kebab-case.
- [CONTENT-01] PASS — README covers the required sections.

Verdict: FAIL
"""
FAIL_FILES = f"A\t{BAD_PATH}/README.md\nA\t{BAD_PATH}/demo.zip\n"
PASS_SUMMARY = f"""## Purpose

Adds a correctly laid out Agent Builder demo.

## Changed files

- **Added** `{GOOD_PATH}/README.md` — use case, scenario, and benefits.
- **Added** `{GOOD_PATH}/data-files/demo.zip` — binary sample; contents not examined.

## Rule check

- [STRUCT-01] PASS — correct product folder.
- [STRUCT-02] PASS — kebab-case name.
- [CONTENT-01] N/A — not applicable to this example.

Verdict: PASS
"""
PASS_FILES = f"A\t{GOOD_PATH}/README.md\nA\t{GOOD_PATH}/data-files/demo.zip\n"


def render(summary=FAIL_SUMMARY, files=FAIL_FILES, rules_changed=False):
    return render_review(summary, files, SHA, RULES, BASE, rules_changed)


class RuleIdTests(unittest.TestCase):
    def test_ids_come_only_from_review_checks_section(self):
        self.assertEqual(["STRUCT-01", "STRUCT-02", "CONTENT-01"],
                         parse_rule_ids(RULES.decode()))

    def test_repository_contributing_defines_checks(self):
        text = (Path(__file__).resolve().parents[2] / "CONTRIBUTING.md").read_text(
            encoding="utf-8")
        ids = parse_rule_ids(text)
        self.assertIn("STRUCT-01", ids)
        self.assertIn("CONTENT-01", ids)

    def test_missing_section_is_an_error(self):
        with self.assertRaisesRegex(ValueError, "Review checks"):
            parse_rule_ids("# Contributing\n")

    def test_job_output_size_uses_utf16_code_units(self):
        self.assertEqual(3, output_size_code_units("A", "😀"))


class ReviewFormattingTests(unittest.TestCase):
    def test_fail_review_lists_every_check_and_file(self):
        body = render()
        self.assertIn("FAIL", body)
        self.assertIn("Review checks (2 failed of 3)", body)
        self.assertIn("| CONTENT-01 | \u2705 PASS |", body)
        self.assertIn(f"| Added | `{BAD_PATH}/demo.zip` |", body)
        self.assertEqual(1, body.count(f"<!-- use-case-review:{SHA} -->"))

    def test_pass_review(self):
        body = render(PASS_SUMMARY, PASS_FILES)
        self.assertIn("All review checks passed", body)
        self.assertIn("Review checks (0 failed of 3)", body)
        self.assertEqual(2, body.count("| Added |"))

    def test_provenance_is_computed_from_rules(self):
        import hashlib
        body = render()
        digest = hashlib.sha256(RULES).hexdigest()[:12]
        self.assertIn(f"`CONTRIBUTING.md` @ `{BASE[:7]}` (sha256 `{digest}`)", body)

    def test_rules_changed_adds_warning(self):
        self.assertNotIn("[!WARNING]", render())
        self.assertIn("[!WARNING]", render(rules_changed=True))

    def test_missing_rule_id_is_an_error(self):
        summary = FAIL_SUMMARY.replace(
            "- [CONTENT-01] PASS — README covers the required sections.\n", "")
        with self.assertRaisesRegex(ValueError, "Missing rule check IDs: CONTENT-01"):
            render(summary)

    def test_zero_rule_ids_is_an_error(self):
        summary = PASS_SUMMARY.split("## Rule check")[0] + (
            "## Rule check\n\nNo violations found.\n\nVerdict: PASS\n")
        with self.assertRaisesRegex(ValueError, "Invalid rule check line"):
            render(summary, PASS_FILES)

    def test_unknown_rule_id_is_an_error(self):
        summary = FAIL_SUMMARY.replace("[CONTENT-01]", "[CONTENT-09]")
        with self.assertRaisesRegex(ValueError, "Unknown rule check ID"):
            render(summary)

    def test_duplicate_rule_id_is_an_error(self):
        summary = FAIL_SUMMARY.replace("[CONTENT-01]", "[STRUCT-01]")
        with self.assertRaisesRegex(ValueError, "Duplicate rule check ID"):
            render(summary)

    def test_fail_without_path_is_an_error(self):
        summary = FAIL_SUMMARY.replace(f"`{BAD_PATH}/` is not kebab-case", "not kebab-case")
        with self.assertRaisesRegex(ValueError, "without a path"):
            render(summary)

    def test_verdict_must_match_results(self):
        with self.assertRaisesRegex(ValueError, "Verdict disagrees"):
            render(FAIL_SUMMARY.replace("Verdict: FAIL", "Verdict: PASS"))
        with self.assertRaisesRegex(ValueError, "Verdict disagrees"):
            render(PASS_SUMMARY.replace("Verdict: PASS", "Verdict: FAIL"), PASS_FILES)

    def test_empty_summary_is_an_error(self):
        with self.assertRaisesRegex(ValueError, "empty"):
            render("")

    def test_missing_changed_file_is_an_error(self):
        with self.assertRaisesRegex(ValueError, "missing"):
            render(files=FAIL_FILES + "A\tother.txt\n")

    def test_invalid_verdict_is_an_error(self):
        with self.assertRaisesRegex(ValueError, "Verdict"):
            render(FAIL_SUMMARY.replace("Verdict: FAIL", "Verdict: MAYBE"))

    def test_invalid_sha_is_an_error(self):
        with self.assertRaisesRegex(ValueError, "SHA"):
            render_review(FAIL_SUMMARY, FAIL_FILES, "unsafe", RULES, BASE)
        with self.assertRaisesRegex(ValueError, "SHA"):
            render_review(FAIL_SUMMARY, FAIL_FILES, SHA, RULES, "unsafe")

    def test_only_bot_review_with_exact_marker_can_be_reused(self):
        marker = f"<!-- use-case-review:{SHA} -->"
        reviews = [
            {"id": 1, "user": {"login": "Copilot"}, "body": marker},
            {"id": 2, "user": {"login": "github-actions[bot]"},
             "body": "<!-- use-case-review:" + "b" * 40 + " -->"},
            {"id": 3, "user": {"login": "github-actions[bot]"}, "body": marker},
        ]
        self.assertEqual(3, find_existing(reviews, marker))
        self.assertIsNone(find_existing(reviews[:2], marker))


class PublishingTests(unittest.TestCase):
    def test_new_review_is_a_comment_on_the_expected_commit(self):
        calls = []

        def request(method, path, payload=None):
            calls.append((method, path, payload))
            if path.endswith("/pulls/4"):
                return {"head": {"sha": SHA}}
            if "/reviews" in path and method == "GET":
                return []
            return {"id": 7}

        publish_review(render(), "owner/repo", 4, SHA, request)
        self.assertEqual("POST", calls[-1][0])
        self.assertEqual("COMMENT", calls[-1][2]["event"])
        self.assertEqual(SHA, calls[-1][2]["commit_id"])

    def test_rerun_updates_same_bot_review(self):
        calls = []

        def request(method, path, payload=None):
            calls.append((method, path, payload))
            if path.endswith("/pulls/4"):
                return {"head": {"sha": SHA}}
            if method == "GET":
                return [{"id": 11, "user": {"login": "github-actions[bot]"},
                         "body": f"<!-- use-case-review:{SHA} -->"}]
            return {"id": 11}

        publish_review(render(), "owner/repo", 4, SHA, request)
        self.assertEqual("PUT", calls[-1][0])
        self.assertTrue(calls[-1][1].endswith("/reviews/11"))
        self.assertEqual({"body"}, set(calls[-1][2]))

    def test_stale_head_does_not_publish(self):
        calls = []

        def request(method, path, payload=None):
            calls.append((method, path))
            return {"head": {"sha": "b" * 40}}

        with self.assertRaisesRegex(ValueError, "head"):
            publish_review(render(), "owner/repo", 4, SHA, request)
        self.assertEqual(1, len(calls))


if __name__ == "__main__":
    unittest.main()