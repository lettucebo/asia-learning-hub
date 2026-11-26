# Prompt pack

[Workshop home](./README.md)

Every prompt and follow-up from the six workshops, ready to copy. Use the code-block copy button in GitHub. Prompts are verbatim from the instructor deck. Always ask the follow-up, because the first answer is only a starting point.

> [!NOTE]
> In Copilot Chat prompt 2, replace the words in square brackets with your group topic.

## Session 1: Word

[Open the lab](./lab/01-word.md)

### Try Out 1: Get to know the client

**Where:** Word › open the file › Copilot · **File:** [01_Client_Background.docx](./sample-files/01_Client_Background.docx)

**Prompt**

```text
Summarise this client background for a new engagement team member in no more than 8 bullet points. Include what the business does, the group structure, the key FY2026 numbers and the three changes that increase risk the most.
```

**Follow-up**

```text
Which numbers or statements in this document look inconsistent or need checking? Tell me the section for each one.
```

### Try Out 2: From interview notes to a finding

**Where:** Word › open the file › Copilot · **File:** [02_Audit_Interview_Notes.docx](./sample-files/02_Audit_Interview_Notes.docx)

**Prompt**

```text
From the Financial Controller and Inventory Manager interviews, create a table with the columns: Statement, Who said it, Possible risk, Evidence to request.
```

**Follow-up**

```text
Pick the most serious issue and write one audit finding with three headings: Condition, Risk, Recommendation. Use only facts from this document.
```

**Optional stretch task:** Open `03_Audit_Findings_Draft.docx`, select finding F-02 and ask Copilot to rewrite it in neutral, professional language with a risk rating.

### Refine: Write the executive summary

**Where:** Word › open the file › Copilot · **File:** [03_Audit_Findings_Draft.docx](./sample-files/03_Audit_Findings_Draft.docx)

**Prompt**

```text
Write the executive summary for this draft: the three most significant matters, the financial exposure and the evidence still outstanding, in under 150 words for the engagement leader.
```

**Follow-up**

```text
Check your summary against the document and list anything you cannot support.
```

## Session 2: Excel

[Open the lab](./lab/02-excel.md)

### Try Out 3: Flag risky journals

**Where:** Excel › General_Ledger sheet › Copilot · **File:** [04_Audit_Analytics.xlsx](./sample-files/04_Audit_Analytics.xlsx)

**Prompt**

```text
Add a column called Self_Approved that shows Yes when Prepared By equals Approved By, and a column called Late_Posting that shows Yes when Posting Time is after 20:00.
```

**Follow-up**

```text
How many Manual journals are both self-approved and posted late? List them with Journal ID, Description and Local Amount.
```

### Try Out 4: Hunt for exceptions

**Where:** Excel › General_Ledger sheet › Copilot · **File:** [04_Audit_Analytics.xlsx](./sample-files/04_Audit_Analytics.xlsx)

**Prompt**

```text
Find transactions that look unusual: the same amount paid to the same vendor on the same day, amounts just below SGD 25,000, and round-number manual entries in December. Explain why each one is unusual.
```

**Follow-up**

```text
Look up each Vendor ID in the Vendors sheet and flag payments to vendors that are Dormant or a Related Party.
```

**Optional stretch task:** In the Expenses sheet, ask: “Find duplicate claims and claims approved by the person who submitted them.”

### Refine: Prioritise your top 5

**Where:** Excel › Audit_Findings sheet › Copilot · **File:** [04_Audit_Analytics.xlsx](./sample-files/04_Audit_Analytics.xlsx)

**Prompt**

```text
Summarise my top 5 exceptions by priority with Journal ID, amount, why it is unusual and the evidence we should request.
```

**Follow-up**

```text
Copy your top 5 into the Audit_Findings sheet and compare with the answers revealed by your instructor.
```

### Optional tax stretch _(Suggested, not from the course pack)_

**Classify prompt**

```text
Act as an audit senior. In the Tax_Adjustments sheet, list the items whose Evidence Status is not Provided, with the evidence still needed and the row each comes from. Say these are training assumptions, not tax advice.
```

**Review prompt**

```text
Act as an audit senior. In Review_Summary, draft a conclusion and next action for each area, naming the evidence still needed. No tax opinion: these are training assumptions.
```

## Session 3: PowerPoint

[Open the lab](./lab/03-powerpoint.md)

### Try Out 5: Build the executive briefing

**Where:** PowerPoint › New presentation › Copilot · **File:** [03_Audit_Findings_Draft.docx](./sample-files/03_Audit_Findings_Draft.docx)

**Prompt**

```text
Create a 5-slide executive briefing for Meridian Retail Group's leadership from /03_Audit_Findings_Draft.docx. Slides: Executive summary, Financial snapshot, Top 3 findings, Evidence outstanding, Recommended next actions. Maximum 4 bullets per slide.
```

**Follow-up**

```text
Add a slide with a table of all six findings showing Finding, Rating, Owner and Target date.
```

### Try Out 6: Make it boardroom-ready

**Where:** PowerPoint › your new deck › Copilot · **File:** [01_Client_Background.docx](./sample-files/01_Client_Background.docx), [06_Supporting_Documents.pdf](./sample-files/06_Supporting_Documents.pdf)

**Prompt**

```text
Rewrite the Executive summary slide for a busy CFO: one headline sentence and three bullets that each include an amount.
```

**Follow-up**

```text
Add a slide about the related-party logistics arrangement using /06_Supporting_Documents.pdf: what we found, why it matters, and what evidence we still need.
```

