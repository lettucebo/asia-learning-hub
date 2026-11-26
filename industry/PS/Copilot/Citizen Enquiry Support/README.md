# Citizen Enquiry Support: From High-Volume Inbox to Confident Responses

The Riverbend Services Agency frontline team is receiving a high volume of citizen enquiries across multiple channels: email, web forms, phone call notes, social media messages and in-person service centre logs. Many enquiries are repeats, some are urgent or involve vulnerable citizens, and answers depend on policy and eligibility guidance spread across several documents.

The Frontline Service Team Leader needs to understand what is coming in, prioritise what needs attention first, give officers consistent and accurate responses, and brief leadership on demand and service pressure.

With Microsoft Copilot, the team leader works across Chat, Excel, Word, PowerPoint and Outlook to triage enquiries, analyse volumes and trends, prepare response guidance, report to leadership and coordinate follow-up. Copilot supports the team; officers remain responsible for decisions, eligibility determinations and what is sent to citizens.

# Pain points and demonstrated benefits
| **Pain point** | **How Copilot helps** | **Business benefits** |
|----------------|-----------------------|-----------------------|
| Enquiries arrive across many channels in inconsistent formats. | Copilot Chat summarises and groups enquiries by topic, urgency and channel with source grounding. | Faster situational awareness and less manual reading. |
| Volumes, wait times and repeat contacts are hard to see in raw logs. | Copilot in Excel cleans the enquiry log, identifies trends, peaks and backlog by topic and channel. | Evidence-based staffing and prioritisation decisions. |
| Responses vary between officers and may not reflect current policy. | Copilot in Word drafts response guidance and template replies grounded in the service policy and FAQ. | Consistent, accurate, plain-language responses. |
| Urgent or vulnerable-citizen cases can be buried in the queue. | Copilot flags enquiries needing escalation or human review according to the escalation guideline. | Reduced risk and safer handling of sensitive cases. |
| Leadership needs a short narrative, not raw logs. | Copilot in PowerPoint turns the analysis into a decision-oriented briefing. | Shorter preparation time and clearer decisions. |
| Follow-up actions across teams lack owners and deadlines. | Copilot in Outlook drafts a structured coordination message from the final brief. | Clear accountability and faster resolution. |

# Demo files
(all synthetic data):
- `Riverbend_Citizen_Enquiry_Log.xlsx` – 4 weeks of enquiries with channel, date, topic, status, response time, repeat-contact flag and priority fields (include deliberate data quality issues)
- `Riverbend_Service_Policy_and_Eligibility_Guide.docx`
- `Riverbend_Frequently_Asked_Questions.docx`
- `Riverbend_Escalation_and_Vulnerable_Citizen_Guideline.docx`
- `Riverbend_Sample_Enquiry_Emails.docx` - 25 sample enquiries from email, web form, phone notes, social media and service centre notes.
- `Riverbend_Service_Pressure_Briefing_Template.docx`
- `Riverbend_Leadership_Briefing_Template.pptx`

# Demo journey
| **Stage** | **Copilot Experience** | **Story** |
|-----------|------------------------|-----------|
| 1. Understand | Copilot Chat | Bring together sample enquiries, policy and FAQs to see what citizens are asking, what is urgent, and where guidance is unclear. |
| 2. Analyse | Copilot in Excel | Clean the enquiry log and identify volume, backlog, response time and repeat-contact patterns by topic and channel. |
| 3. Respond | Copilot in Word | Create consistent response guidance and template replies, and a service pressure brief. |
| 4. Communicate | Copilot in PowerPoint | Convert the brief into a leadership-ready service pressure update. |
| 5. Coordinate | Copilot in Outlook | Draft follow-up requests to policy, digital, contact centre and communications teams. |

## Stage 1 - Understand in Copilot Chat
Attach all Word files and run the following prompts:
>Using the attached sample enquiries, service policy, FAQ and escalation guideline, summarise what citizens are asking about for a Frontline Service Team Leader. Group enquiries by topic and channel, identify the most common themes, and highlight any that look urgent or involve a vulnerable citizen. Include citations to the source files.

