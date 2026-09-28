# Copilot CLI review card POC

## Goal

Present the existing Copilot CLI PR summary as a GitHub pull request review
rather than appended text in the PR description. Keep Copilot code review (A)
and the structure check (C) unchanged.

## Design

The `generate` job continues to collect the diff and changed-file list, run
the `pr-summary` custom agent, and upload its Markdown artifact. The `publish`
job receives only `pull-requests: write`, checks that the PR head SHA still
matches the event, formats the summary as a Markdown review body, and posts it
through `POST /repos/{owner}/{repo}/pulls/{number}/reviews` with
`event: COMMENT`. It no longer edits the PR description. The review author
will be `github-actions[bot]`, not Copilot.

The body has a prominent PASS/FAIL heading, a purpose sentence, a table of
every changed file, and a collapsible rule-check list with rule IDs and paths.
These are Markdown/HTML elements rendered by GitHub, not native Copilot
severity badges, review effort metadata, AI identity, or line comments. The
publisher uses a hidden marker tied to the PR head SHA: if a review by
`github-actions[bot]` already contains this marker, it updates that review
through the review API instead of posting another. A new head SHA may receive
a new review. It must fail explicitly when the AI output or marker is invalid.

## Validation

Test the review-body formatter with FAIL and PASS sample output, including
HTML/Markdown formatting, complete changed-file coverage, missing verdict,
and duplicate publication. Run the existing four structure-check tests.
Verify a live FAIL and PASS PR: both get a B review card by
`github-actions[bot]`, no new B-generated PR description block, no duplicate
review for the same head SHA, and A/C results remain unchanged. New PRs or
reopening the closed POC PRs require separate user approval.

## Limits and alternative

Beautifying the PR description alone would be simpler but would not create a
review timeline card. Posting line-specific review comments would more closely
match native Copilot review but requires exact diff positions and duplicates
A's findings, so it is outside this POC. A repository `code-review` agent skill
could improve A's relevance, but GitHub decides when to use it and does not
guarantee complete per-file output. It is a separate experiment, not a
substitute for this deterministic publication path.
