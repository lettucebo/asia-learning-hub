# LaunchPad Digital Experience: From Signup to First Value

LaunchPad is a fictional digital-native software-as-a-service (SaaS) company that provides self-service digital workspaces to startups, small and medium businesses, education providers and enterprise customers. A customer signs up, verifies their identity, receives a provisioned workspace, creates a first project and completes a first-value activity.

Following the deployment of release **REL-2410 on 20 October 2026**, successful customer activation has deteriorated. Signup volume remains comparatively stable, but workspace provisioning and first-project creation show higher error rates, longer completion times and increased abandonment. Customer Success and Support are reporting more cases involving workspaces stuck in provisioning and failed first-project creation. Some enterprise accounts may be exposed to contractual service commitments, while trial customers may abandon before converting to paid subscriptions.

The release changed parts of the unified provisioning API and asynchronous job orchestration. The timing makes REL-2410 a reasonable investigation lead, but the supplied evidence does **not** establish it as the confirmed root cause. Per-tenant traces are missing for a portion of requests and there is no controlled rollback comparison. The team must avoid turning correlation into causation.

The Head of Digital Service Operations must prepare for a **15:00 cross-functional review**. With Microsoft 365 Copilot, the manager will synthesize fragmented evidence in Copilot Chat, investigate the customer journey and business impact in Excel, prepare a decision brief in Word, create an executive review deck in PowerPoint and coordinate owners and deadlines in Outlook.

## Pain points and demonstrated benefits

| **Pain point** | **How Copilot helps** | **Business benefits** |
| --- | --- | --- |
| Customer journey evidence is fragmented across analytics exports, support cases, release notes and operating guidance. | Copilot Chat synthesizes product, customer, engineering and policy context with source grounding. | Faster situational awareness and less manual searching. |
| Teams debate severity using different funnel and customer metrics. | Copilot in Excel explores conversion, success, error, latency and abandonment trends and relates them to customer segments and estimated ARR. | Shared evidence base and clearer prioritization of journey steps and customers. |
| A release that precedes deterioration may be incorrectly declared the root cause. | Copilot in Word structures confirmed facts, hypotheses, missing telemetry, risks and approval needs separately. | Better decision quality and reduced communication risk. |
| Leadership needs a concise business narrative, not raw event telemetry. | Copilot in PowerPoint turns the decision brief into a decision-oriented executive story. | Shorter preparation time and clearer decisions. |
| Recovery actions can be vague or lack owners and safeguards. | Copilot in Outlook drafts a structured coordination message from the final brief and decisions. | Clear accountability, deadlines, dependencies and faster execution. |

## Demo files

Download and extract **LaunchPad_Digital_Experience_Copilot_Demo_Files.zip**. Use the exact filenames below; the names are case-sensitive in some environments.

### Package structure and exact filenames

```text
LaunchPad_Digital_Experience_Copilot_Demo_Files/
│
├── README.md
│
├── data/
│   ├── LaunchPad_Digital_Service_Operations_Analytics.xlsx
│   ├── daily_product_journey_metrics.csv
│   ├── customer_segment_impact.csv
│   ├── customer_support_cases.csv
│   ├── release_monitoring.csv
│   ├── release_record_REL-2410.json
│   ├── DATA_DICTIONARY.md
│   ├── known_data_quality_issues.csv
│   └── facilitator_validation.md
│
├── source_documents/
│   ├── Product_Operations_Incident_Update.docx
│   ├── Platform_Engineering_Release_Review.docx
│   ├── Customer_Success_Impact_Review.docx
│   └── Digital_Service_Assurance_Playbook.docx
│
└── templates/
    ├── Digital_Service_Incident_Decision_Brief_Template.docx
    └── Digital_Service_Executive_Review_Template.pptx
```

### What each source file contains

