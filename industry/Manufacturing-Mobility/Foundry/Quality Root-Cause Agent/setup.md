# Quality Root-Cause Agent: Setup

Follow this guide from top to bottom in one Windows PowerShell terminal. By the end you will have run the investigation and read its report. You copy one command block at a time; signing in, entering your project details, and reading the report need your input.

## Before you start

### What you need

- **Tools:** Python 3.11 or later (tested with 3.14), Azure CLI, and VS Code with this repository cloned or downloaded. Open a PowerShell terminal in the repository root, the `asia-learning-hub` folder, and use it for every step.
- **A Foundry project and a model deployment** that support tool calling through the Responses API. The demo uses an existing project and does not create one. If you have none, create them once with [Set up Microsoft Foundry resources](https://learn.microsoft.com/en-us/azure/foundry/tutorials/quickstart-create-foundry-resources); see also [Create a project](https://learn.microsoft.com/en-us/azure/foundry/how-to/create-projects) and [Deploy models](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/create-model-deployments).
- **Access**, assigned by the project owner:
  - To run the demo: **Foundry User** on the Foundry project (some pages still call it Azure AI User).
  - To browse the parent Foundry resource in the portal: **Reader**. Reader alone does not allow running the demo.
  - To review billed costs: **Cost Management Reader** at the right scope, or ask the owner to do the review.
- **Approval to incur model charges.**

Creating projects, deployments, and role assignments are administrator tasks. If you get an access error, do not ask for broader access; see [Troubleshooting](#troubleshooting). Role details: [Foundry RBAC](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry) and [SDK prerequisites](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview#prerequisites).

### Time and cost

- **Runtime:** One test run took about 90 seconds after setup. Setup time and runtime vary with your environment and model.
- **Charges:** Each run sends several requests to the model, and they incur charges. Get the project owner's approval before you run it.
- **Cost:** It depends on the model you use. The actual cost of this demo was not measured.
- **Pricing:** See [Foundry Models pricing](https://azure.microsoft.com/en-us/pricing/details/ai-foundry-models/aoai/) or the model provider's pricing page, and [Foundry cost management](https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs).

## Step-by-step setup

### 1. Sign in to Azure

**Why:** The demo uses your Azure sign-in to call the model, so no API key is needed.

```powershell
az login
```

When sign-in finishes, confirm the account:

```powershell
az account show --query "{Subscription:name,Tenant:tenantId}" --output table
```

**Check:** The subscription and tenant are the ones that own the Foundry project. If you are unsure, ask the project owner. Never copy tokens or credentials into the repository.

### 2. Collect your project details

**Why:** The demo needs to know which model to call. You enter these two values in step 4.

In the [Foundry portal](https://ai.azure.com), open your project and note:

- **Project endpoint:** The full HTTPS address of the project, not the portal page URL. It looks like `https://<resource-name>.services.ai.azure.com/api/projects/<project-name>`.
- **Model deployment name:** The name of the deployment, which may differ from the model's catalog name.

If you cannot find them, see [Get your project connection details](https://learn.microsoft.com/en-us/azure/foundry/tutorials/quickstart-create-foundry-resources#get-your-project-connection-details).

**Check:** You have both values, and the owner has confirmed that the deployment supports tool calling and has quota for the demo.

### 3. Install the Python packages

**Why:** The demo's Python tools read the factory records and run the three roles. A virtual environment keeps its packages separate from your other projects.

From the repository root, go to the demo's `source` folder and create the virtual environment:

```powershell
Set-Location -LiteralPath '.\industry\Manufacturing-Mobility\Foundry\Quality Root-Cause Agent\source' -ErrorAction Stop
if (Test-Path -LiteralPath .\main.py) { python --version; python -m venv .venv }
```

The version printed should be 3.11 or later. Then install the packages. The dependency check runs only if the installation succeeds:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
if ($LASTEXITCODE -eq 0) { .\.venv\Scripts\python.exe -m pip check }
```

**Check:** The last line says **No broken requirements found.** Stay in this `source` folder for steps 4 and 5. You do not need to activate the environment or change any execution policy. If installation fails, see [Troubleshooting](#troubleshooting).

### 4. Enter your project details

**Why:** The demo reads the project endpoint and model name from a local settings file named `.env`. Git ignores this file, so your values stay on your machine.

Create `.env` if it does not exist yet, then open it:

```powershell
if (-not (Test-Path -LiteralPath .env)) {
    Copy-Item -LiteralPath .env.example -Destination .env -ErrorAction Stop
}
notepad.exe .env
```

In Notepad, replace every `<...>` placeholder with your values from step 2, then save and close the file. The two settings look like this:

```dotenv
FOUNDRY_PROJECT_ENDPOINT=https://<resource-name>.services.ai.azure.com/api/projects/<project-name>
FOUNDRY_MODEL=<model-deployment-name>
```

**Check:** No `<...>` is left in the file, and it contains no API key. Variables already set in your terminal take priority over `.env`, so remove any that conflict.

### 5. Run the investigation

**Why:** This is the investigation itself. The program calculates the comparisons, reads the two past reports, and asks the model to write the report.

The program asks the model one fixed question, so you do not type or paste anything:

```text
Why did fewer products pass their first inspection in W42 on Contoso Plant A Line 1 (Power Module), and what should we verify before choosing corrective action?
```

This command **sends billable requests to the model** and takes about 90 seconds:

```powershell
.\.venv\Scripts\python.exe main.py
```

**Check:** The program prints this line and, after a short wait, one report:

```text
Local inputs checked. Running DataAnalysisAgent -> KnowledgeAgent -> ReportAgent...
```

The three roles run one after another without any input from you. When the report appears, go on to step 6 instead of running the command again.

### 6. Read the report

**Why:** The report is only useful if you can explain what the evidence supports, what is still unknown, and what to check next.

Two names appear in the evidence. **SP-002** is a new batch of soldering paste used from W42. **OP-04** is a new operator who first worked in W42. A **high-defect shift** is a shift with a first-inspection pass rate below 95%.

First, confirm the weekly pass rates in the report: W40 97.5%, W41 96.9%, W42 93.6%, and W43 97.7%. Then look for findings like these. The wording and ranking change from run to run; this table is an illustration based on one test run, not a transcript.

| What the report finds | What it means | What to check next |
|---|---|---|
| Hotter shifts had lower pass rates, and W43 recovered when temperatures came back down. | Oven heating is the leading lead to investigate, not a proven cause. | Verify the sensors and the product's full temperature-over-time curve. |
| SP-002 stayed in use during the W43 recovery. | The paste batch alone does not explain the drop, but it may interact with the heating conditions. | Review the batch's test results and compare batches under matched conditions. |
| OP-04 did not work any high-defect W42 shift. | Little supports blaming the new operator. This does not rule out every operator effect. | Review training and assignments, comparing similar operating conditions. |
| The 2025 oven case fits; the 2024 connector case has a different cause. | A past case can guide the checks but cannot prove today's cause. | Collect current defect and process evidence. |

A complete report has five sections: **Summary**, **Ranked hypotheses**, **Evidence gaps**, **Next checks**, and **Decision boundary**. Its claims cite files, fields, or past-report sections. Spot-check a few against the [weekly quality data](data/quality_supplier_risk.csv) (`First Pass Yield Actual`), the [shift records](data/process_parameters.csv), and the past cases from [2025](knowledge/rca_2025_reflow_profile_drift.md) and [2024](knowledge/rca_2024_connector_misalignment.md).

#### What the demo shows

- **Shows:** Calculations and past cases combine into an evidence-backed starting point for a quality investigation, with three roles passing the work along. A Quality Engineer gets possible causes and next checks in one place.
- **Does not show:** A confirmed root cause. The comparisons are observations, not controlled experiments, and defect types, sensor calibration, full heating curves, and controlled batch trials are missing. Confidence labels in the report are qualitative, not probabilities. The demo does not measure time saved or predict better pass rates.

#### You are done when

You can explain the leading hypothesis, the evidence that limits it, and the next check. In a real plant, the Quality Engineer then chooses the validation plan. The demo never changes equipment, rejects a batch, or blames an operator. **These are hypotheses; the Quality Engineer makes the final judgment.**

#### Tester checklist

If you are the peer verifying this demo, follow the guide without help and fill in the table. Record preparation time (steps 1-4) and run time (step 5) separately in the notes; there is no pass/fail time target.

| # | Check | Pass/Fail | Notes |
|---|---|---|---|
| 1 | **Before you start** was clear, and you had a Foundry project, a model deployment, and the access you need. | | |
| 2 | Steps 1-4 worked without help: signed in, packages installed (`No broken requirements found.`), and `.env` saved. | | |
| 3 | Step 5 printed the `Local inputs checked` line and then one report. | | |
| 4 | The report has all five sections. | | |
| 5 | The weekly pass rates match: 97.5%, 96.9%, 93.6%, 97.7%. | | |
| 6 | The report links the temperature rise to the W42 drop and notes that SP-002 stayed in use during the W43 recovery. | | |
| 7 | The report does not blame OP-04 and does not call any cause confirmed. | | |
| 8 | A few citations (files, fields, report sections) match the supplied data. | | |
| 9 | You can explain the leading hypothesis, its limit, and the next check in your own words. | | |
| 10 | Preparation time and run time are written in the notes, in minutes. | | |

---

The sections below are reference material, not additional steps.

## Troubleshooting

### Sign-in or permission errors

Check that the tenant shown in step 1 owns the project, and that the project owner has assigned you **Foundry User** on it. Variables set in your terminal override `.env`, so remove any that conflict. A role for using a published agent endpoint is not the same as project access for this demo.

### Package installation errors

Run this from the `source` folder:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
if ($LASTEXITCODE -eq 0) { .\.venv\Scripts\python.exe -m pip check }
```

The packages are pinned to tested versions, and `azure-ai-inference`, a dependency of the Foundry integration, is a preview release. If your package mirror cannot find a pinned version, check that it exists on public PyPI and use an organization-approved index instead of changing versions.

### Quota, region, or model errors

Use your project's own region; the demo does not choose one. For throttling or quota errors, wait or ask the owner to raise the deployment's capacity. Make sure `FOUNDRY_MODEL` matches a deployment that supports tool calling through the Responses API. Each run is billable, so find the cause before you rerun.

### Garbled punctuation

The program writes UTF-8. If redirected output looks garbled, open it as UTF-8. A failure after the model has answered can still be billed, so find the cause before you rerun.

### Data errors

Use the supplied files unchanged. See [DATA_DICTIONARY.md](DATA_DICTIONARY.md).

## Cleanup

The demo creates no resources in Foundry, so there is nothing to delete. Keep shared projects and deployments, and remove only resources you created just for testing. Your service settings control how long responses are retained.

## SDK references

- [Microsoft Agent Framework documentation](https://learn.microsoft.com/agent-framework/)
- [Pinned Foundry integration](https://pypi.org/project/agent-framework-foundry/1.16.1/)
- [Pinned orchestration package](https://pypi.org/project/agent-framework-orchestrations/1.4.2/)
