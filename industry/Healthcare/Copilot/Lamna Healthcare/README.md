# Reducing Readmissions Through Better Care Transitions
Lamna Hospital (a fictional hospital) is seeing 30-day readmissions rise on its Cardiology, Pulmonology and Geriatrics wards, particularly for Heart Failure and COPD patients.

The Care Transitions Operations Manager has been asked to prepare a seven-day intervention decision package for the Executive Quality Committee.

Making a responsible decision requires bringing together:
- Readmission and post-discharge contact patterns
- Bed capacity, patient flow and service events
- Patient-level discharge data
- Approved programs, cost thresholds, consent and vulnerable-patient rules
- Input from Pharmacy, Finance, Data Governance and clinical leads

The manager uses Microsoft Copilot as a connected workflow across Chat, Excel, Word, PowerPoint, Outlook and Teams.

> **Important:** All files in this demo contain **synthetic data**. No real patients, staff or facilities are represented. Copilot supports drafting and analysis; it does **not** make clinical decisions.

## Demo files
All files are in the [`data-files`](data-files/) folder:
- **Word (Chat, Word):** `Readmission_Quality_Summary.docx`, `Bed_Capacity_and_Patient_Flow_Report.docx`, `Care_Transitions_Eligibility_Policy.docx`, `Related_Emails_Care_Transitions.docx`
- **Excel:** `Lamna_Care_Transitions_Cohort_Demo.xlsx` (Patient Cohort, Programs, Ward Monthly, Risk Metrics)
- **Teams fallbacks:** `Teams_Huddle_Transcript.docx`, `Teams_Channel_Thread.docx`
- **Trainer only:** `Trainer_Notes_Data_Issues.md` lists the seeded data issues by row. Keep it from learners until after the exercise.

## Demo journey: pain points and how Copilot helps
| **Stage** | **Pain point** | **How Copilot helps** | **Business benefit** |
|-----------|----------------|-----------------------|----------------------|
| 1. Understand (Chat) | Evidence is scattered across reports, policies and emails | Builds a grounded, cited situation summary | Less manual searching and consolidation |
| 2. Analyze (Excel) | Discharge data is inconsistent, and it is hard to target the right patients within consent rules | Finds data issues, then builds a governed intervention cohort with exception lists | More reliable, better-targeted outreach |
| 3. Recommend (Word) | Analysis must become an auditable proposal | Drafts the intervention brief and executive summary | Faster, consistent decision documents |
| 4. Communicate (PowerPoint) | Executives need the story, not the detail | Turns the brief into an executive deck | Clearer alignment and decisions |
| 5. Coordinate (Outlook) | Approvals sit with five different teams | Drafts a targeted approval request | Faster coordination without rewriting context |
| 6. Align (Teams) | Decisions and actions get lost in meetings and channels | Recaps meetings, lists owners and actions, catches up on threads | Fewer missed actions, clearer accountability |

## Stage 1 - Understand the situation in Copilot Chat
- **Situation summary:** Attach the four Word files and run:
>Using the attached readmission quality summary, capacity and flow report, care transitions policy and emails, prepare a situation summary for a Care Transitions Operations Manager. Identify the main drivers of repeat post-discharge contact, the patient groups affected, relevant service events, existing support programs, and unresolved questions with likely owners. Separate confirmed facts, assumptions and missing evidence, and cite the source files.

- **Action plan**
>Turn this summary into an action plan for a seven-day care-transitions decision package, organized into data to validate, analysis required, policy and consent checks, stakeholder decisions, and final deliverables.

- **Governance check**
>Review this action plan against the care transitions policy. Identify steps that need human approval, consent verification, vulnerable-patient handling, or confirmation from Pharmacy, Finance or Data Governance.

## Stage 2 - Clean and analyze the discharge cohort in Excel
Open **Lamna_Care_Transitions_Cohort_Demo.xlsx** (sheet **Patient Cohort**).

