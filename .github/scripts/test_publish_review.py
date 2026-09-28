import unittest

from publish_review import find_existing, publish_review, render_review


SHA = "a" * 40
BAD_PATH = "industry/FSI/Agent builder/Relationship Manager Assistant"
GOOD_PATH = "industry/FSI/Agent-Builder/relationship-manager-assistant"
FAIL_SUMMARY = f"""## Purpose

Adds a relationship-manager demo.

## Changed files

- **Added** `{BAD_PATH}/README.md` — describes the scenario and demo.
- **Added** `{BAD_PATH}/demo.zip` — binary knowledge-source package; contents not examined.

## Rule check

- [STRUCT-01] `{BAD_PATH}/` — wrong product folder.
- [STRUCT-02] `{BAD_PATH}/` — name is not kebab-case.
- [STRUCT-04] `{BAD_PATH}/demo.zip` — put the package in data-files.

Verdict: FAIL
"""
FAIL_FILES = f"A\t{BAD_PATH}/README.md\nA\t{BAD_PATH}/demo.zip\n"
PASS_SUMMARY = f"""## Purpose

Adds a correctly laid out Agent Builder demo.

## Changed files

- **Added** `{GOOD_PATH}/README.md` — use case, scenario, and benefits.
- **Added** `{GOOD_PATH}/setup.md` — environment and setup.
- **Added** `{GOOD_PATH}/data-files/demo.zip` — binary sample; contents not examined.

## Rule check

No violations found.

Verdict: PASS
"""
PASS_FILES = (f"A\t{GOOD_PATH}/README.md\nA\t{GOOD_PATH}/setup.md\n"
              f"A\t{GOOD_PATH}/data-files/demo.zip\n")


class ReviewFormattingTests(unittest.TestCase):
    def test_fail_review_includes_every_file_and_collapsible_findings(self):
        body = render_review(FAIL_SUMMARY, FAIL_FILES, SHA)
        self.assertIn("FAIL", body)
        self.assertIn("Rule check (3)", body)
        self.assertIn("<details", body)
        self.assertIn(f"| Added | `{BAD_PATH}/demo.zip` |", body)
        self.assertEqual(1, body.count(f"<!-- poc-cli-review:{SHA} -->"))

    def test_pass_review_has_three_files_and_no_findings(self):
        body = render_review(PASS_SUMMARY, PASS_FILES, SHA)
        self.assertIn("PASS", body)
        self.assertIn("No POC issues found", body)
        self.assertIn("Rule check (0)", body)
        self.assertEqual(3, body.count("| Added |"))

    def test_missing_changed_file_is_an_error(self):
        with self.assertRaisesRegex(ValueError, "missing"):
            render_review(FAIL_SUMMARY, FAIL_FILES + "A\tother.txt\n", SHA)

    def test_invalid_verdict_is_an_error(self):
        with self.assertRaisesRegex(ValueError, "Verdict"):
            render_review(FAIL_SUMMARY.replace("Verdict: FAIL", "Verdict: MAYBE"),
                          FAIL_FILES, SHA)

    def test_invalid_head_sha_is_an_error(self):
        with self.assertRaisesRegex(ValueError, "SHA"):
            render_review(FAIL_SUMMARY, FAIL_FILES, "unsafe")

    def test_only_bot_review_with_exact_marker_can_be_reused(self):
        marker = f"<!-- poc-cli-review:{SHA} -->"
        reviews = [
            {"id": 1, "user": {"login": "Copilot"}, "body": marker},
            {"id": 2, "user": {"login": "github-actions[bot]"},
             "body": "<!-- poc-cli-review:" + "b" * 40 + " -->"},
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
            if path.endswith("/reviews") and method == "GET":
                return []
            return {"id": 7}

        publish_review(FAIL_SUMMARY, FAIL_FILES, "lettucebo/asia-learning-hub",
                       4, SHA, request)
        self.assertTrue(calls, "publisher did not call the review API")
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
                         "body": f"<!-- poc-cli-review:{SHA} -->"}]
            return {"id": 11}

        publish_review(FAIL_SUMMARY, FAIL_FILES, "lettucebo/asia-learning-hub",
                       4, SHA, request)
        self.assertTrue(calls, "publisher did not call the review API")
        self.assertEqual("PUT", calls[-1][0])
        self.assertTrue(calls[-1][1].endswith("/reviews/11"))
        self.assertEqual({"body"}, set(calls[-1][2]))

    def test_stale_head_does_not_publish(self):
        calls = []

        def request(method, path, payload=None):
            calls.append((method, path))
            return {"head": {"sha": "b" * 40}}

        with self.assertRaisesRegex(ValueError, "head"):
            publish_review(FAIL_SUMMARY, FAIL_FILES,
                           "lettucebo/asia-learning-hub", 4, SHA, request)
        self.assertEqual(1, len(calls))


if __name__ == "__main__":
    unittest.main()
