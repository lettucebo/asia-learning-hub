# Asia Learning Hub

This repository holds reusable learning and demo assets for the Asia MTT
community. `industry\README.md` is the navigation index; each industry/product
use case is an independent demo package with its own story, data/knowledge,
setup, and, where applicable, code or exported Power Platform solution.
Read the case README and setup guide together before changing its assets.

Use `RULE.md` for the standardized layout and `Instruction.txt` for delivery
workflow. The coverage and Publisher Name rules below incorporate the updated
Industry Readiness guidelines and supersede the older values in those files.

## Industry use cases

- Add new cases under `industry\<Industry>\<Product>\<kebab-case-use-case>\`.
  Use the product directory names in `RULE.md`: `Copilot`, `Agent-Builder`,
  `Copilot-Studio`, `Foundry`, or `Fabric`. Put country-specific variants in
  a country/region subfolder when needed, rather than making the shared case
  country-specific.
- Each use-case `README.md` should cover the scenario, pain points, benefits,
  demo steps, and demo outcome. Write concise demo handoffs for MTTs who
  already know the products, rather than detailed training/lab guides or
  repeated product-feature explanations. Curate, simplify, and streamline
  Copilot/Cowork-generated material before check-in instead of publishing raw
  generated output. Agent Builder cases also document the agent configuration.
  For agents, Foundry, and Fabric, `RULE.md` requests environment/setup
  guidance in `setup.md`; its Agent-Builder diagram omits that file, so clarify
  the expectation before treating its absence as a violation.
- Keep supporting files with their use case: `data-files\` for Copilot,
  Agent Builder, and Copilot Studio; `source\` for Foundry code; `notebook\`
  and `data\` for Fabric assets. Use publicly available reference data and
  fictitious customer names.
- Preserve existing space-containing or legacy directory names and artifact
  locations unless a migration is requested. Resolve references against actual
  files; old index/package links are not templates for new cases.
- Have another team member reproduce the setup and verify the instructions
  before treating a deliverable as complete.

### Product coverage

Assess coverage per industry, separately from an individual case's compliance.
The baseline is 2 Copilot, 2 Agent Builder, 1 Copilot Studio, 1 Foundry, and
1 Fabric case. Copilot coverage spans Chat, Word, PowerPoint, Excel, Outlook,
and Teams. Apply these Foundry/Fabric exceptions:

- Healthcare, Public Sector (`PS`), and Telco have no Fabric requirement.
- Retail has neither a Foundry nor a Fabric requirement.
- Digital Native and IT/ITeS share the same Foundry and Fabric cases; count
  shared cases for both industries rather than duplicating the assets.

## Copilot Studio delivery

For new Studio cases, use the **Microsoft Copilot harness**. Preserve existing
standard-harness cases unless their migration is requested.

- Create one custom solution per demo agent and set it as the preferred
  solution before creating the agent. Verify the agent and all required
  components belong to that solution. Let Copilot Studio generate schema
  names; name the solution after the use case, shortening it if necessary.
- Prefer Dataverse and file-based data sources/tools to reduce environment
  complexity; this is a preference, not a ban on other integrations.
- Test the agent, then export the solution and check in the actual package.
  The README includes a concise component list (skills, knowledge, tools and
  their purposes), the real package path, post-import setup such as file
  uploads/connections, and demo steps. Link to case-local setup guidance;
  detailed agent-creation instructions are not required.

Use these **Publisher Name** values for new solutions. Keep customization
prefixes and display names as documented in `RULE.md`'s publisher table;
short names do not imply new prefixes. Preserve publishers in existing exports.

| Industry directory | Publisher Name |
| --- | --- |
| `Digital Native` | `DN` |
| `FSI` | `FSI` |
| `PS` | `PS` |
| `Healthcare` | `HC` |
| `IT-ITeS` | `IT` |
| `Manufacturing-Mobility` | `MFG` |
| `Retail` | `RET` |
| `Telco` | `TEL` |

## Demo commands and verification

The Foundry Quality Root-Cause demo runs locally using Microsoft Agent
Framework: `main.py` validates local inputs, then `workflow.py` passes evidence
through DataAnalysisAgent, KnowledgeAgent, and ReportAgent sequentially.
Python tools calculate from CSVs and read past reports; the model explains
the evidence. It calls an existing Foundry deployment rather than creating
cloud agents or deployments.

First follow `industry\Manufacturing-Mobility\Foundry\Quality Root-Cause Agent\setup.md`
for prerequisites, the virtual environment/pinned requirements, Azure sign-in,
and local configuration. After setup, run from the repository root:

```powershell
Set-Location -LiteralPath '.\industry\Manufacturing-Mobility\Foundry\Quality Root-Cause Agent\source' -ErrorAction Stop
.\.venv\Scripts\python.exe main.py
```

This run sends tool evidence to the model and incurs model charges; obtain
approval before invoking it. Use the setup guide's report/peer checklist to
verify the result, not just successful process exit.

Studio verification is case-specific and tenant-based:

- To run a single case, choose one documented test prompt and start a new
  Preview/test-pane conversation unless the case specifies a multi-turn
  sequence. Compare the answer and required source/tool evidence with the
  expected result.
- Example: after Retail Click & Collect setup, run CS-01 from
  `industry\Retail\Copilot Studio\Click & Collect Recovery Agent\acceptance_tests.csv`:
  `Review CC-101 at the fixed demo time.` Expect an urgent Store Fulfilment
  Lead status check supported by CC-101 and CR-3, not a readiness promise.
  Its `setup.md` describes running all eight acceptance cases.
- For FSI ratio checks, use
  `industry\FSI\Copilot-Studio\Commercial Credit Health Ratio Analyzer\SETUP.md`,
  section 5. For the Telco regression set, use
  `industry\Telco\Copilot Studio\NOC Incident Coach\README.md`,
  "Evaluate the agent"; preserve its multi-turn conversations and documented
  starting-data assumptions.
