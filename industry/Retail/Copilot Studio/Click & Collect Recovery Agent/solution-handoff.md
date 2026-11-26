# Solution handoff: Retail Collect Recovery

**Pending tenant build, tests, peer verification, and export.** This file is not an importable solution. Do not mark the Copilot Studio deliverable complete until the export and clean-environment import have both been verified.

## Naming and contents

| Item | Required value |
|---|---|
| Publisher display name | `Retail&ConsumerGoods` |
| Publisher prefix | `rt` |
| Solution display name | `Retail Collect Recovery` |
| Solution unique name | `RetailCollectRecovery` |
| Initial version | `1.0.0.0` |
| Agent name | `Juniper Lane Click & Collect Recovery Agent` |
| Agent/component schema | Let Copilot Studio generate it; do not hand-edit generated internals |
| Packaging | One custom solution containing this agent and required components |
| Planned export location | `solution\RetailCollectRecovery_1_0_0_0.zip` (does not exist yet) |

Set this custom solution as preferred **before** creating the agent. Confirm ownership in the solution explorer rather than assuming it worked.

## Export after testing

1. Complete [setup.md](setup.md), pass all eight acceptance cases, and have a second person reproduce them. Record the results below.
2. In the custom solution, include the agent and use **Add required objects**. Inspect topics, instructions, and knowledge dependencies. Do not assume knowledge file contents or data rows transfer automatically with a solution.
3. Publish customizations as required for export; this is not publishing an agent channel. Export an **unmanaged** solution for this reusable demo, version 1.0.0.0, to the planned location. Do not manufacture a ZIP from these preparation files.
4. Import that export into a separate permitted nonproduction environment. Confirm the publisher, agent instructions, and all required dependencies. Re-upload `orders.csv` and `recovery_policy.txt` if the imported knowledge is missing or unprocessed.
5. Repeat all eight cases after import. Add the actual ZIP and update the README with its real path, tested version, import dependencies, verifier, and date. Re-export a new version if changes were needed; do not label an untested archive as verified.

## Completion record

| Item | Actual result |
|---|---|
| Source environment build | Pending |
| Eight acceptance cases | Pending |
| Peer verifier and verification date | Pending |
| Export archive and version | Not created |
| Clean-environment import | Pending |
| Post-import knowledge check and eight cases | Pending |

References: [preferred/custom solutions](https://learn.microsoft.com/microsoft-copilot-studio/authoring-solutions-overview), [export and import agents using solutions](https://learn.microsoft.com/microsoft-copilot-studio/authoring-solutions-import-export). Instructions in the repository's root `Instruction.txt` determine the Retail publisher convention.
