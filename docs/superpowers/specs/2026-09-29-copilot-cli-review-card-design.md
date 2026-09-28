# Copilot review skill and CLI review card POC

## Goal

Compare an improved Copilot code review (A) with a Copilot CLI summary presented
as a pull request review card (B), using new PASS and FAIL PRs against the same
isolated base branch. Keep the deterministic structure check (C) unchanged.

## A: Code review skill

Add `.github/skills/code-review/SKILL.md` with review-focused frontmatter and
instructions to use `RULE.md` and the existing `.github/copilot-instructions.md`.
Ask for an overview listing **every** changed file, including the name and
role of binary files without claiming to inspect their contents, and the
affected industry, product, use case, and POC rule findings. Distinguish
repository-wide minimum use-case counts from checks of changed use cases;
do not misrepresent either as the other. Do not add MCP servers or duplicate
the full rule set in the skill.

GitHub decides when relevant skills are loaded, and the overview format is
controlled by Copilot code review. This experiment measures whether a focused
skill increases file coverage; it cannot guarantee B's output shape or update
the PR description. Inspect review attributions or session logs to determine
whether the new skill was used.

## B: CLI review card

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
and duplicate publication. Check the `SKILL.md` frontmatter and instructions
against the documented skill format. Run the existing four structure-check
tests.

Update `e2e/base`, then create new FAIL and PASS head branches **from the
updated base** so the skill is present in each head branch when A reviews the
PR. Replay the same twelve historical commits for FAIL and add the same
compliant use case for PASS. Verify in both PRs:

* A runs automatically, flags STRUCT-01/02/04 on FAIL and no POC structural
  violations on PASS; record its exact changed-file coverage and distinguish
  separate repository-wide advice. Check if the skill was used through
  attributions or session logs.
* B posts one `github-actions[bot]` review card with every changed file and
  the correct verdict, without writing a new PR description block. A rerun
  on the same SHA does not create a duplicate review.
* C remains FAILURE with three issues on FAIL and SUCCESS with none on PASS.

Compare against the previous closed PRs #1 and #2; write the results in the
session report, then close the two new PRs without merging. Leave `main` and
the old PRs unchanged.

## Limits and alternative

Beautifying the PR description alone would be simpler but would not create a
review timeline card. Posting line-specific review comments would more closely
match native Copilot review but requires exact diff positions and duplicates
A's findings, so it is outside this POC. A custom instruction alone already
omitted the binary ZIP from both prior overviews; the skill is a focused second
experiment, not a substitute for B's explicit per-file publication path.
