# IT Service Desk Monthly Service Review with Microsoft 365 Copilot

> **Industry:** IT / ITeS (IT Services & Managed Services) · **Workload:** Microsoft 365 Copilot · **Level:** Intermediate · **Demo time:** 40–45 minutes

![Industry](https://img.shields.io/badge/Industry-IT%20%2F%20ITeS-blue) ![Product](https://img.shields.io/badge/Product-Microsoft%20365%20Copilot-purple) ![Use%20Case](https://img.shields.io/badge/Copilot%20Use%20Case-1-green)

---

## Table of contents

1. [Overview](#overview)
2. [Business scenario](#business-scenario)
3. [Persona](#persona)
4. [Pain points](#pain-points)
5. [Business benefits](#business-benefits)
6. [Learning objectives](#learning-objectives)
7. [Prerequisites](#prerequisites)
8. [Package contents](#package-contents)
9. [Environment setup](#environment-setup)
10. [Demo walkthrough](#demo-walkthrough)
11. [Expected outcomes](#expected-outcomes)
12. [Real-world alignment](#real-world-alignment)
13. [Responsible AI considerations](#responsible-ai-considerations)
14. [Extend this use case](#extend-this-use-case)
15. [Troubleshooting](#troubleshooting)

---

## Overview

Outsourced IT service desks are governed by contracts with **Service Level Agreements (SLAs)** and a **Monthly Service Review (MSR)**, where the service provider reports performance, explains incidents and proposes improvements to the client.

Preparing an MSR is typically a manual, multi-day effort: exporting tickets from the ITSM tool, pivoting data in Excel, cross-checking the contract, chasing last month's actions, writing the report, building the deck, and following up after the meeting.

This use case shows how a Service Delivery Manager uses **Microsoft 365 Copilot** across **Copilot Chat, Excel, Word, PowerPoint, Teams and Outlook** to move from raw ticket data to a client-ready review — and a closed-loop follow-up — in under an hour.

---

## Business scenario

**Contoso Ltd** is an IT services company. It runs a **24x7 IT Service Desk (L1) and resolver groups (L2)** for its client **Fabrikam Retail**, supporting ~8,000 users across a head office, 2 distribution centres and 60 retail stores.

The contract (*Schedule 3 – Service Levels and Service Credits*) requires Contoso to:

- Meet response and resolution SLAs per priority (P1–P4) at **95% compliance**.
- Meet experience KPIs: **First Contact Resolution ≥ 65%**, **CSAT ≥ 4.2**, **Reopen rate ≤ 5%**, **Backlog ≤ 60**.
- Pay **service credits** when P1 or P2 resolution compliance misses target.
- Issue the MSR report **24 hours before** the review meeting.

**It is Monday, 2 November 2026.** The October MSR is on **Thursday, 5 November**. October included a major store network outage (**INC-P1-1042**), and Fabrikam's CIO, **Laura Chen**, has just emailed her concerns ahead of the meeting.

---

## Persona

| | |
|---|---|
| **Name** | Anita Rao |
| **Role** | Service Delivery Manager, Contoso |
| **Responsible for** | SLA performance, client relationship and the MSR for the Fabrikam account |
| **Goal this week** | Issue an accurate, insightful October MSR report by Wednesday, run a constructive review on Thursday and lock in an improvement plan |
| **Works with** | Sam Lee (Service Desk Manager), Ravi Menon (Network Ops Lead), Laura Chen (Fabrikam CIO) |

---

## Pain points

| Pain point | Impact |
|---|---|
| **Manual data crunching** – ~1,500 ticket rows pivoted by hand to calculate SLA compliance, FCR, CSAT and reopen rates | 4–6 hours per month; formula errors creep into client-facing numbers |
| **Information is scattered** – contract, last month's action log, major incident report and client emails live in different places | Key context (e.g. an overdue action that *caused* an incident) is missed |
| **Reporting instead of insight** – most effort goes into producing numbers, not explaining them | Reviews feel defensive; improvement opportunities go unnoticed |
| **Inconsistent quality** – report and deck rebuilt each month, quality depends on the author | Client perception varies month to month |
| **Weak follow-through** – actions agreed in the meeting live in someone's notes | Actions slip, eroding client trust (as with the password self-service guide) |

---

## Business benefits

| Benefit | How Copilot helps |
|---|---|
| ⏱️ **Hours → minutes** | Natural-language analysis of ticket data in Excel; first drafts of report and deck generated from source files |
| 🔍 **Grounded, traceable narrative** | Report content references the actual ticket data, contract and incident report |
| 💡 **Proactive insights** | Copilot surfaces patterns (shift-left opportunity, weekend CSAT gap, knowledge gaps) and suggests improvements |
| 🤝 **Better client conversations** | The CIO's concerns are addressed directly, with facts and a concrete plan |
| ✅ **Closed-loop governance** | Meeting actions, owners and dates are captured automatically and sent to the client the same day |

---

## Learning objectives

After completing this use case, learners will be able to:

1. Use **Copilot Chat** to synthesise information across multiple work files and emails into a briefing.
2. Use **Copilot in Excel** to analyse operational data, create PivotTables and charts, and identify trends and outliers.
3. Use **Copilot in Word** to draft a structured, client-ready report grounded in referenced files, and refine it iteratively.
4. Use **Copilot in PowerPoint** to create an executive presentation from a Word document.
5. Use **Copilot in Teams** to recap a meeting and extract actions, and **Copilot in Outlook** to draft a follow-up.
6. Apply **responsible AI** practices: verifying figures, keeping analysis at team level, and reviewing tone before sending to a client.

<img width="1920" height="1080" alt="Demo_Flow" src="https://github.com/user-attachments/assets/6978b038-2f12-45ca-bcf6-8266cc401e8a" />

---

## Prerequisites

- A **Microsoft 365 Copilot** licence (in-app Copilot in Word, Excel, PowerPoint, Teams and Outlook is required).
- **OneDrive for Business** or **SharePoint** to store the demo files (Copilot can only reference and analyse cloud-stored files).
- **Microsoft Teams** with meeting **recording and transcription** enabled (for Step 6).
- Desktop or web versions of Word, Excel, PowerPoint, Outlook and Teams.
- Optional: a second person (or learner group) for the role-play in Step 6.

---

## Package contents

```
copilot-uc1-service-desk-msr/
├── README.md                                   ← this file
├── data/
│   ├── Fabrikam_Tickets_Oct2026.xlsx           ← 1,505 October tickets (Excel table "Tickets")
│   ├── Fabrikam_Contoso_SLA_Schedule.docx      ← contract Schedule 3: SLAs, KPIs, service credits, MSR obligations
│   ├── MSR_September_2026_Actions.xlsx         ← September action log + September KPI baseline
│   ├── Major_Incident_Report_INC-P1-1042.docx  ← 14 Oct store WAN outage report
│   ├── Email_from_Fabrikam_CIO.eml             ← CIO's pre-meeting email (open in / import to Outlook)
│   ├── Email_from_Fabrikam_CIO.txt             ← same email as plain text (to paste/forward if needed)
│   └── MSR_Meeting_Roleplay_Script.docx        ← script for the recorded Teams review meeting

```

### Ticket data dictionary – `Fabrikam_Tickets_Oct2026.xlsx`

| Column | Description |
|---|---|
| Ticket ID | Unique ticket number (the major incident is `INC-P1-1042`) |
| Opened / Resolved | Date-time the ticket was created / resolved (blank if still open) |
| Priority | P1 (Critical) – P4 (Low) |
| Category / Subcategory | Service area, e.g. *Access & Identity / Password Reset* |
| Assignment Group | Resolver team, e.g. *Network Operations*, *Desktop Support L2* |
| Channel | Portal, Phone, Email, Chat |
| Shift | Weekday Day, Weekday Night, Weekend |
| Site | Head Office, Distribution Centre or Store number |
| Status | Closed, In Progress, Pending User |
| Response SLA Met / Resolution SLA Met | Y / N against the contract targets |
| First Contact Resolution | Y if resolved by L1 at first contact |
| Reopened | Y if reopened within 7 days |
| CSAT (1-5) | Customer satisfaction survey score (blank if no response) |

> All data is **fictional** and generated for training. Contoso and Fabrikam are fictitious companies.

---

## Environment setup

1. Create a folder in your **OneDrive** called `Contoso MSR Demo`.
2. Upload every file from the `data/` folder into it.
3. Open `Email_from_Fabrikam_CIO.eml` and either drag it into an Outlook folder **or** forward/paste its contents to your own mailbox so Copilot can find it (subject: *"Concerns ahead of the October service review"*).
4. Open `Fabrikam_Tickets_Oct2026.xlsx` once in Excel and confirm the data shows as a formatted **table** (Copilot in Excel works on tables).
5. For Step 6, schedule a Teams meeting called **"Fabrikam October MSR"** with the role-play participants, and make sure recording and transcription are allowed.
6. Allow ~10–15 minutes for new files to be indexed before using `/` to reference them in Copilot.

---

## Demo walkthrough

> 💡 In Copilot Chat, Word and PowerPoint, type **`/`** to reference a file by name. Prompts below show file references as `/FileName`.

### Step 1 – Prepare: build a briefing with Copilot Chat (≈5 min)

**Context:** Anita starts her week by understanding what she's walking into.

**App:** Microsoft 365 Copilot Chat (Work mode)

```text
Summarise /Fabrikam_Contoso_SLA_Schedule, /MSR_September_2026_Actions and
/Major_Incident_Report_INC-P1-1042. Give me:
1. The SLA and KPI targets in a table
2. The service credit rules
3. September actions that are still open or overdue
4. Key facts about the October major incident, including root cause
```

```text
Summarise the email from Laura Chen about the October service review.
What are her specific concerns and what does she expect to see on Thursday?
```

```text
Is there any link between the open September actions and the October
major incident?
```

**What to highlight:** Copilot connects the dots — the root cause of INC-P1-1042 (firmware not going through CAB) is the **overdue September action A-0904**, and the CIO is already chasing the **overdue password self-service guide (A-0901)**.

---

### Step 2 – Analyse: ticket performance with Copilot in Excel (≈10 min)

**Context:** Anita needs the numbers — fast and accurate.

**App:** Excel → open `Fabrikam_Tickets_Oct2026.xlsx` → **Copilot**

```text
Show ticket volume by Category and Subcategory, sorted highest to lowest,
and add a chart.
```

```text
Calculate Resolution SLA compliance % by Priority for Closed tickets.
Compare each against the 95% target.
```

```text
Which Assignment Groups had the most Resolution SLA breaches?
Show breaches by week of October.
```

```text
What is the average CSAT by Shift? Show it as a chart.
```

```text
Calculate the Reopened rate % by Subcategory for Closed tickets and
highlight any above 10%.
```

```text
What percentage of tickets are Password Reset or Account Unlock?
```

**What to highlight:** The five planted insights emerge (see [Expected outcomes](#expected-outcomes)). Show learners how to **check** one figure manually (e.g. filter Priority = P2) — Copilot accelerates analysis but the SDM owns the numbers.

---

### Step 3 – Interpret: insights and recommendations (≈5 min)

**App:** Copilot in Excel *or* Copilot Chat

```text
Based on this October ticket data, what are the top 5 insights a
Service Delivery Manager should present to the client? For each, suggest
a practical improvement action.
```

```text
Compare October with the September KPIs in /MSR_September_2026_Actions.
What improved and what got worse?
```

**What to highlight:** Copilot moves from *what happened* to *what to do*: self-service password reset (shift-left), firmware change control, weekend staffing/skills, knowledge-article refresh, and an FCR improvement plan.

---

### Step 4 – Write: draft the MSR report with Copilot in Word (≈8 min)

**App:** Word → new blank document → **Copilot → Draft with Copilot**

```text
Create a Monthly Service Review report from Contoso to Fabrikam Retail for
October 2026, using /Fabrikam_Tickets_Oct2026, /Fabrikam_Contoso_SLA_Schedule,
/MSR_September_2026_Actions and /Major_Incident_Report_INC-P1-1042.

Structure:
1. Executive summary
2. SLA and KPI performance vs contract targets (table)
3. Ticket volume and channel trends
4. Major incident summary – INC-P1-1042
5. Customer satisfaction
6. Status of September actions
7. Service credits
8. Service improvement plan for November
Use a professional, transparent tone suitable for a client CIO.
```

Refine iteratively:

```text
Rewrite the executive summary in 5 bullet points and acknowledge the CIO's
concerns about the 14 October outage directly.
```

```text
Add a table to the service improvement plan with Action, Owner, Due date
and Expected benefit.
```

Save as **`MSR_Report_Oct2026.docx`** in the same OneDrive folder.

**What to highlight:** Grounding in referenced files; iterative refinement; the SDM reviews every number against Step 2 before sending.

---

### Step 5 – Present: build the executive deck with Copilot in PowerPoint (≈5 min)

**App:** PowerPoint → new presentation (or your company template) → **Copilot**

```text
Create a presentation from /MSR_Report_Oct2026 for a 30-minute client
service review with the Fabrikam CIO. Keep it to about 10 slides.
```

```text
Add a slide titled "Shift-left: self-service password reset" that explains
the opportunity and expected impact.
```

```text
Add speaker notes to every slide.
```

**What to highlight:** From report to presentation in minutes; using an organisational template keeps the deck on-brand.

---

### Step 6 – Review & follow up: Copilot in Teams and Outlook (≈10 min)

**Context:** The MSR meeting happens; actions must not get lost.

1. Start the **"Fabrikam October MSR"** Teams meeting, **turn on recording and transcription**, and role-play `MSR_Meeting_Roleplay_Script.docx` (≈8 minutes).
2. After the meeting, open **Copilot in Teams** (meeting recap / chat) and ask:

```text
Summarise the key decisions from this meeting.
```

```text
List all action items with owner and due date in a table.
```

3. In **Outlook**, reply to Laura Chen's email and use **Draft with Copilot**:

```text
Thank Laura for the review, summarise the outcomes, confirm the service
credits for P1 and P2 will be reflected on the October invoice, and list
the agreed actions with owners and due dates. Mention that the MSR report
is attached. Keep it concise and professional.
```

Attach `MSR_Report_Oct2026.docx`, review, and send (to yourself in a demo).

**What to highlight:** The loop is closed — the CIO's original three asks (explanation, honest SLA view, concrete improvements) are all answered.

---

## Expected outcomes

Results generated by Copilot will vary in wording, but the analysis should surface these facts from the data:

| # | Insight | Evidence in the data |
|---|---|---|
| 1 | **P2 resolution SLA missed** due to the store network outage | P2 resolution compliance **85.2%** vs 95% target; Network Operations accounts for 17 breaches of 84 P2 tickets; breaches peak in the week of 12–18 Oct |
| 2 | **The P1 outage itself breached SLA** | INC-P1-1042 restored in 5 h 20 min vs 4 h target → P1 compliance **80.0%** (4/5) → service credits apply for **P1 and P2** |
| 3 | **Shift-left opportunity** | Password Reset + Account Unlock = **398 tickets (26.4%)** — the single largest demand driver |
| 4 | **Weekend experience gap** | CSAT **3.69** at weekends vs **4.44** on weekday days (overall 4.3) |
| 5 | **Knowledge gap in software installs** | Software Install reopen rate **15.0%** vs 3.5% overall |
| 6 | **FCR below target** | First contact resolution **58.1%** vs 65% target (September 61.2%) |
| 7 | **Channel shift to Portal** | Portal tickets up **19.1%** vs September; Phone down **12.2%** |

What stays healthy (useful for a balanced report): overall response SLA **97.6%**, overall resolution SLA **97.0%**, reopen rate **3.5%** (≤ 5%), and month-end backlog **49** (≤ 60).

---

## Real-world alignment

This scenario mirrors standard managed-services practice:

- **Contract-driven SLAs and service credits** by priority, as found in IT outsourcing agreements.
- **Monthly Service Reviews** as the core governance forum between provider and client.
- **ITSM / ITIL-aligned KPIs:** SLA compliance, First Contact Resolution, CSAT, reopen rate and backlog.
- **Ticket exports** structured like those from common ITSM platforms (ServiceNow, Jira Service Management, etc.).
- **Major incident management** with root cause, corrective and preventive actions.
- **Shift-left** (moving repetitive demand to self-service) and **change control (CAB)** as typical improvement levers.

The scenario is deliberately **geography-neutral** so trainers in any market can reuse it.

---

## Responsible AI considerations

- **Verify before you send.** Copilot can make mistakes; cross-check key figures (e.g. P2 compliance) against the source data before sharing with a client.
- **Team-level, not individual.** Keep analysis at queue, shift, category or assignment-group level. Do not use Copilot to rank or evaluate individual agents' performance.
- **Human ownership of commitments.** Contractual statements (service credits, due dates) must be confirmed by the accountable manager.
- **Data handling.** Use only data the user is authorised to access; Copilot respects existing Microsoft 365 permissions.
- **Tone review.** Review client-facing drafts for accuracy and tone, especially after a service failure.

---

## Extend this use case

| Next step | Idea |
|---|---|
| **Agent Builder (Use Case 1)** | Build a *Service Desk Insights* agent grounded on the SLA schedule, ticket exports and incident reports, so delivery managers and client stakeholders can ask "What was P2 compliance last month and why?" at any time. |
| **Copilot Studio** | Automate the monthly pipeline: on new ticket export, generate the KPI summary and draft the MSR for review. |
| **Learner challenge** | Ask learners to produce a *Service Improvement Plan* for weekend CSAT using Copilot, with measurable targets. |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| File doesn't appear when typing `/` | Ensure it is in OneDrive/SharePoint and allow time for indexing; try the full file name. |
| Copilot in Excel says it can't analyse the data | Confirm the data is an Excel **table** and the file is saved to OneDrive with AutoSave on. |
| Numbers differ slightly from the Expected outcomes | Check whether Copilot included open tickets in resolution SLA (use **Closed** only) or counted blank CSAT as zero. |
| No meeting recap in Teams | Recording/transcription must be on, and the recap can take a few minutes to appear after the meeting ends. |
| Copilot can't find the CIO email | Make sure it is in your mailbox (not only on disk); search by the subject line. |

---

**Author:** Neeraj Kumar, Microsoft Technical Trainer (IT/ITeS Industry Lead) · **Version:** 1.0 · **Date:** October 2026
