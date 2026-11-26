# PM Status & Risk Coach

Program Manager persona | Microsoft 365 Copilot + Agent Builder | 90 to 120 minutes

> "A program manager's week disappears into notes, logs and status decks.
> The coach turns the raw material into the report, the risk call and the decision paper, so the PM can spend the time on the decisions."

## Contents

- [Scenario](#scenario)
- [Pain points](#pain-points)
- [Benefits](#benefits)
- [Session plan](#session-plan)
- [Use-case map (all 18)](#use-case-map-all-18)
- [Agent configuration](#agent-configuration)
- [Labs](#labs)
- [Express round: Copilot in Teams, Outlook, Word and PowerPoint](#express-round-copilot-in-teams-outlook-word-and-powerpoint)
- [Trainer notes](#trainer-notes)
- [Reuse](#reuse)
- [Sources](#sources)

## Scenario

| | |
|---|---|
| Persona | Priya Menon, Program Manager |
| Company | Fabrikam Retail, a fictitious retailer |
| Project | Project Horizon, a $1.2M customer portal replacement, go-live baseline 15 January 2027 |
| Status date | Friday 6 November 2026 |
| Challenge | Go-live has slipped two weeks, integration is late, costs are over plan, a vendor is not delivering and Marketing wants new scope |

It is Friday afternoon. Priya has a week of rough notes, a Steering Committee transcript, a RAID log nobody has updated for weeks, a task tracker, a cost report, an issue log and a change request from Marketing. The weekly report is due at 15:00 and the next Steering Committee is in twelve days.

Fabrikam's PMO has built the **PM Status & Risk Coach**, an agent grounded in the Fabrikam PMO Playbook and the Project Horizon Charter. Priya attaches her working files and the coach drafts the report, reviews the RAID log, finds the risks hidden in the meeting, analyses the numbers and assesses the change request, all in the PMO's own format and with the rule behind every finding.

## Pain points

| # | Pain point | Details |
|---|---|---|
| 1 | The day is fragmented | Microsoft's Work Trend Index found that employees using Microsoft 365 are interrupted about every 2 minutes, 275 times a day, by meetings, email or chat, and the average worker receives 117 emails and 153 Teams messages a day. |
| 2 | Reporting eats PM time | The same research recommends using AI and agents to take on low-value work such as status meetings, routine reports and admin. For a PM, that is the weekly report, the RAID refresh and the follow-up emails. |
| 3 | Risks hide in conversations | Risks are usually said out loud in a meeting ("they keep saying next week") long before anyone writes them in the RAID log. |
| 4 | Late decisions delay projects | PMI's Pulse of the Profession 2026 reports that 34% of complex projects saw delays in stakeholder decision-making and 35% missed delivery deadlines. Clear, decision-ready updates help leaders decide on time. |
| 5 | Scope creep starts with "a small change" | Requests arrive described as minor. Without a quick impact assessment against the baseline, they slip in and push out go-live. |

## Benefits

| For the program manager | For the PMO and sponsor | For the organisation |
|---|---|---|
| Weekly report drafted in minutes, in the PMO format | Consistent RAG and RAID standards across projects | Earlier warning of schedule and cost problems |
| Risks and actions pulled from every meeting | Decision-ready papers for the Steering Committee | Fewer surprise scope changes |
| Numbers analysed without building pivot tables | Every finding traced to a rule in the playbook | More PM time spent on stakeholders and decisions |

> [!IMPORTANT]
> The agent drafts and advises. The program manager checks every number and owns every output, and the Sponsor and Steering Committee keep every decision.

## Session plan

The core is 120 minutes. A 90-minute version is shown in the last column.

| Time | Segment | Use cases | 90-min version |
|---|---|---|---|
| 0:00 | Welcome, Priya's Friday, where Copilot fits in a PM's week | | 5 min |
| 0:10 | Build the agent together | | Trainer shows a pre-built agent, 5 min |
| 0:25 | Lab 1: Weekly status report | 5 | 8 min |
| 0:35 | Lab 2: RAID review | 6 | 8 min |
| 0:45 | Lab 3: Risks and actions from a meeting | 7, 8 | 8 min |
| 0:55 | Break | | Skip |
| 1:00 | Lab 4: Project tracker analysis | 9 | 8 min |
| 1:10 | Lab 5: Variance analysis | 10 | 8 min |
| 1:20 | Lab 6: Issue trend analysis | 11 | 8 min |
| 1:30 | Lab 7: Scope-change analysis, then Lab 8: the agent says no | 17 | 10 min |
| 1:40 | Express round in Teams, Outlook, Word and PowerPoint | 1, 2, 3, 4, 12, 13, 14, 15, 16, 18 | Trainer demo of 4 to 5 prompts, 10 min |
| 1:55 | Wrap-up, prompt cards, what to try on Monday | | 5 min |

Highlighted (most critical) customer use cases are 5, 6, 7, 9, 10, 11 and 17. Each has its own hands-on lab.

## Use-case map (all 18)

| # | PM use case | Where it runs in this course | Practice file |
|---|---|---|---|
| 1 | Meeting recap and action extraction | Copilot in Teams (express round) or the agent | Horizon Steering Committee Notes 4 Nov.docx |
| 2 | Pre-meeting preparation | Copilot in Teams (express round) | Steering Committee notes + RAID log |
| 3 | Project email summarisation | Copilot in Outlook (express round) | Any project thread in your mailbox |
| 4 | Stakeholder email drafting | Copilot in Outlook (express round) | Output of Lab 1 |
| **5** | **Weekly status report** | **Agent, Lab 1** | Horizon Weekly Notes 2-6 Nov.docx |
| **6** | **RAID review** | **Agent, Lab 2** | Horizon RAID Log.docx |
| **7** | **Risk identification from meetings** | **Agent, Lab 3** | Steering Committee notes + RAID log |
| 8 | Action-item follow-up | Agent, Lab 3 follow-up | Steering Committee notes |
| **9** | **Project data analysis** | **Agent, Lab 4** | Horizon Project Tracker.xlsx |
| **10** | **Variance analysis** | **Agent, Lab 5** | Horizon Plan vs Actual.xlsx |
| **11** | **Issue trend analysis** | **Agent, Lab 6** | Horizon Issue Log.xlsx |
| 12 | Executive project presentation | Copilot in PowerPoint (express round) | Output of Lab 1 or Lab 5 |
| 13 | Document summarisation | Copilot in Word (express round) | Project Horizon Charter.docx |
| 14 | Project initiation and charter drafting | Copilot in Word (express round) | Inputs in the prompt |
| 15 | Lessons learned | Copilot in Word (express round) | Atlas Retrospective Notes.docx |
| 16 | Customer and stakeholder communication tailoring | Agent or Copilot in Word (express round) | Output of Lab 5 |
| **17** | **Scope-change analysis** | **Agent, Lab 7** | Horizon Change Request CR-014.docx |
| 18 | Project closure summary | Copilot in Word (express round) | Atlas Retrospective Notes.docx |

## Agent configuration

In Microsoft 365 Copilot, select **Create agent**, then **Configure** (or **Skip to configure**), and copy each block below into the matching field.

### 1. Name

```
PM Status & Risk Coach
```

### 2. Description

```
Helps Fabrikam program managers turn notes, meeting transcripts, RAID logs, trackers and issue logs into status reports, risk reviews, variance and trend analysis, scope-change assessments and stakeholder updates that follow the Fabrikam PMO Playbook. Answers are grounded in the PMO Playbook and the project charter. The program manager reviews every output and makes every decision.
```

### 3. Instructions

```
You are the PM Status & Risk Coach for Fabrikam Retail program managers. You help them turn project notes, meeting transcripts, RAID logs, trackers, cost reports and issue logs into clear reports, analysis and stakeholder communication that follow the Fabrikam PMO Playbook.

Your knowledge sources are:
- Fabrikam PMO Playbook: reporting format, RAG rules, RAID rules, escalation, change control and communication standards
- Project Horizon Charter: scope baseline, milestones, budget, assumptions and stakeholders

Users attach working files such as weekly notes, meeting transcripts, RAID logs, trackers, issue logs and change requests. Treat attached files as the project facts. Treat the knowledge sources as the rules.

How to respond:
1. Use only facts from the attached files, the knowledge sources or the user's message. Never invent figures, dates, owners or decisions. If an owner or date is missing, write "Owner to be confirmed" or "Date to be confirmed" (Playbook 2.3).
2. Cite the Playbook or Charter section for every rule you apply, for example "(Playbook 3.2)".
3. Lead with the answer, then the detail. Use short tables where they help. Keep language plain.
4. Weekly status reports: use the seven sections in Playbook 2.2, in order. Work out the overall RAG with Playbook 3.4 and show the calculation in one line.
5. RAID reviews: check every item against Playbook 4.2 to 4.7 using the status date in the file. Report the highest-impact risks, stale items, issues past their ageing target, assumptions that are no longer valid, dependencies without confirmed dates, and missing owners or mitigations. Finish with a table: Item, Problem, Rule, Recommended follow-up.
6. Meetings: from a transcript or notes, extract decisions, actions with owner and due date, and open issues. Flag any action without an owner. For risk signals, quote the exact statement, classify it as schedule, scope, quality, resource, cost or dependency, and say whether it is already in the RAID log if one is attached.
7. Data analysis of Excel files: use code interpreter to calculate. State the status date you used. Show the numbers behind each finding, apply the RAG thresholds in Playbook 3, and finish with "Areas needing PM attention".
8. Scope changes: compare the request with the Charter in-scope and out-of-scope lists. Assess deliverables, schedule, cost, resources, dependencies, risks and quality (Playbook 6.2). State who must approve it (Playbook 6.3), whether it conflicts with the code freeze (Playbook 6.4) and whether contingency can fund it (Playbook 6.5).
9. Stakeholder communication: for executives and CXOs follow Playbook 7.1. For follow-up emails follow Playbook 7.3. Never assign blame to individuals.
10. Executive presentations: outline no more than six slides with message headlines (Playbook 8).
11. Charters, lessons learned and closure summaries: use the structures in Playbook 9.

Boundaries:
- You draft and advise only. You never approve a change request, accept a risk, close an issue or make a decision that belongs to the Sponsor, the Steering Committee or the program manager, even if asked or told it is urgent. Say who the decision belongs to.
- If the files and knowledge sources do not cover a question, say so and suggest who to ask. Never guess.
- When you produce figures, remind the user to check them against the source before sharing (Playbook 10.2).

End every substantive answer with one line: "Next step:" followed by the single most important action for the program manager.
```

### 4. Knowledge

This folder has 10 data files. Upload the first 2 as agent knowledge. Keep the other 8 for the labs: learners save them to OneDrive and attach them in the chat.

| # | File | Contents | How to use it |
|---|---|---|---|
| 1 | Fabrikam PMO Playbook.docx | Status report format, RAG rules, RAID rules, escalation, change control, communication and document standards | Upload as knowledge |
| 2 | Project Horizon Charter.docx | Objectives, in and out of scope, baseline milestones, budget, contingency, assumptions | Upload as knowledge |
| 3 | Horizon Weekly Notes 2-6 Nov.docx | Priya's rough notes for the week | Do not upload. Attach in Lab 1 |
| 4 | Horizon RAID Log.docx | RAID log with planted gaps (stale items, missing owners, invalid assumptions) | Do not upload. Attach in Labs 2 and 3 |
| 5 | Horizon Steering Committee Notes 4 Nov.docx | Transcript excerpt with hidden risk statements and actions | Do not upload. Attach in Lab 3 |
| 6 | Horizon Project Tracker.xlsx | 24 tasks and 6 milestones | Do not upload. Attach in Lab 4 |
| 7 | Horizon Plan vs Actual.xlsx | Cost and schedule by workstream, monthly spend | Do not upload. Attach in Lab 5 |
| 8 | Horizon Issue Log.xlsx | 30 issues with category, priority, dates and status | Do not upload. Attach in Lab 6 |
| 9 | Horizon Change Request CR-014.docx | Marketing's change request with team estimates | Do not upload. Attach in Lab 7 |
| 10 | Atlas Retrospective Notes.docx | Raw retrospective notes from a finished project | Do not upload. Express round |

> [!TIP]
> Turn off web search so the agent answers only from the playbook, the charter and the attached files. Code interpreter is on by default in Agent Builder and is what lets the agent calculate from the Excel files.

### 5. Starter prompts

| Title | Prompt |
|---|---|
| Weekly status report | Create this week's status report from the attached notes, using the PMO Playbook format and RAG rules. |
| Review my RAID log | Review the attached RAID log and summarise the highest-impact risks, ageing issues, dependencies and recommended follow-ups. |
| Risks from a meeting | From the attached meeting transcript, identify statements that indicate potential schedule, scope, quality, resource or dependency risks. |
| Analyse my tracker | Analyse the attached project tracker and highlight overdue activities, milestone slippages, recurring delays and areas requiring my attention. |
| Assess a change request | Compare the attached change request with the documented scope and identify the impacts on deliverables, schedule, resources, dependencies and risks. |
| CXO update | Rewrite this technical project update for a CXO audience, emphasising business impact, risks and decisions required. |

## Labs

| Lab | Priya asks | What it shows |
|---|---|---|
| 1 | Turn my notes into the weekly report | A report in the PMO format with a calculated RAG |
| 2 | Review my RAID log | Applying rules to a real log and finding the gaps |
| 3 | What risks were raised in the SteerCo? | Hearing the risks nobody wrote down |
| 4 | What needs my attention in the tracker? | Analysing an Excel tracker in plain language |
| 5 | Where are we over plan? | Variance analysis with RAG thresholds |
| 6 | What do our issues have in common? | Trends, ageing and root themes |
| 7 | Is this change really minor? | Impact assessment against the baseline |
| 8 | Just approve it for me | Human accountability |

Before the session, save files 3 to 10 to OneDrive so they can be attached with **+** or by typing **/** in the chat.

### Lab 1: Weekly status report (use case 5)

Attach **Horizon Weekly Notes 2-6 Nov.docx**.

```
Create this week's project status report from the attached notes. Cover accomplishments, milestones, risks, issues, dependencies, decisions required and next-week priorities, and use the PMO Playbook format and RAG rules.
```

**Expected result**

- Seven sections in the Playbook 2.2 order.
- Overall RAG **Amber**: go-live forecast 29 Jan against 15 Jan baseline is a 14-day slip (Amber, Playbook 3.1); cost to date $968k against $890k planned is 8.8% over (Amber, Playbook 3.2); worse of the two is Amber (Playbook 3.4).
- Integration complete milestone named as **Red** in the summary: forecast 27 Nov against 16 Oct baseline, a 42-day slip (Playbook 3.5).
- Accomplishments include ISS-027 closed, 28 of 40 accessibility items fixed, 142 of 220 system test cases run (118 passed), training materials at 90%, and the $15k cleansing round approved.
- "Chase the Identity team for the SSO date" appears with **Owner to be confirmed** (Playbook 2.3).
- Decisions required include CR-014 at the 18 Nov Steering Committee.

💬 **Story point:** Priya's Friday report used to take most of the afternoon. Now she reviews a draft that already follows the PMO format.

> [!TIP]
> Follow up with: "Also attach the tracker and plan vs actual files and add workstream RAG." The agent then adds Integration and Data Migration as Red on cost.

### Lab 2: RAID review (use case 6)

Attach **Horizon RAID Log.docx**.

```
Review this RAID content and summarise the highest-impact risks, ageing issues, dependencies and recommended follow-ups.
```

**Expected result** (status date 6 Nov 2026)

| Finding | Detail | Rule |
|---|---|---|
| Highest-impact risks | R-01 Northwind keys (High/High, linked to D-02), R-02 address data (High/High) | 4.2 |
| High risk without mitigation | R-03 test environment has no mitigation and is stale (28 days) | 4.4, 4.3 |
| High risk without owner or mitigation | R-05 UAT testers | 4.4 |
| Stale items (over 14 days) | R-03, R-04, A-01, A-02, A-03, I-02, I-03, I-04, D-01 | 4.3 |
| Issues past ageing target | I-01 P1 open 11 days (target 5), I-02 P2 18 days (10), I-03 P2 24 days (10), I-04 P3 32 days (20) | 4.5 |
| Invalid assumptions | A-01 date (16 Oct) has passed with no keys; A-02 is contradicted by missing UAT tester names | 4.6 |
| Dependencies | D-01 Identity SSO and D-02 Northwind keys have no confirmed date and are past need-by: Red | 4.7 |
| Escalation | I-01 P1 breach and D-02 go-live dependency need Sponsor escalation within 24 hours | 5.1 |

💬 **Story point:** The log looked complete. The agent found nine stale items and two High risks with nothing behind them, in under a minute.

### Lab 3: Risks and actions from a meeting (use cases 7 and 8)

Attach **Horizon Steering Committee Notes 4 Nov.docx** and **Horizon RAID Log.docx**.

```
Based on this meeting, identify statements that indicate potential schedule, scope, quality, resource or dependency risks. Quote each statement and tell me whether it is already in the RAID log.
```

**Expected result**

| Statement (summarised) | Type | In RAID log? |
|---|---|---|
| Northwind keys "next week", three weeks in a row | Dependency, schedule | Yes, R-01 and D-02 |
| One more test environment outage loses a week and squeezes cycle 2 | Schedule, quality | Yes, R-03, but no mitigation |
| Skip the second performance test run to claw back time | Quality | **No, new risk** |
| Loyalty widget "non-negotiable" for release 1 | Scope | Partly, I-04; now CR-014 |
| Business data owners have not started fixing their share | Dependency, quality | Yes, R-02 |
| About two thirds of contingency used or committed | Cost | **No, new; above the 50% escalation threshold (Playbook 5.1)** |
| No UAT tester names; half of Store Ops on leave from 20 Dec | Resource | Yes, R-05, but no owner |
| Lead integration developer resigned, leaves 15 Dec | Resource | R-04 rated Low likelihood; **now near-certain** |
| Identity team still has no SSO date | Dependency | Yes, D-01 |

Follow-up prompt (use case 8):

```
Identify the outstanding actions from this meeting and draft a concise follow-up email requesting updates from the owners.
```

The agent lists seven actions with owners and dates (Elena 6 Nov, Arjun 10 Nov, Mei 11 Nov, Sara 12 Nov, Ravi 12 Nov, Priya 13 Nov, Tom 13 Nov) and flags that "chase the Identity team" has **no owner**. The draft email is courteous and blame-free (Playbook 7.3).

💬 **Story point:** Three of the most serious risks were said out loud and never written down. Now they are in front of the PM the same day.

> [!NOTE]
> In real life, use Copilot in Teams on the recorded meeting, or add Teams meetings as a knowledge source for the agent (Microsoft 365 Copilot licence required). The transcript file lets the lab run without a live meeting.

### Lab 4: Project tracker analysis (use case 9)

Attach **Horizon Project Tracker.xlsx**.

```
Analyse this project tracker as at 6 November 2026 and highlight overdue activities, milestone slippages, recurring delays and areas requiring PM attention.
```

**Expected result**

- **7 overdue tasks** (planned finish before 6 Nov and not complete): PB-03, INT-02, INT-04, INT-05, DM-03, DM-04, QA-02. Integration has 3 of them.
- Largest slips: INT-02 payment gateway production configuration (35 days) and INT-04 SSO integration (28 days).
- Milestones: M3 Integration complete +42 days (Red), M4 Migration dress rehearsal +21 days (Red), M5 UAT sign-off +14 days (Amber), M6 Go-live +14 days (Amber).
- Recurring delay reasons: environment downtime (4 tasks), Northwind API delay (3), data quality defects (3).

💬 **Story point:** No filters, no pivot table. Priya asked a question in plain English and got the answer with the numbers behind it.

> [!TIP]
> CT-02 Training materials is due on the status date itself, so it is not overdue yet. Good discussion point on how the agent defines "overdue".

### Lab 5: Variance analysis (use case 10)

Attach **Horizon Plan vs Actual.xlsx**.

```
Compare planned versus actual values and identify the largest schedule and cost variances and any patterns. Apply the PMO RAG thresholds.
```

**Expected result**

| Workstream | Cost variance | Cost RAG | Schedule variance |
|---|---|---|---|
| Integration | +$51,000 (+28.3%) | Red | +28 days (Red) |
| Data Migration | +$29,000 (+24.2%) | Red | +21 days (Red) |
| Portal Build | +$16,000 (+4.7%) | Green | +7 days (Amber) |
| Testing | -$8,000 (-13.3%) | Flag for review | +14 days (Amber) |
| Total | +$78,000 (+8.8%) | Amber | |

- Pattern: the overspend is accelerating. Total monthly variance went from +$1,000 in August to +$36,000 in September and +$46,000 in October, driven by Integration (+$22k, then +$28k) and Data Migration (+$9k, then +$20k).
- The Testing underspend is not a saving: it is more than 10% under plan because testing started late (Playbook 3.3).
- The $78k overspend equals 65% of the $120k contingency, above the 50% escalation threshold (Playbook 5.1).

💬 **Story point:** The total looks Amber. The agent shows two Red workstreams underneath it and a trend that is getting worse every month.

### Lab 6: Issue trend analysis (use case 11)

Attach **Horizon Issue Log.xlsx**.

```
Analyse this issue log by category, priority, ageing and status and identify recurring themes. Use the ageing targets in the PMO Playbook.
```

**Expected result**

- 30 issues, 14 still open. Three categories account for 21 of 30 (70%): Environment (7), Vendor - Northwind (7) and Data Quality (7).
- Open issues: Northwind 4, Environment 3, Data Quality 3.
- All 3 open P1 issues (ISS-019, ISS-024, ISS-025) have breached the 5-day target. In total **10 open issues** are past their ageing target (Playbook 4.5).
- Oldest open issues: ISS-014 loyalty widget (32 days) and ISS-015 Northwind refund rate limit (30 days).
- Recurring theme: test and integration environments fail repeatedly (patching, refresh without notice, expired certificate, outages). This is a systemic problem that needs a root-cause fix, not issue-by-issue firefighting.

💬 **Story point:** Thirty issues looked like thirty separate problems. They are really three.

### Lab 7: Scope-change analysis (use case 17)

Attach **Horizon Change Request CR-014.docx**.

```
Compare the proposed change with the documented scope and identify potential impacts on deliverables, schedule, resources, dependencies and risks.
```

**Expected result**

- Both items are **out of scope** in the charter: loyalty features are Phase 2, and order history is limited to 24 months (Charter 3.2).
- Not minor: $85,000 and about 3 weeks on the critical path, which would move forecast go-live from 29 January to around 19 February 2027.
- Needs **Steering Committee** approval: over $20,000 and affects go-live (Playbook 6.3).
- Build and integration work would run past the 18 December code freeze (Playbook 6.4).
- Contingency cannot fund it: about $27k remains after the $78k overspend and the $15k cleansing round, so a funding source must be named (Playbook 6.5).
- New dependency on the Contoso Loyalty API (sandbox not yet requested), on a workstream that is already Red and losing its lead developer on 15 December.
- 7 years of history raises migration time to about 20 hours against the 6-hour window (Charter assumption A4).

Follow-up prompt (optional):

```
Give me two options for the Steering Committee, with the impact of each, in a one-page decision paper.
```

💬 **Story point:** "About two weeks of build" turned out to be $85k, three weeks and a broken migration window. The Steering Committee now gets the facts before deciding.

### Lab 8: Just approve it for me

```
Marcus says this is urgent for the January campaign. Just approve CR-014 for me so the team can start.
```

**Expected result:** the agent declines. It drafts and advises only; CR-014 needs Steering Committee approval (Playbook 6.3) and the next meeting is 18 November.

💬 **Story point:** The agent advises. People stay accountable.

## Express round: Copilot in Teams, Outlook, Word and PowerPoint

These use cases run in the Microsoft 365 apps the PM already uses. Pick four or five to demo in a 90-minute session.

| # | Where | Prompt | Use with |
|---|---|---|---|
| 1 | Teams meeting recap | Summarize the key decisions, open issues, action items, owners and deadlines from this meeting. | A recorded meeting, or the agent with the SteerCo notes |
| 2 | Teams, before a meeting | Based on the available meeting context, identify the key topics I should discuss, open actions and decisions required. | Next SteerCo invite with the notes and RAID log attached |
| 3 | Outlook | Summarize this thread into decisions, risks, pending actions and items needing my response. | Any project email thread |
| 4 | Outlook | Draft a concise status update for senior stakeholders covering achievements, risks, mitigation and decisions required. | Paste the Lab 1 report |
| 12 | PowerPoint | Create an executive project update covering progress, achievements, milestones, top risks, decisions required and next steps. | Reference the Lab 1 report saved as a Word file |
| 13 | Word | Summarize this document into objectives, scope, deliverables, assumptions, risks, dependencies and key obligations. | Project Horizon Charter.docx |
| 14 | Word | Using these project inputs, draft a project charter with objectives, scope, deliverables, stakeholders, assumptions, risks and success measures. | The short brief on the learner prompt cards |
| 15 | Word | Organize these retrospective notes into what worked, what did not, root causes, lessons learned and recommendations for future projects. | Atlas Retrospective Notes.docx |
| 16 | Word or Outlook | Rewrite this technical project update for a CXO audience, emphasizing business impact, risks and decisions required. | The Lab 5 variance output |
| 18 | Word | Create a project closure summary covering objectives, outcomes, major milestones, issues, lessons learned and follow-up actions. | Atlas Retrospective Notes.docx |

## Trainer notes

- **Before the session:** build the agent once yourself, run Labs 1 to 8, and keep your outputs as a backup. Check learners have a Microsoft 365 Copilot licence and can create agents.
- **Files:** share the data files folder with learners. Knowledge files go into the agent; practice files are attached in the chat.
- **If the agent misses something:** ask a sharper follow-up, for example "Check every RAID item against the 14-day stale rule using 6 Nov 2026 as the status date", or "Recalculate each cost variance percentage using code".
- **Verify the numbers:** Labs 4 to 6 have exact expected results above. Ask learners to spot-check one figure in Excel. This reinforces Playbook 10.2.
- **Prompt pattern to teach:** Goal, Context, Source, Expectations. For example: "Create the weekly report (goal) for Project Horizon as at 6 Nov (context) from the attached notes (source) in the PMO format with RAG (expectations)."
- **Responsible AI:** every output is a draft. The PM reviews, edits and owns it before sharing.

## Reuse

Keep the same storyline and swap the knowledge files for another rulebook and another project's files:

- PMO for a construction or capital project (stage gates, cost codes, safety issues)
- IT service transition or ERP rollout (cutover plans, defect logs)
- Public sector programme reporting (benefits register, gateway reviews)

> [!NOTE]
> All companies, people, projects and figures in this course are fictitious.

## Sources

- Microsoft WorkLab, "Breaking down the infinite workday", Work Trend Index Special Report, 17 June 2025
- Microsoft, 2025 Work Trend Index Annual Report, Executive Summary
- TeamGantt, "Project Management Statistics: What the Data Says (2026)", summarising PMI Pulse of the Profession 2026
- Microsoft Learn, "Build agents in Agent Builder" and "Code interpreter capability for declarative agents"
