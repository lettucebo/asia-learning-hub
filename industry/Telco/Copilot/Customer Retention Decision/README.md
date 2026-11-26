# From Customer Complaints to a Retention Decision: A Telco Care Manager’s Copilot Journey

AsterWave Mobile is seeing repeated customer complaints, particularly around slow data, dropped calls, and intermittent coverage.

The Customer Care Operations Manager has been asked to prepare a retention decision package for leadership.

The challenge is that making a responsible decision requires bringing together several different types of information:
- Customer complaint patterns
- Network service-quality and incident information
- Customer-level data
- Retention eligibility and approved offers
- Consent and vulnerable-customer considerations
- Outage communication rules

The manager uses Microsoft Copilot as a connected workflow across Chat, Excel, Word, PowerPoint, and Outlook.

## Paint points and demonstrated benefits
| **Pain point** | **How Copilot helps** | **Business benefits** |
|----------------|-----------------------|-----------------------|
| Evidence is scattered across emails, reports, files, and spreadsheets | Copilot Chat creates a grounded situation summary | Less manual searching and consolidation |
| Customer data contains inconsistent or incomplete values | Copilot in Excel detects and helps correct data-quality issues | More reliable segmentation and fewer misleading results |
| Care teams struggle to connect repeat contacts with network experience | Copilot in Excel analyzes contacts, service degradation, tenure, plan, and risk indicators | Better-targeted intervention population |
| Analysis must be converted into an auditable proposal | Copilot in Word drafts a structured intervention brief using the analysis and policy | Faster production of consistent decision documents |
| Technical and business stakeholders need different levels of detail | Copilot in PowerPoint converts the brief into an executive narrative | Clearer stakeholder alignment and decision-making |
| Approvals are spread across multiple teams | Copilot in Outlook drafts targeted approval requests | Faster coordination without repeatedly rewriting context |