**Optional stretch task:** Add speaker notes to every slide, under 60 words each.

### Refine: Challenge your deck

**Where:** PowerPoint › your briefing deck › Copilot · **File:** [03_Audit_Findings_Draft.docx](./sample-files/03_Audit_Findings_Draft.docx)

**Prompt**

```text
Review this presentation as a sceptical board member. What is unclear, unsupported or missing? Suggest three improvements.
```

**Follow-up**

```text
Apply the one improvement that matters most.
```

## Session 4: Outlook

[Open the lab](./lab/04-outlook.md)

### Try Out 7: What does this email need from me?

**Where:** Outlook › open the Meridian email › Copilot · **File:** [Meridian_Retail_Email.eml](./sample-files/Meridian_Retail_Email.eml)

**Prompt**

```text
Summarise this email and its attachments. What is being asked of me, by when, and which items are blocked by missing evidence?
```

**Follow-up**

```text
Put the actions in a table with Action, Owner, Due date and Evidence needed, sorted by due date.
```

### Try Out 8: Reply with the right tone

**Where:** Outlook › Reply › Draft with Copilot · **File:** [Meridian_Retail_Email.eml](./sample-files/Meridian_Retail_Email.eml)

**Prompt**

```text
Draft a reply to the Finance Director confirming we can meet the 20 February board timeline only if the outstanding evidence arrives by 12 February. List the three most urgent evidence items. Professional and firm, under 150 words.
```

**Follow-up**

```text
Make it more diplomatic and propose a 30-minute call this Thursday.
```

**Optional stretch task:** Use Coaching by Copilot on your draft and apply one suggestion.

### Refine: Close the gaps

**Where:** Outlook › your draft reply › Copilot · **File:** [Meridian_Retail_Email.eml](./sample-files/Meridian_Retail_Email.eml)

**Prompt**

```text
Compare my reply with the original email. Have I answered every question and request? List anything I missed.
```

**Follow-up**

```text
Fix the gaps and save the reply as a draft (do not send).
```

## Session 5: Teams

[Open the lab](./lab/05-teams.md)

### Try Out 1: Catch up in 2 minutes

**Where:** Teams › Meridian engagement chat › Copilot · **File:** [Meridian-Teams-channel-transcript.txt](./sample-files/Meridian-Teams-channel-transcript.txt)

**Prompt**

```text
Summarise this conversation. What has been decided, what is still open, and who owns each action?
```

**Follow-up**

```text
What has been said about the related-party logistics arrangement and the duplicate advisory payments? Show who said it.
```

### Try Out 2: Prepare tomorrow’s status meeting

**Where:** Teams › Meridian engagement chat › Copilot · **File:** [Meridian-Teams-channel-transcript.txt](./sample-files/Meridian-Teams-channel-transcript.txt)

**Prompt**

```text
Help me prepare a 30-minute status meeting with the Finance Director: an agenda, the five questions we must ask, and the evidence we still need.
```

**Follow-up**

```text
Draft a short message to the team sharing the agenda and asking each owner to update their status by 5 pm.
```

### Refine: Action summary

**Where:** Teams › Meridian engagement chat › Copilot · **File:** [Meridian-Teams-channel-transcript.txt](./sample-files/Meridian-Teams-channel-transcript.txt)

**Prompt**

```text
Based on this chat, list every action with owner and due date. Flag anything with no owner or no date.
```

**Follow-up**

```text
Post your action list in the training chat (training chat only).
```

## Session 6: Copilot Chat

[Open the lab](./lab/06-copilot-chat.md)

### Try Out 1: Brief the engagement leader

**Where:** Chat (Web) › + Add files · **File:** [01_Client_Background.docx](./sample-files/01_Client_Background.docx), [04_Audit_Analytics.xlsx](./sample-files/04_Audit_Analytics.xlsx), [06_Supporting_Documents.pdf](./sample-files/06_Supporting_Documents.pdf)

**Prompt**

```text
Act as an audit senior. Using only the attached files, write a one-page briefing for an engagement leader joining today: the client, the key FY2026 numbers, the top 5 risks and the evidence still outstanding. Name the file for each point.
```

**Follow-up**

```text
Which of these points are confirmed by a document and which are your assumptions?
```

### Try Out 2: Group investigation

**Where:** Chat (Web) › same conversation · **File:** [01_Client_Background.docx](./sample-files/01_Client_Background.docx), [04_Audit_Analytics.xlsx](./sample-files/04_Audit_Analytics.xlsx), [06_Supporting_Documents.pdf](./sample-files/06_Supporting_Documents.pdf)

**Prompt**

```text
Investigate [our group topic]. Find all related evidence across the three files, explain what looks wrong, quantify the exposure in SGD and list the evidence we should request next.
```

**Follow-up**

```text
Turn this into three sentences I can present to the engagement leader in one minute.
```

### Refine: Verify every number

**Where:** Chat (Web) › same conversation · **File:** [01_Client_Background.docx](./sample-files/01_Client_Background.docx), [04_Audit_Analytics.xlsx](./sample-files/04_Audit_Analytics.xlsx), [06_Supporting_Documents.pdf](./sample-files/06_Supporting_Documents.pdf)

**Prompt**

```text
Check your investigation again. For each number you quoted, tell me the exact file and where it appears. Remove anything you cannot support.
```

**Follow-up**

```text
Compare your answer with another group's — did Copilot reach the same conclusion?
```

> [!IMPORTANT]
> Copilot proposes; the team verifies. This is a training exercise, not audit or tax advice.