>Separate your findings into what is clearly answered by policy, what is ambiguous or conflicting, and what is missing from current guidance. Do not make eligibility decisions for individual citizens.

>Create a preparation checklist for this week's team huddle. Include enquiries needing escalation, guidance gaps to raise, and an owner for each item.

## Stage 2 - Analyse in Excel
Open Excel file **Riverbend_Citizen_Enquiry_Log.xlsx**.

### Detect and clean data issues
>Review the data in this table and identify data quality issues such as inconsistent channel or topic names, missing values, duplicate enquiry IDs, wrong date formats and out-of-range response times. Create a review table showing the row, column, issue and recommended handling. Do not change the source data yet.

### Analyse data
>Show the number of enquiries by topic and by channel, ordered from highest to lowest.

>Which topics have the longest average response time and the highest repeat-contact rate?

>Identify the days and channels where volume peaked and describe what may have driven the peaks, noting where the data does not provide an explanation.

>Compare the proportion of enquiries resolved at first contact by topic and channel.

### Other analysis and data visualisation
>Create a PivotTable with topic in rows, channel in columns, and enquiry count and average response time as values. Add priority and status as filters.

>Add a "Recommended Handling" column with value Escalate, Priority, Standard or Self-service based on the priority and vulnerability fields and the escalation guideline.

>Highlight rows where the enquiry has been open for more than 5 days in light red.

>Create a line chart of daily enquiry volume by channel.

>Create a heatmap of topic against channel showing enquiry count.

## Stage 3 - Respond in Word
- **Create draft:** Attach all demo files:
>Based on the attached policy, FAQ and the Excel analysis, draft response guidance for the three most common enquiry topics. For each topic include a plain-language summary, a template reply, information to confirm with the citizen, and when to escalate to a human decision-maker.

Save the file as "**Citizen Enquiry Response Guidance.docx**".

- **Create service pressure brief:**
>Using the service pressure briefing template and the Excel analysis, draft a brief for the Director of Service Delivery covering volumes, response times, backlog, top themes, guidance gaps, risks and recommended actions.

Save the file as "**Frontline Service Pressure Brief.docx**".

- **Refine**
>Rewrite the template replies at a reading level suitable for the general public. Keep them empathetic, avoid jargon, and do not promise outcomes or eligibility.

## Stage 4 - Communicate in PowerPoint
- **Create draft:** Open an existing presentation with the right template. Run the prompt with attached "**Frontline Service Pressure Brief.docx**".
>Create a five-slide leadership presentation from the attached brief: 1) situation and scope, 2) enquiry volume and trends, 3) citizen impact and risks, 4) recommended actions, and 5) decisions required. Use concise titles that state the takeaway. Use the format and styles in this presentation.

- **Review and refine**
>Review this deck as if you were the Director of Service Delivery. Identify what is unclear, too detailed or missing. Recommend changes that strengthen the evidence, risks, recommendation and decision required.

## Stage 5 - Coordinate in Outlook
- **Create draft:** Run the prompt with attached "**Frontline Service Pressure Brief.docx**".
>Draft an email to Policy, Digital Services, the Contact Centre and Communications. Summarise the service pressure and ask each team to confirm its action: Policy to clarify the ambiguous guidance, Digital Services to improve the web form and self-service content, Contact Centre to confirm staffing and escalation handling, and Communications to review public messaging.

- **Review and refine**
>Make the email concise and action-oriented. Add a table with team, requested action, deadline and evidence required. Request that blockers be escalated early.

## Responsible use
- Copilot drafts and summarises; officers make all eligibility, entitlement and escalation decisions.
- Review every drafted citizen response before sending.
- Use only synthetic or approved data; do not paste real citizen personal information into prompts.

## Final demo outcome
By the end of the story, the team leader has produced:
- A grounded summary of citizen enquiries and guidance gaps.
- A cleaned and analysed enquiry log showing volume, backlog and repeat-contact patterns.
- Consistent, plain-language response guidance and a service pressure brief.
- A leadership-ready presentation focused on impact and decisions.
- A ready-to-review Outlook message with clear owners and deadlines.
