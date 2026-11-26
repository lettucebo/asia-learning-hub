# Manufacturing Line Downtime Response Agent

| | |
|---|---|
| **Industry** | Manufacturing & Mobility |
| **Product** | Microsoft Copilot Studio |
| **Customer (fictitious)** | Contoso Manufacturing – packaging plant |
| **Builds on** | Agent Builder use case *Production Downtime Resolution Assistant* |
| **Setup** | See [setup.md](setup.md) – import the solution, then complete the post-import steps |

---

## Scenario

A packaging line at Contoso Manufacturing (Line P-204) keeps stopping on the night shift. In the Agent Builder use case, the plant supervisor could get a downtime briefing – but the team still had to raise tickets, check spare parts, warn procurement and notify the maintenance lead by hand.

The **Line Downtime Response Agent** closes that gap. In one conversation it briefs the supervisor, checks whether the spare parts for the fix are available (and whether the supplier is at risk), raises a corrective work order after confirmation, alerts the maintenance lead, and routes any safety issue straight to EHS.

---

## Pain Points and Benefits

| Pain point | Benefit |
|---|---|
| Briefings tell people what to do, but tickets, alerts and parts checks are still manual and logged hours later | Work orders and alerts are raised from the conversation, with a human confirmation step |
| Maintenance sees the failure, procurement sees the late PO – nobody links the two | Spare-part shortages are linked automatically to open POs and supplier performance |
| Safety-related stoppages are escalated differently by each shift | A fixed Safety Escalation topic always routes to EHS and never gives troubleshooting advice |
| Work-order quality varies (missing machine, priority or action) | Every work order follows the same structure defined in the plant SOP |
| A personal agent is hard to share and govern across plants | Published to Teams and Microsoft 365 Copilot as a governed, shareable agent |

---

## Agent Components

| Component | Type | Purpose |
|---|---|---|
| Production Downtime Demo Pack (4 files) | Knowledge | Alarms, maintenance tickets, quality defects and spare-parts inventory for Line P-204 |
| Supplier Risk Demo Pack (4 files) | Knowledge | Open POs, supplier on-time delivery, incoming rejections and material criticality |
| Downtime Response SOP | Knowledge | Priority definitions (P1–P3), escalation rules and the work-order standard |
| Create corrective work order | Tool (Excel Online) | Adds a row to the *WorkOrders* table in `Corrective_Work_Orders.xlsx` after the user confirms |
| Send downtime alert | Tool (Outlook) | Emails a structured alert to the maintenance lead after the user confirms |
| Safety Escalation | Topic | Deterministic response for injury, fire, smoke, electrical or LOTO issues – stop, escalate to EHS, no troubleshooting |

All data in `data-files/` is fictional.

---

## Demo

### Demo overview

Act as the Line P-204 supervisor preparing for the morning production review. Move from **insight** (briefing, root cause, supply risk) to **action** (work order, alert), then show the **safety guardrail**. Open the activity map in the test pane to show which knowledge source, tool or topic the agent chose at each step. Allow about 10 minutes.

### Demo steps

| # | Prompt | What to highlight |
|---|---|---|
| 1 | *Prepare me for today's production review for Line P-204. Include downtime summary, likely root causes, repeated alarm patterns, open maintenance actions, quality impact and safety concerns. Flag any missing information.* | Grounded briefing that follows the SOP headings |
| 2 | *For the top root cause, which spare parts are needed? Are they in stock? If not, check open purchase orders and supplier performance and tell me the supply risk.* | Reasoning across both data packs – inventory linked to POs and supplier OTD |
| 3 | *Create a corrective work order for this issue with the right priority.* | Agent summarises and asks for confirmation, then writes to the Excel tracker |
| 4 | *Send an alert to the maintenance lead about this work order.* | Second tool with confirmation; email arrives in the inbox |
| 5 | *There is smoke coming from the FM-12 motor, how do I reset it?* | Safety Escalation topic takes over; no reset steps are given |

### Demo outcome

- A production-review briefing grounded in plant data, including the supply risk for the parts needed
- A new row in the *WorkOrders* table of `Corrective_Work_Orders.xlsx`
- An alert email to the maintenance lead
- Proof that safety events are always escalated to EHS, not troubleshot
