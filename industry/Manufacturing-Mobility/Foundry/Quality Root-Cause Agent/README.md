# Quality Root-Cause Agent

**From a quality drop to an investigation plan:** A short Python demo in which three AI roles, running on a Microsoft Foundry model, help a Contoso Quality Engineer decide what to check next after a drop in first-inspection pass rate.

**Audience:** MTTs presenting Microsoft Foundry to manufacturing customers. **Format:** one command, one report, no front end.

## Business Scenario

Contoso is a fictitious electronics manufacturer. On Plant A Line 1, which builds Power Modules, about 97% of products normally pass their first inspection without rework or retesting. In W42, this **first-inspection pass rate** fell to 93.6%. In W43 it recovered.

| Reporting week (W40-W43 are weeks 40-43) | W40 | W41 | W42 | W43 |
|---|---|---|---|---|
| First-inspection pass rate | 97.5% | 96.9% | **93.6%** | 97.7% |

It is now after W43. The Quality Engineer knows **what** happened but not **why**. The recovery is one more clue, not proof that a fix worked. The question for the demo:

> Why did fewer products pass their first inspection in W42 on Contoso Plant A Line 1 (Power Module), and what should we verify before choosing corrective action?

| | |
|---|---|
| **Goal** | Narrow down the possible causes and choose the next checks. |
| **You run** | One Python command. |
| **You get** | One report with ranked hypotheses, the evidence for each, what is still missing, and recommended checks. |

## Pain points and benefits

| Pain point | What the demo shows |
|---|---|
| Weekly totals show the drop but not the reason. | Shift records compared by oven temperature, soldering-paste batch, and operator. |
| Several things changed at once, so every cause looks possible. | Evidence for and against each explanation, side by side. |
| A similar past incident can bias the team. | Past cases used as a guide, not as proof. |

## How the demo works

You run one command. Three roles then work one after another, each passing its findings to the next:

| Role (name shown in the output) | What it does |
|---|---|
| **Data analyst** (`DataAnalysisAgent`) | Calculates pass rates by week and compares oven temperature, soldering-paste batch, and operator assignments. |
| **Past-case reviewer** (`KnowledgeAgent`) | Reads two past investigations, one about oven heating and one about a connector alignment problem, and compares them with today's problem. |
| **Report writer** (`ReportAgent`) | Combines the evidence, ranks the possible causes, and proposes checks. |

Python tools do the calculations, so the numbers are computed rather than guessed. Microsoft Agent Framework passes work from one role to the next, and one Microsoft Foundry model deployment powers all three roles. The demo creates no agents or deployments in Foundry; it only calls an existing model.

## Key Takeaway & Talking point

- **From detection to investigation:** The Copilot scenario shows what happened. This demo asks the next question: why did it happen?
- **Tools calculate, agents explain:** Pass rates and comparisons come from Python code. The model turns them into a readable report.
- **Hypotheses, not verdicts:** The report ranks possible causes and lists missing evidence. The Quality Engineer makes the final call.

## Start the demo

> **Next: open [setup.md](setup.md#before-you-start) and follow it from top to bottom.** Check the prerequisites, then do steps 1 to 6, from Azure sign-in to reading the report. You finish there; you do not need to come back here.

You need Python, Azure CLI, and a Foundry project with a model deployment. **Model requests incur charges.**

## Data and related material

All records are fictitious. The demo reuses the weekly data from the Copilot scenario [Manufacturing Operations Performance & Risk](<../../Copilot/Manufacturing Operations Performance & Risk/README.md>), so the story continues at the same Contoso plant. It adds the shift records and past investigation reports that the deeper question needs. It runs on its own and does not need that scenario's output.

| File | What it holds |
|---|---|
| [operations_data.csv](data/operations_data.csv) | Reused weekly operating data (`Operations_Data`) |
| [quality_supplier_risk.csv](data/quality_supplier_risk.csv) | Reused weekly quality and supplier data (`Quality_and_Supplier_Risk`) |
| [process_parameters.csv](data/process_parameters.csv) | New shift records: oven temperature, paste batch, operator, and inspection counts |
| [Oven heating investigation](knowledge/rca_2025_reflow_profile_drift.md) | New past case about oven heating |
| [Connector alignment investigation](knowledge/rca_2024_connector_misalignment.md) | New past case with a different cause |

[DATA_DICTIONARY.md](DATA_DICTIONARY.md) has the field definitions, a [glossary](DATA_DICTIONARY.md#plain-language-glossary), and the [checks run on the data](DATA_DICTIONARY.md#validation-results). Tool results are sent to the Foundry model, so the data does not stay on your computer.

[Optional extensions](source/advanced/README.md) lists ideas that are not part of this demo: Magentic, VisionAgent, and Foundry Evals.

## Appendix: Microsoft Learn alignment

**Course:** [AI-3026-A: Develop AI agents on Azure](https://learn.microsoft.com/en-us/training/courses/ai-3026).

| Learn module | Applied in this demo |
|---|---|
| [Develop an AI agent with Microsoft Agent Framework](https://learn.microsoft.com/en-us/training/modules/develop-ai-agent-with-semantic-kernel/) | Connect to Foundry and expose local analysis and document-reading functions as agent tools |
| [Orchestrate a multi-agent solution using the Microsoft Agent Framework](https://learn.microsoft.com/en-us/training/modules/orchestrate-semantic-kernel-multi-agent-solution/) | Apply [sequential orchestration](https://learn.microsoft.com/en-us/training/modules/orchestrate-semantic-kernel-multi-agent-solution/5-use-sequential-orchestration): analysis, precedent comparison, then reporting with shared evidence |

This is an industry extension of those objectives, not a replacement for the official labs. The agents run locally against an existing model deployment.
