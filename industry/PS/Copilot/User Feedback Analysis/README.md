# User Feedback Analysis: From Hundreds of Comments to Clear Themes

The Riverbend Services Agency has launched an online service for renewing and updating personal details (the "MyRiverbend Renewals" service). Since launch, the Digital Service Product Owner has received hundreds of comments through satisfaction survey free text, feedback forms, app store reviews and contact centre notes.

Rather than reading every comment, the Product Owner wants to understand the overall themes: what is frustrating users, what is working well, which issues matter most, and what to fix first.

With Microsoft Copilot, the Product Owner works across Chat, Excel, Word, PowerPoint and Outlook to analyse the feedback, quantify themes, produce a findings brief, share the story with leadership and coordinate improvements with delivery teams. Copilot surfaces patterns; the Product Owner validates findings against the source comments and decides priorities.

# Pain points and demonstrated benefits
| **Pain point** | **How Copilot helps** | **Business benefits** |
|----------------|-----------------------|-----------------------|
| Hundreds of comments across multiple sources are too many to read manually. | Copilot Chat summarises feedback and identifies recurring themes with example quotes. | Much faster understanding of user sentiment. |
| It is unclear what matters most. | Copilot in Excel classifies comments by theme and sentiment, and counts and ranks them by journey step and source. | Evidence-based prioritisation instead of anecdote. |
| Positive feedback is overlooked when focusing on complaints. | Copilot highlights what is working well alongside pain points. | Balanced view; protects what users value. |
| Findings are hard to share in a consistent format. | Copilot in Word drafts a structured findings and recommendations brief. | Consistent, auditable insights that stakeholders can trust. |
| Leaders need a concise story. | Copilot in PowerPoint turns the brief into a decision-oriented presentation. | Faster alignment and clearer decisions. |
| Improvement work needs owners and timelines. | Copilot in Outlook drafts requests to design, development, content and service teams. | Faster action and clear accountability. |

# Demo files
*To be added.* Proposed contents (all synthetic data):
- `Riverbend_Renewals_User_Feedback.xlsx` – ~300 comments with source, date, rating, service step, device and free text (include blanks, duplicates and mixed formats)
- `Riverbend_Renewals_Service_Overview.docx` – description of the service and user journey steps
- `Riverbend_Renewals_Satisfaction_Survey_Summary.docx`
- `Riverbend_Renewals_Product_Roadmap.docx`
- `Riverbend_User_Research_Findings_Template.docx`

# Demo journey
| **Stage** | **Copilot Experience** | **Story** |
|-----------|------------------------|-----------|
| 1. Understand | Copilot Chat | Get a first view of themes, frustrations and positives across the feedback without reading every comment. |
| 2. Analyse | Copilot in Excel | Clean, classify and quantify comments by theme, sentiment, journey step and source. |
| 3. Report | Copilot in Word | Produce a findings and recommendations brief that distinguishes evidence, interpretation and recommendations. |
| 4. Communicate | Copilot in PowerPoint | Convert the brief into a leadership-ready story. |
| 5. Coordinate | Copilot in Outlook | Draft improvement requests to delivery and content teams. |

## Stage 1 - Understand in Copilot Chat
Attach the service overview, survey summary and feedback file, then run the following prompts:
>Using the attached feedback, summarise the overall themes for a Digital Service Product Owner. Identify the main things frustrating users, what is working well, and any feedback about specific steps in the service. Include a short representative quote for each theme.

>Separate the themes into those mentioned by many users, those mentioned by a few but with high impact (for example accessibility or inability to complete a task), and those that need more evidence. Do not overstate how many people raised a theme.

>Create a checklist of what I should validate before sharing these findings, such as sample bias, duplicate comments and sources that are over-represented.

## Stage 2 - Analyse in Excel
Open Excel file **Riverbend_Renewals_User_Feedback.xlsx**.

### Detect and clean data issues
>Review the data in this table and identify data quality issues such as blank comments, duplicate comments, inconsistent source names, missing ratings, wrong date formats and out-of-range ratings. Create a review table showing the row, column, issue and recommended handling. Do not change the source data yet.

### Classify and analyse feedback
>Add a "Theme" column that categorises each comment into a short list of themes (for example login and identity, document upload, payment, clarity of instructions, speed and reliability, accessibility, support, positive experience). Show the list of themes you used.

>Add a "Sentiment" column with Positive, Neutral or Negative for each comment.

>Show the number of comments by theme and sentiment, ordered from highest to lowest count.

>Which service steps have the lowest average rating? Compare themes by step.

>Compare themes by source and by device type. Note any differences between sources.

### Other analysis and data visualisation
>Create a PivotTable with theme in rows, sentiment in columns and comment count as values. Add source, service step and device as filters.

>Create a bar chart of the top 10 themes by comment count, split by sentiment.

>Create a line chart of average rating by week and mark the date of the most recent release.

>Highlight rows where the comment is Negative and the rating is 2 or below in light red.

## Stage 3 - Report in Word
- **Create draft:** Attach the service overview, survey summary, user research findings template and Excel analysis:
>Based on the attached material and the Excel analysis, draft a user feedback findings brief using the user research findings template. Include key themes, what is working well, what is frustrating users, evidence for each finding, confidence level, and recommended improvements.

Save the file as "**MyRiverbend Renewals Feedback Findings.docx**".

- **Refine**
>Rewrite the executive summary in no more than five bullets for a senior audience. Make clear where evidence is strong and where it is limited.

## Stage 4 - Communicate in PowerPoint
- **Create draft:** Open an existing presentation with the right template. Run the prompt with attached "**MyRiverbend Renewals Feedback Findings.docx**".
>Create a five-slide presentation from the attached findings: 1) what we looked at, 2) what is working well, 3) what is frustrating users, 4) recommended improvements and priority, and 5) decisions and next steps. Use concise titles that state the takeaway. Include user quotes where helpful. Use the format and styles in this presentation.

- **Review and refine**
>Review this deck as if you were the Executive Sponsor. Identify what is unclear, unsupported by evidence or missing, and suggest changes to strengthen the recommendation.

## Stage 5 - Coordinate in Outlook
- **Create draft:** Run the prompt with attached "**MyRiverbend Renewals Feedback Findings.docx**".
>Draft an email to Design, Development, Content and Contact Centre teams. Summarise the findings and ask each team to confirm the proposed actions: Design to review the document upload step, Development to investigate reliability issues, Content to simplify instructions, and the Contact Centre to share common user questions.

- **Review and refine**
>Make the email concise. Add a table with team, requested action, priority and target date.

## Responsible use
- Copilot classification is a starting point; spot-check themes and sentiment against the original comments.
- Feedback volume does not equal importance; consider impact on accessibility and inclusion.
- Use only synthetic or approved data; remove personal information from comments before analysis.

## Final demo outcome
By the end of the story, the Product Owner has produced:
- A grounded summary of themes, frustrations and positives.
- A classified and quantified view of feedback by theme, sentiment and service step.
- A findings brief that separates evidence, interpretation and recommendations.
- A leadership-ready presentation.
- A ready-to-review Outlook message with clear owners and timelines.
