# Regional 5G Service Degradation: From Alarm to Executive Action

AsterWave is experiencing sustained 5G service degradation across the Harbor District. Network latency and packet loss are worsening on several cells, customer complaints are rising, enterprise customers may be at SLA risk, and a recent QoS configuration change may be related. The evidence is distributed across network data, operational reports, customer-care analysis, the change record, and the service-assurance runbook.

The Service Assurance Manager must prepare for a 15:00 cross-functional review. With Microsoft Copilot, the manager plans to synthesize the incident in Copilot Chat, analyze operational and customer-impact data in Excel, produce a decision brief in Word, create an executive review deck in PowerPoint, and use Outlook to coordinate actions with other teams.

# Paint points and demonstrated benefits
| **Pain point** | **How Copilot helps** | **Business benefits** |
|----------------|-----------------------|-----------------------|
| Incident context is fragmented across files and data tables. | Copilot Chat synthesizes network, customer, change, and policy context with source grounding. | Faster situational awareness and less manual searching. |
| Teams debate severity using different metrics. | Copilot in Excel explores trends, prioritizes cells, and relates KPIs to customer impact. |	Shared evidence base and clearer operational prioritization. |
| Correlation may be presented as confirmed root cause.	| Copilot in Word structures confirmed facts, hypotheses, gaps, and approval needs separately. |	Better decision quality and reduced communication risk. |
| Leadership needs a concise narrative, not raw telemetry. | Copilot in PowerPoint turns the brief into a decision-oriented executive story. |	Shorter preparation time and clearer decisions. |
| Actions can be vague or lack ownership. |	Copilot in Outlook drafts a structured coordination message from the final brief and decisions. |	Clear accountability, deadlines, and faster execution. |

# Demo files
[Telco_5G_Service_Degradation_Demo_Files.zip](https://github.com/CSDSkilling/asia-learning-hub/raw/refs/heads/main/industry/Telco/Copilot/5G%20Service%20Degradation/data-files/Telco_5G_Service_Degradation_Demo_Files.zip)

# Demo journey
| **Stage** | **Copilot Experience** | **Story** |
|-----------|------------------------|-----------|
| 1. Understand |	Copilot Chat | Bring fragmented incident material together and identify what is confirmed, suspected, and missing. |
| 2. Investigate | Copilot in Excel	| Analyze KPI deterioration and customer impact to identify the highest-priority cells. |
| 3. Decide |	Copilot in Word |	Create a decision brief with evidence, hypotheses, safeguards, actions, and approval gates. |
| 4. Communicate |Copilot in PowerPoint	| Convert the technical brief into a leadership-ready operations review. |
| 5. Coordinate |	Copilot in Outlook | Draft the post-review action request using the brief and agreed decisions. |

## Stage 1 - Understand in Copilot Chat
Attach all demo files and run the following prompts:
>Using the attached AsterWave documents, summarize the Harbor District service degradation for a Service Assurance Manager. Identify affected services, customer impact, timeline, likely contributing factors, unresolved questions, and required decision.

>Separate the findings into confirmed facts, reasonable hypotheses, and missing evidence. Flag any statements that could incorrectly imply that CHG-58217 is the confirmed root cause.

>Create a preparation checklist for the review. Include technical validation, customer and SLA impact, approval requirements, and the decision owner for each topic.

## Stage 2 - Investigate in Excel
Open Excel file **AsterWave_Harbor_District_Service_Assurance.xlsx**.

### Detect and clean data issues
>Review the data in this table, identify data quality issues such as inconsistency, wrong format, out-of-range values, missing values etc. Create a data quality reporting with details of the type of issue, location, and suggestion.

### Explore and Analyze data
>Show me the list of cells ordered by average packet loss % in descending order

>Analyze the network KPI and customer-impact tables. Identify the three cells with the most significant service deterioration and explain the evidence for each.

>Assess whether complaint volume appears more closely correlated with latency, packet loss, or availability.

### Highlight, visualize, and create advanced analysis
>Create a cell priority PivotTable, with grouping by SLA Risk and Cell ID, value of priority score, complaints, enterprise subscribers, vulnerable customers, and subscribers

>Create a "Recommended Priority" column, with value Critical, High, Medium or Low  when Priority Score value is: >= 75, >= 55, >=35 or else.

>Format the "Cell ID" in dark red fill with white bold text when Recommended Priority is critical.

>Create three line charts for the daily average of availability, latency and packet loss. Mark the date of CHG-58217 using a vertical line.

>Create a heatmap for cells vs change of availability, latency and packet loss due to CHG-58217 on 2026-10-19.

## Stage 3 - Decide in Word
- **Draft incident decision brief:** Attach all demo files:
>Based on the AsterWave source material and Excel analysis, draft an incident decision brief using the format in the incident brief template.

Save the file as "**Harbor District 5G Service Incident Brief.docx**".

- **Refine**
>Rewrite the executive summary for a senior operations audience in no more than six bullets. Preserve uncertainty where root cause is not confirmed.

## Stage 4 - Communicate in PowerPoint
- **Draft execution presentation:** Open an existing presentation with the right template. Run the prompt with attached "**Harbor District 5G Service Incident Brief.docx**".
>Create a five-slide executive presentation from the attached incident brief: 1) situation and scope, 2) customer and service impact, 3) evidence and incident timeline, 4) recommended actions and safeguards, and 5) decisions required today. Use concise titles that state the takeaway. Do not present CHG-58217 as the confirmed root cause. Use the format and styles in this presentation.

- **Review and refine**
>Review this deck as if you were the decision maker. Identify what is unclear, too detailed, or missing. Recommend changes that strengthen the business impact, evidence, risks, trade-offs, recommendation, and decision required. Provide slide-by-slide suggestions and propose a stronger executive storyline.

## Stage 5 - Coordinate in Outlook
- **Draft action-request email:** Run the prompt with attached "**Harbor District 5G Service Incident Brief.docx**".
>Draft an action-request email to Network Operations, Change Management, Customer Care, Enterprise Services, Finance, and Legal. Summarize the Harbor District degradation and ask each team to confirm its assigned action, dependency, and completion time. State clearly that root cause remains under validation.

- **Review and refine**
>Make the email concise and action-oriented. Add a table with team, requested action, deadline, and approval or evidence required. Include a request to escalate blockers before the rollback decision window.

## Final demo outcome
By the end of the story, the Service Assurance manager has produced:
-	A grounded situation summary assembled from multiple operational sources.
-	A prioritized, data-supported view of the cells and customer groups requiring attention.
-	A decision brief that separates fact, hypothesis, risk, and approval requirements.
-	A leadership-ready presentation focused on service impact and decisions.
-	A ready-to-review Outlook coordination message with clear owners and deadlines.
