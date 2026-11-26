# Data Dictionary: Manufacturing Operations Performance & Risk Demo

This document explains every column in `Manufacturing_Operations_Performance_and_Risk.xlsx`.

> All records are **synthetic sample data** for training and demonstration only. No real company, plant, supplier or person is represented. All email addresses are fictional (`contoso.com`).

---

## Workbook at a Glance

| Sheet | What it holds | Rows | Grain |
|---|---|---|---|
| `Operations_Data` | Weekly production, equipment and delivery KPIs | 17 (includes 1 intentional duplicate) | One row per week × plant × line |
| `Quality_and_Supplier_Risk` | Weekly quality results and supplier performance | 16 | One row per week × plant × line |
| `Action_Register` | Management actions already proposed, with owners and due dates | 5 | One row per action |
| `Email_Distribution` | Recipients for the weekly leadership update | 6 | One row per person |

**Coverage:** 4 weeks (W40 to W43) × 2 plants (Plant A, Plant B) × 2 lines each.

| Plant | Line | Product Family | Key Supplier | Material |
|---|---|---|---|---|
| Plant A | Line 1 | Power Module | Supplier Nova | PCB |
| Plant A | Line 2 | Control Board | Supplier Delta | Housing |
| Plant B | Line 1 | Drive Train | Supplier Apex | Drive Shaft |
| Plant B | Line 2 | Sensor Pack | Supplier Orion | Sensors |

---

## `Operations_Data`

| Column | What it means | Unit / Format | How to read it |
|---|---|---|---|
| Week | Production week label | Text (e.g. `W42`) | Use to compare week-over-week trends |
| Plant | Manufacturing site | Text | — |
| Line | Production line within the plant | Text | One line builds one product family |
| Product Family | Product the line builds | Text | — |
| Opening WIP Units | Work-in-progress units on the line at the start of the week | Units | Context for how loaded the line is |
| Completed Units | Good units finished in the week (throughput) | Units | ↑ Higher is better |
| Scrap Units | Units discarded because they could not be used or reworked | Units | ↓ Lower is better |
| Downtime Minutes | Minutes the line was stopped (breakdowns, waiting for material, etc.) | Minutes | ↓ Lower is better |
| On-Time Delivery % | Share of customer orders shipped on the promised date | % (stored as decimal, 0.90 = 90%) | ↑ Higher is better; below 90% is a customer risk |
| Runtime Minutes | Minutes the line actually ran | Minutes | Runtime ÷ Planned = Availability |
| Planned Minutes | Minutes the line was scheduled to run | Minutes | 480 = one 8-hour shift |
| Availability | Share of planned time the line was actually running | % | ↑ Higher is better |
| Performance | How fast the line ran compared with its ideal speed | % | ↑ Higher is better |
| Quality | Share of produced units that were good | % | ↑ Higher is better |
| OEE | **Overall Equipment Effectiveness** = Availability × Performance × Quality. The single headline score for line health | % | ↑ Higher is better; ~85% is world class, below 60% signals serious loss |
| Cycle Time Sec | Average seconds to produce one unit | Seconds | ↓ Lower is better |
| Changeover Minutes | Minutes spent switching the line between products or setups | Minutes | ↓ Lower is better |
| Estimated Gross Margin USD | Estimated gross margin the line generated in the week (a contribution, **not** a loss) | USD | ↑ Higher is better; a drop shows the financial cost of disruption |

---

## `Quality_and_Supplier_Risk`

| Column | What it means | Unit / Format | How to read it |
|---|---|---|---|
| Week / Plant / Line / Product Family | Same keys as `Operations_Data`, used to link the two sheets | — | — |
| Supplier | Key supplier for the line | Text | Links quality problems to a source |
| Material Group | Material the supplier provides | Text | — |
| First Pass Yield Target | Target share of units that pass inspection the first time | % | Fixed at 98% |
| First Pass Yield Actual | Actual share of units that passed inspection the first time, without rework (**FPY**) | % | ↑ Higher is better; below target = quality problem |
| Scrap Rate | Scrapped units as a share of total units | % | ↓ Lower is better |
| Defect PPM | Defective parts per million units produced | Count | ↓ Lower is better |
| Customer Complaints | Complaints received from customers in the week | Count | ↓ Lower is better |
| Late PO Lines | Purchase-order lines the supplier delivered late | Count | ↓ Lower is better; drives material shortages |
| Expedite Cost USD | Extra money paid to rush late materials (e.g. air freight) | USD | ↓ Lower is better |
| Production Impact Hours | Production hours lost because of supplier issues | Hours | ↓ Lower is better |
| Containment Status | Whether defective material has been isolated so it cannot reach customers | Open / Closed | Open = issue still active |
| CAPA Status | **Corrective and Preventive Action**, the formal fix for the root cause | Open / In Progress / Closed | Closed = fix completed |
| Risk Rating | Quality team's overall risk rating for the line that week | Low / Medium / High / Critical | Critical needs leadership attention |

---

## `Action_Register`

| Column | What it means | Unit / Format |
|---|---|---|
| Action ID | Unique action reference | Text (e.g. `A-001`) |
| Week | Week the action was raised | Text |
| Priority | Business priority | High / Medium |
| Action | What will be done | Text |
| Owner Role | Function accountable for the action | Text |
| Owner Name | Person accountable | Text |
| Target Date | Due day, relative to the review week | Text (e.g. `W44 Wed`) |
| Status | Current progress | Planned (not started) / In Progress |
| Expected Impact | The business result the action should deliver | Text |

---

## `Email_Distribution`

| Column | What it means |
|---|---|
| Name | Recipient name |
| Role | Job title |
| Function | Department |
| Email | Fictional email address |
| Primary or CC | `Primary` = To line, `CC` = copied |

---

## Manufacturing Glossary

| Term | Plain-language meaning | Good direction |
|---|---|---|
| **OEE** (Overall Equipment Effectiveness) | One score for line health = Availability × Performance × Quality | ↑ Higher |
| **Throughput** | Good units produced in a period | ↑ Higher |
| **WIP** (Work in Progress) | Units started but not yet finished | Context |
| **Downtime** | Time the line was stopped | ↓ Lower |
| **Changeover** | Time spent switching a line to a different product or setup | ↓ Lower |
| **On-Time Delivery** | Share of customer orders shipped on the promised date | ↑ Higher |
| **FPY** (First Pass Yield) | Share of units that pass inspection the first time, without rework | ↑ Higher |
| **Scrap** | Units thrown away | ↓ Lower |
| **PPM** (Parts Per Million) | Defects per million units, a common quality measure | ↓ Lower |
| **PO** (Purchase Order) | Order placed with a supplier; a "PO line" is one item on it | — |
| **Expedite** | Paying extra to rush materials | ↓ Lower |
| **Containment** | Immediate step to stop bad material reaching customers | Closed = done |
| **CAPA** (Corrective and Preventive Action) | Formal process to fix the root cause and prevent recurrence | Closed = done |
