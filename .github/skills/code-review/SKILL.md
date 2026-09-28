---
name: code-review
description: Use when reviewing a pull request that changes industry use cases and needs a complete file-by-file change overview.
---

# Industry use-case PR review

Use `RULE.md` and `.github/copilot-instructions.md` for this repository's
review criteria. For the review overview, use the PR's full changed-file list
as a checklist before writing a summary.

## Overview contract

Include a "What changed in this PR" table with **one row per changed file**:
path, added/modified/deleted status, and the file's purpose in this change.
Include binary files such as ZIP archives by path and role; say their contents
were not inspected rather than inventing what they contain. Identify the
industry, product, and use case affected, then state whether the **changed
use cases** meet the POC structure and README rules.

List violations with the relevant `STRUCT-*` or `CONTENT-*` rule ID and path.
The minimum number of use cases in `RULE.md` is a separate **repository-wide**
requirement: report it as context when relevant, not as a structural defect
in a correctly laid out changed use case. If the complete changed-file list is
unavailable, state that file coverage could not be verified.