| Exact filename | Folder | Use in the demo |
| --- | --- | --- |
| `Product_Operations_Incident_Update.docx` | `source_documents/` | Product incident overview, customer journey symptoms, timeline and known impact. Primary business-context source for Stage 1. |
| `Platform_Engineering_Release_Review.docx` | `source_documents/` | REL-2410 deployment details, technical observations, telemetry gaps, investigation hypotheses and rollback considerations. Do not treat it as proof of root cause. |
| `Customer_Success_Impact_Review.docx` | `source_documents/` | Customer-segment concerns, enterprise account exposure, trial abandonment signals and customer communication considerations. |
| `Digital_Service_Assurance_Playbook.docx` | `source_documents/` | Incident severity, evidence standards, escalation, rollback governance and approval responsibilities. |
| `release_record_REL-2410.json` | `data/` | Structured change record: release scope, deployment date, checks, known constraints and rollback approval requirements. |
| `daily_product_journey_metrics.csv` | `data/` | Daily funnel and performance measures by journey step. Use for baseline versus post-release analysis and charts. |
| `customer_segment_impact.csv` | `data/` | Segment- and plan-level trial, activation, at-risk account, estimated ARR and priority information. ARR is illustrative exposure, not booked revenue or confirmed loss. |
| `customer_support_cases.csv` | `data/` | Synthetic support-case records for category, severity, response/resolution and customer-pattern analysis. |
| `release_monitoring.csv` | `data/` | Release monitoring snapshots, including worker timeouts and asynchronous queue backlog. |
| `LaunchPad_Digital_Service_Operations_Analytics.xlsx` | `data/` | Main Excel lab workbook with dashboard, analysis tables and data-quality content. This is the file to open for Stage 2. |
| `DATA_DICTIONARY.md` | `data/` | Definitions, date windows, measures and priority thresholds. Attach for Stage 1; consult during Stage 2. |
| `known_data_quality_issues.csv` | `data/` | Facilitator-only index of intentionally seeded data-quality defects. Do not give to learners until they have attempted the data-quality exercise. |
| `facilitator_validation.md` | `data/` | Facilitator notes, scenario guardrails and validation facts. Keep with the instructor; do not attach in the learner's first Copilot Chat prompt. |
| `Digital_Service_Incident_Decision_Brief_Template.docx` | `templates/` | Word structure to use when drafting the decision brief in Stage 3. |
| `Digital_Service_Executive_Review_Template.pptx` | `templates/` | Existing five-slide presentation theme to use in Stage 4. |

## Demo journey

| **Stage** | **Copilot Experience** | **Story** |
| --- | --- | --- |
| 1. Understand | Copilot Chat | Bring fragmented product, customer, release and policy material together; identify what is confirmed, suspected and missing. |
| 2. Investigate | Copilot in Excel | Analyze activation-funnel deterioration, support patterns and customer exposure to identify the highest-priority journey steps and segments. |
| 3. Decide | Copilot in Word | Create a decision brief with evidence, hypotheses, options, safeguards, actions and approval gates. |
| 4. Communicate | Copilot in PowerPoint | Convert the decision brief into a leadership-ready digital service review. |
| 5. Coordinate | Copilot in Outlook | Draft the post-review action request using the brief and agreed decisions. |

## Stage 1 - Understand in Copilot Chat

### Exact files to attach

Attach these seven files to Copilot Chat (or add them to the relevant Microsoft 365 context if your tenant supports that workflow):

1. `source_documents/Product_Operations_Incident_Update.docx`
2. `source_documents/Platform_Engineering_Release_Review.docx`
3. `source_documents/Customer_Success_Impact_Review.docx`
4. `source_documents/Digital_Service_Assurance_Playbook.docx`
5. `data/release_record_REL-2410.json`
6. `data/DATA_DICTIONARY.md`
7. `data/LaunchPad_Digital_Service_Operations_Analytics.xlsx`

Do **not** attach `known_data_quality_issues.csv` or `facilitator_validation.md` in the first learner exercise. Those are facilitator aids and would reveal the seeded defects and scenario answers.