## Demo files
[Telco_Customer_Retention_Demo_Files.zip](https://github.com/CSDSkilling/asia-learning-hub/raw/refs/heads/main/industry/Telco/Copilot/Customer%20Retention%20Decision/data-files/Telco_Customer_Retention_Demo_Files.zip)

## Demo journey
| **Stage** | **Copilot Experience** | **Story** |
|-----------|------------------------|-----------|
| 1. Understand | Copilot Chat | Bring together complaint, network, policy, and communication documents to understand what is happening and what needs to be decided. |
| 2. Validate & analyze | Copilot in Excel | Discover data-quality problems, clean the customer data, then determine which customers warrant further review based on repeat contacts, network experience, consent, eligibility, and exceptions. |
| 3. Recommend | Copilot in Word | Turn the evidence and Excel analysis into a structured retention intervention brief, including recommendations, exclusions, controls, and approvals. |
| 4. Communicate | Copilot in PowerPoint | Transform the detailed brief and analysis into an executive decision story showing the problem, evidence, proposed intervention, controls, and measures of success. |
| 5. Coordinate | Copilot in Outlook | Draft a concise approval request to Care, Network Operations, Data Governance, Legal, and Finance, making the decision required from each stakeholder explicit. |

## Stage 1 - Understand the situation in Copilot Chat
- **Situation summary:** Attach all Word files and run the following prompt:
>Using the Meranti Coast complaint summary, service-quality report, retention policy, and related emails, prepare a situation summary for a Customer Care Operations Manager.
>
>Identify:
>1. The three main drivers of repeat contact
>2. The customer groups that may be affected
>3. Relevant network incidents or service-quality evidence
>4. Existing retention or remediation options
>5. Unresolved questions and their likely owners
>
>Separate confirmed facts, assumptions, and missing evidence. Include citations to the source files.

- **Action plan**
>Turn this situation summary into an action plan for preparing a seven-day retention decision package.
>
>Organize the work into:
>- Data that must be validated
>- Analysis required
>- Policy and consent checks
>- Stakeholder decisions
>- Final deliverables

- **Governance check**
>Review the proposed action plan against the retention policy.
>Identify any steps requiring human approval, consent verification, vulnerable-customer handling, or confirmation from Network Operations.

## Stage 2 - Clean and analyze the retention cohort in Excel
Open Excel file **AsterWave_Retention_Cohort_Demo.xlsx**.

### Detect and clean data issues
>Inspect the Retention Cohort table for data quality issues.
>Look for inconsistency, missing value, duplicate customer ID, invalid data type and formatting issues.
>Create a review table showing the row, column, issue, and recommended handling.
>Do not change the source data yet.

### Explore data
>Compare download speed, latency, and dropped-call rate by plan.

>Which complaint reasons are most common overall, and by segment?

### Analyze data
>What characteristics distinguish high-risk customers from low-risk customers?

>Does churn risk rise with more contacts, complaints, degraded networks, or dropped calls?

>Compare churn risk, service quality, complaint volume, and offer coverage by plan and tenure band.

### Create churn intervention cohort
Run the following prompt in **Edit** mode:
>Propose a churn intervention cohort in a new worksheet, include only customers who:
>- Have two or more contacts in the last 30 days
>- Show degraded network experience
>- Match an active approved offer
>
>Create separate exception list for:
>- High-cost offers requiring elevated approval
>
>List all data in tables with summary of selection criteria.

### Other analysis and data visualization
>Create a professional PivotTable on a new worksheet. Put complaint reason in rows, risk band in columns, and add customer count plus total monthly fee to values. Add eligible offer, segment and plan as filters.

>Add an Offer Coverage column showing Covered when an active eligible offer exists, otherwise Gap.

>Highlight customers with a churn-risk score of 75 or higher in light red.

>Add Risk Band column, apply a red–amber–green scale to churn risk, data bars to download speed, and highlight entire rows where risk is at least 75, the network is degraded, and no incident ID is recorded.

>Create a Risk-band distribution chart in a new sheet - clustered column chart showing Low, Medium, and High customer counts.

>Create a heatmap for Complaint Reason × Risk Band in a new sheet.

## Stage 3 - Create the retention intervention brief in Word
- **Create draft:** Attach **Meranti_Coast_Complaint_Summary.docx**, **Meranti_Coast_Service_Quality_Report.docx**, **Retention_Eligibility_Policy.docx**, and **AsterWave_Retention_Cohort_Demo.xlsx**:
>Using the attached Meranti Coast complaint summary, service-quality report, retention policy, and the "Churn Intervention" worksheet in the attached Excel, draft a two-page retention intervention brief for the Customer Care Director.
>
>Use these sections:
>1. Decision requested
>2. Customer and business problem
>3. Evidence from care and network data
>4. Proposed seven-day intervention cohort
>5. Eligible treatments
>6. Exclusions and exception handling
>7. Human approvals and governance controls
>8. Measurement plan
>9. Open decisions and owners
>
>Clearly distinguish confirmed facts, analytical indicators, and recommendations.

Save the file as "**Meranti Coast Retention Intervention Brief.docx**".

- **Review and refine**
>Review this brief for senior-management readability.
>
>- Place the requested decision in the opening paragraph
>- Reduce technical detail in the main body
>- Move technical assumptions into an appendix
>- Convert long paragraphs into concise bullets where appropriate
>- Retain all approval, consent, vulnerability, and audit controls

- **Create executive summary**
>Write an executive summary of no more than 150 words.
>
>It must explain:
>- Why action is needed now
>- Which customers are being considered
>- What treatment is proposed
>- Which controls prevent inappropriate outreach
>- What approval is required

## Stage 4 - Convert the brief into an executive presentation
- **Create draft:** Open an existing presentation with the right template. Run the prompt with attached "**Meranti Coast Retention Intervention Brief.docx**".
>Create a new seven-slide executive presentation from the attached Meranti Coast retention intervention brief.
>
>Use this structure with customer journey visual and KPI cards.
>1. Decision required
>2. Customer-care problem and business impact
>3. Customer journey showing repeat contact and service degradation
>4. Evidence from the retention cohort
>5. Proposed seven-day intervention workflow
>6. Governance, consent, approvals, and exception handling
>7. Measures of success and next steps
>
>Use the styles and templates in the current presentation.

- **Review and refine**
>Review the presentation as if you are the Customer Care Director.
>
>Identify:
>- Slides with too much detail
>- Claims not clearly supported by the brief
>- Missing decisions
>- Governance controls that should be more visible

## Stage 5 - Coordinate approvals in Outlook
- **Create draft:** Run the prompt with attached "**Meranti Coast Retention Intervention Brief.docx**".
>Draft an email to Customer Care, Network Operations, Data Governance, Legal, and Finance.
>
>Summarize the attached Meranti Coast retention intervention brief, and request approval.
>
>Ask each team to confirm:
>- Customer Care: intervention scope and operating ownership
>- Network Operations: accuracy of service-degradation and incident data
>- Data Governance: consent, vulnerability, and data-handling controls
>- Legal: use of synthetic data and customer communication conditions
>- Finance: approval thresholds for the proposed offers

- **Review and refine**
>Rewrite the email to fit within 180 words.
>Keep the decision requested from each team explicit and easy to scan.
>Use a professional, neutral tone.

## Final demo outcome
By the end of the story, the care manager has produced:
- A grounded situation summary
- A cleaned and analyzed retention cohort
- A governed intervention recommendation and decision-ready Word brief
- A seven-slide executive presentation
- A targeted multi-stakeholder approval request