### Use case 1: Detect data issues
>Inspect this table for data quality issues: inconsistent labels, missing values, duplicate Patient_ID, text stored as numbers or dates, and implausible values. Create a review table showing the row, column, issue and recommended handling. Do not change the source data yet.

### Use case 2: Build the intervention cohort
Run the following prompt in **Edit** mode:
>Propose a care-transitions intervention cohort in a new worksheet named "Care Transitions Cohort". Include only patients with two or more post-discharge contacts, a Transition_Status of Gap, an active eligible program, Consent_To_Contact = Yes, not flagged vulnerable, and not discharged to a skilled nursing facility. Create separate exception lists for programs costing more than $250 per patient and for vulnerable patients with two or more contacts. Add a summary of the selection criteria.

>Highlight patients with a readmission risk score of 75 or higher in light red, and create a clustered column chart showing the number of Low, Medium and High risk patients.

## Stage 3 - Create the intervention brief in Word
- **Create draft:** Attach the policy, quality summary, capacity report and the Excel file:
>Using the attached documents and the "Care Transitions Cohort" worksheet, draft a two-page intervention brief for the Director of Care Transitions with these sections: Decision requested, Patient and operational problem, Evidence, Proposed seven-day cohort, Eligible programs, Exclusions and exception handling, Human approvals and governance controls, Measurement plan, Open decisions and owners. Clearly distinguish confirmed facts, analytical indicators and recommendations.

Save the file as "**Lamna Care Transitions Intervention Brief.docx**".

- **Refine and summarize**
>Review this brief for senior-management readability: put the decision in the opening paragraph, reduce technical detail, move assumptions to an appendix, and keep all approval, consent, vulnerable-patient and audit controls. Then write an executive summary of no more than 150 words.

## Stage 4 - Convert the brief into an executive presentation
- **Create draft:** Open an existing presentation with the right template and attach the brief:
>Create a seven-slide executive presentation from the attached brief with a patient journey visual and KPI cards: Decision required, Readmission problem and impact, Patient journey from discharge to readmission, Evidence from the cohort, Seven-day intervention workflow, Governance and approvals, Measures of success and next steps. Use the styles of the current presentation.

- **Review and refine**
>Review this deck as the Director of Care Transitions. Identify slides with too much detail, claims not supported by the brief, missing decisions, and governance controls that should be more visible.

## Stage 5 - Coordinate approvals in Outlook
- **Create draft:** Attach the brief:
>Draft an email to Care Transitions, Pharmacy, Data Governance, Compliance and Finance summarizing the attached brief and requesting approval. Ask each team to confirm: Care Transitions - scope and ownership; Pharmacy - reconciliation visit capacity including weekend cover; Data Governance - consent, vulnerable-patient and data-handling controls; Compliance - patient communication conditions; Finance - approval thresholds and estimated cost range.

- **Review and refine**
>Rewrite the email in under 180 words. Keep each team's requested decision explicit and easy to scan, in a professional, neutral tone.

## Stage 6 - Align and follow through in Teams
Run a short live huddle (read the transcript aloud with Copilot recording enabled), or use `Teams_Huddle_Transcript.docx` and `Teams_Channel_Thread.docx` as fallbacks.

- **Meeting recap**
>Summarize this meeting in five bullets. List the decisions made, concerns recorded, and every action item with owner and due date, flagging any action with no owner or date.

>Where did attendees disagree, and how was it resolved? What has Pharmacy committed to, and what is still conditional?

- **Channel catch-up**
>Catch me up on the Care Transitions channel since Monday. What changed, and what is blocking progress?

## Final demo outcome
By the end of the story, the manager has produced:
- A grounded situation summary
- A cleaned discharge dataset and a governed intervention cohort
- A decision-ready Word brief and a seven-slide executive presentation
- A targeted multi-team approval request
- A clear record of decisions, owners and actions from the huddle

> Copilot output varies between runs, so review each result. Feature availability (such as Edit mode) depends on your Microsoft 365 Copilot license and tenant settings.