### Prompts

> Using the attached LaunchPad source files, prepare an incident situation summary for the Head of Digital Service Operations. Explain the customer journey from signup to first value. Identify which journey steps are affected, what customers experience, which segments may be exposed, the business implications, the incident timeline, the release context, the unresolved questions and the decision required at the 15:00 review. Cite the source filename for each material finding.

> Separate the findings into (1) confirmed facts directly supported by the files, (2) reasonable hypotheses requiring validation and (3) missing evidence. Explicitly flag any statement that could incorrectly imply REL-2410 is the confirmed root cause. Distinguish observed activation-funnel deterioration from inferred conversion impact and estimated ARR exposure.

> Create a review preparation checklist. Include product telemetry validation, customer and enterprise impact, release/rollback safety, customer communications, financial validation, legal or contractual review, approval requirements, accountable decision owner and evidence required for each topic. Do not invent named individuals where the source files provide only team ownership.

**Expected output:** A concise, source-grounded incident narrative, a fact/hypothesis/gap register and a review checklist.

## Stage 2 - Investigate in Excel

Open **`data/LaunchPad_Digital_Service_Operations_Analytics.xlsx`**. This is the primary workbook for the hands-on exercise. It contains the following sheets:

| Exact worksheet name | What to investigate |
| --- | --- |
| `Executive_Dashboard` | Overall customer journey and business snapshot. |
| `Daily_Journey_Metrics` | Daily attempts, success, errors, completion time and abandonment by journey step. |
| `Customer_Impact` | Segment and plan exposure, account counts, estimated ARR and priority. |
| `Support_Cases` | Support case trends, categories, severity and resolution measures. |
| `Release_Monitoring` | Release-period health indicators, timeouts and queue backlog. |
| `Known_Data_Issues` | Facilitator reference for seeded data defects; hide this sheet or do not show it to learners until the exercise is complete. |

The corresponding raw CSV files are also supplied in `data/` for users who want to import the source data independently:

- `daily_product_journey_metrics.csv`
- `customer_segment_impact.csv`
- `customer_support_cases.csv`
- `release_monitoring.csv`

### Detect and clean data issues

> Review the `Daily_Journey_Metrics`, `Customer_Impact`, `Support_Cases` and `Release_Monitoring` tables in the workbook. Identify data-quality issues such as inconsistent category values, wrong formats, out-of-range values, missing values, negative counts, duplicate records and text in numeric fields. Create a data-quality report with issue type, exact worksheet and row or field, business impact and suggested handling. Do not silently invent or impute source values. Preserve the original data and document any exclusions.

Facilitator note: after learners finish, compare their findings with `data/known_data_quality_issues.csv`. This file is an answer aid, not a learner source for the first attempt.

### Analyze the data

> Show the journey steps ordered by average post-release error rate in descending order. Compare the baseline period 12–19 October 2026 with the post-release period 20–25 October 2026. State the calculation and the number of valid observations used.

> Analyze the `Daily_Journey_Metrics` and `Customer_Impact` tables. Identify the three journey steps with the most significant deterioration. Explain the evidence using success rate, error rate, P95 completion time and abandonment. Distinguish absolute percentage-point change from relative percentage change.

> Assess whether daily support-case volume is more closely associated with provisioning errors, first-project errors or completion time. Explain the limitations of this small synthetic dataset. Do not claim causation from correlation.

> Identify customer segments and plans with the highest activation failures, at-risk accounts and estimated ARR exposure. Clearly label ARR as an estimate derived from sample data, not booked revenue, recognized revenue or confirmed loss. Avoid double-counting segment and plan totals.

### Other analysis and data visualization

> Create a Customer Priority PivotTable grouped by Customer Segment, Plan and Recommended Priority. Include Trial Accounts, Activated Accounts, Activation Failures, At-Risk Accounts, Estimated Annual Recurring Revenue and Priority Score. Explain the aggregation method used for each value.

