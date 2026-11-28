# Acceptance: Juniper Lane Omnichannel Service Agent

[繁體中文](README.zh-TW.md)

| Set | Cases |
| --- | --- |
| [Click & Collect Recovery](collect.csv) | `CS-01`–`CS-08`: exact order, deadline, consent, closed records, and freshness. |
| [Returns & Exchange Coach](returns.csv) | `AB-01`–`AB-10`: evidence, policy boundaries, escalation, and exceptions. |
| [Foundry integration](foundry.csv) | `FD-01`–`FD-04`: intent routing, conversation isolation between routes, and unavailable evidence. |

These are presenter-only inputs and expected results. Never index or provide this directory to the agent as knowledge.

Use the [Playground walkthrough](playground.md) for copy-ready English prompts, real screenshots, and observed deviations. The CSVs remain the acceptance source of truth.

## Run and score

- Start a new conversation per case. For `FD-03`, send both turns in the same conversation and score each turn against its own evidence. For `FD-04`, match the candidate's instructions, deployment, and tool settings in an isolated configuration, with the same knowledge files **except** `recovery_policy.txt`. Record the isolated configuration and file list separately. Do not change the saved candidate or its vector store.
- Check the expected route, owner where specified, required evidence, and prohibited claims. In Playground, inspect response details, source annotations, or tool traces. For positive order evidence, confirm the retrieved material contains the exact order record; for policy evidence, confirm the required sections were retrieved. When the case expects clarification before retrieval or an unavailable source, verify the stated absence and safe stop instead.
- Mark a case failed if retrieval cannot be verified when required, the answer borrows evidence across routes, or it claims an action or certainty the sources do not support. Do not turn a failed run into a pass by retrying the same conversation. If you change the configuration, record the change and rerun the matrix on the replacement candidate.

Record: test ID and turn, UI or SDK, exact agent version, model deployment (alias in shared records), observed route, tool/source evidence, prohibited-claim check, pass/fail, and verifier. Use sanitized file and rule identifiers, not raw trace exports. Have a teammate reproduce the portal setup and checks before exporting. SDK parity uses the same scenarios and evidence standard, not identical phrasing.

**Actual results:** The walkthrough records one v3 Playground run: 21 cases captured, four cases with observed deviations, and `FD-04` not run. It is not a trace-level or peer sign-off and does not qualify the version for export.