> Create a `Recommended Priority` column with values Critical, High, Medium or Low when Priority Score is: >= 75, >= 55, >= 35 or else. Use a formula and fill it down for all applicable records.

> Format customer segment and plan rows marked Critical with dark red fill and bold white text. Apply conditional formatting so that the priority is visually obvious without changing the underlying values.

> Create three line charts showing daily average Success Rate, Error Rate and P95 Completion Time by Journey Step. Mark 20 October 2026, the REL-2410 deployment date, with a vertical reference line. If Copilot cannot add a true vertical line, add a clearly labeled release marker series and explain the method. Do not imply the release date proves causation.

> Create a heatmap comparing baseline-to-post-release change in Success Rate, Error Rate and P95 Completion Time for each Journey Step. Define baseline as 12–19 October and post-release as 20–25 October. Exclude malformed values and disclose the exclusions and denominator used.

**Expected output:** A documented data-quality report, prioritized customer/journey analysis, PivotTable, three trend charts and a baseline-versus-post-release heatmap.

## Stage 3 - Decide in Word

### Exact files to use

Attach the following source files and the completed Excel workbook:

1. `source_documents/Product_Operations_Incident_Update.docx`
2. `source_documents/Platform_Engineering_Release_Review.docx`
3. `source_documents/Customer_Success_Impact_Review.docx`
4. `source_documents/Digital_Service_Assurance_Playbook.docx`
5. `data/release_record_REL-2410.json`
6. `data/LaunchPad_Digital_Service_Operations_Analytics.xlsx` (the learner's analyzed and saved copy)
7. `templates/Digital_Service_Incident_Decision_Brief_Template.docx`

### Create the draft

Open **`templates/Digital_Service_Incident_Decision_Brief_Template.docx`** in Word and use Copilot:

> Based on the attached LaunchPad source material and completed Excel analysis, draft a digital service incident decision brief using the structure and headings in `Digital_Service_Incident_Decision_Brief_Template.docx`. Include an executive summary, customer journey and scope, business and customer impact, evidence and timeline, confirmed facts, hypotheses, missing telemetry, options and trade-offs, recommendation, safeguards, approval gates and an action register. Cite the source filename for key evidence. Do not present REL-2410 as the confirmed root cause. Distinguish estimated ARR exposure from actual revenue loss. Do not invent owners, commitments or approvals.

Save the completed document as **`LaunchPad Customer Activation Decision Brief.docx`**.

### Refine

> Rewrite the executive summary for a senior digital leadership audience in no more than six bullets. Lead with customer and business impact, preserve uncertainty about root cause, distinguish measured results from estimates, and state the decision required today.

> Review the brief for unsupported claims, contradictory figures, missing evidence, unclear owners and actions without deadlines. Produce a short list of corrections before this brief is circulated to leadership.

**Expected output:** `LaunchPad Customer Activation Decision Brief.docx`, with facts, hypotheses, decisions, safeguards and accountable actions clearly separated.

## Stage 4 - Communicate in PowerPoint

### Exact files to use

- Open `templates/Digital_Service_Executive_Review_Template.pptx` as the existing presentation/template.
- Attach `LaunchPad Customer Activation Decision Brief.docx` created in Stage 3.
- If needed for source verification, also attach `data/LaunchPad_Digital_Service_Operations_Analytics.xlsx` (the analyzed copy).

### Create the draft

> Create a five-slide executive presentation from the attached `LaunchPad Customer Activation Decision Brief.docx`, using the existing slide format and styles in `Digital_Service_Executive_Review_Template.pptx`: 1) situation and customer journey scope, 2) customer and business impact, 3) evidence and release timeline, 4) recommended actions and safeguards, and 5) decisions required today. Use concise takeaway titles, not generic section headings. Include only decision-relevant metrics. Do not present REL-2410 as the confirmed root cause. Clearly separate observed metrics from estimated financial exposure. Preserve the template's visual style.

### Review and refine

> Review this deck as if you were the Chief Digital Officer. Identify what is unclear, too detailed, unsupported or missing. Recommend changes that strengthen customer impact, funnel evidence, financial assumptions, risks, trade-offs, recommendation and the decision required. Provide slide-by-slide suggestions and propose a stronger executive storyline. Check that no slide implies that REL-2410 is a proven root cause or that estimated ARR exposure is realized loss.

**Expected output:** A concise five-slide executive review presentation aligned to the Word decision brief.

## Stage 5 - Coordinate in Outlook

### Exact file to use

Attach **`LaunchPad Customer Activation Decision Brief.docx`** created in Stage 3. Optionally attach the executive presentation from Stage 4 if the recipients need the same leadership narrative.

### Create the draft

> Draft an action-request email for Platform Engineering, Product Management, Customer Success, Finance and Legal using the attached `LaunchPad Customer Activation Decision Brief.docx`. Summarize the customer activation degradation and its business implications. Ask each team to confirm its accountable owner, action, dependency, evidence required and completion time. State clearly that REL-2410 remains under investigation and is not a confirmed root cause. Do not promise customer credits, refunds or SLA remedies without Finance and Legal approval. Leave recipient addresses as placeholders if they are not supplied.

### Review and refine

> Make the email concise and action-oriented. Add a table with Team, Requested Action, Accountable Owner, Deadline, Dependency and Approval or Evidence Required. Include a request to escalate blockers before the controlled rollback decision window. Distinguish immediate containment from longer-term corrective action. Do not invent actual meeting decisions or claim that a rollback has been approved.

**Expected output:** A ready-to-review Outlook draft with clear team-level accountability, deadlines and approval dependencies.

## Final demo outcome

By the end of the story, the Head of Digital Service Operations has produced:

- A grounded situation summary assembled from product, customer, engineering and operating sources.
- A prioritized, data-supported view of customer journey steps, customer segments and subscription plans requiring attention.
- An Excel analysis of activation, abandonment, service performance, support trends and estimated customer exposure, including documented data-quality handling.
- A decision brief that separates fact, hypothesis, risk, estimated financial exposure and approval requirements.
- A leadership-ready presentation focused on customer outcomes, business implications and decisions.
- A ready-to-review Outlook coordination message with clear owners, dependencies, deadlines and approval requirements.

## Facilitator delivery notes

**Suggested duration:** 60–75 minutes (approximately 10 minutes Chat, 20 minutes Excel, 15 minutes Word, 10 minutes PowerPoint and 10 minutes Outlook, plus discussion).

**Suggested audience:** Digital Service Operations, Product Operations, SaaS Customer Success, Platform Engineering, Digital Transformation and business leadership teams.

**Suggested setup:** Microsoft 365 Copilot access in the relevant apps; Excel desktop or web with workbook editing; Word and PowerPoint; Outlook. Availability of Copilot features can vary by tenant, license, app version and organizational configuration. The learner should save a working copy of the workbook before editing.

**Facilitator preparation:** Extract the ZIP; verify the workbook opens; keep `known_data_quality_issues.csv` and `facilitator_validation.md` for instructor use; distribute the four `source_documents` files and data files to learners; and ensure the Word and PowerPoint templates are available. Use synthetic records only.

**Scenario guardrails:**

- LaunchPad, its customers, metrics, release REL-2410, support cases and financial figures are entirely synthetic.
- The date 20 October 2026 is the scenario's release date; it is not proof of causation.
- Per-tenant traces are missing for some requests and no controlled rollback comparison is supplied.
- Estimated ARR exposure is illustrative and must not be described as booked revenue, realized loss or approved customer compensation.
- Do not invent customer names, named decision-makers, legal conclusions, SLA breaches or approvals.
- Copilot-generated analysis and drafts must be checked against the supplied source data before being used as a decision record.

