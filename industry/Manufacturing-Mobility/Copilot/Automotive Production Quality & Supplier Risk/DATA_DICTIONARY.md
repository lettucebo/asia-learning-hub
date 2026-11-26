# Data Dictionary: Automotive Production Quality & Supplier Risk

This document defines the columns in `Manufacturing_Operations_Performance_and_Risk.xlsx`.

> **Synthetic training data.** Contoso, the plants, people, suppliers, records, figures and events in this demonstration are fictional. The addresses are examples; do not send messages to them. This is not a real quality, safety, recall or engineering assessment.

## Workbook at a glance

| Worksheet | Excel table | Rows before cleanup | Grain |
|---|---|---:|---|
| `Operations_Data` | `OperationsData` | 17, including one intentional duplicate | Week × plant × line |
| `Quality_and_Supplier_Risk` | `QualitySupplierRisk` | 16 | Week × plant × line |
| `Action_Register` | `ActionRegister` | 5 | Management action |
| `Email_Distribution` | `EmailDistribution` | 6 | Recipient |

Coverage is 2026 weeks W40–W43, two plants and two lines per plant. After cleaning, each operational and quality table has one row per week, plant and line. Join them on **Week, Plant and Line** after normalizing the labels. Product Family is an additional consistency check, not a substitute for the join key.

| Plant | Line | Product family | Key supplier | Critical purchased material |
|---|---|---|---|---|
| Plant A | Line 1 | EV Battery Cooling Assembly | Supplier Vale | Battery coolant connector |
| Plant A | Line 2 | EV Inverter Assembly | Supplier Meridian | Power semiconductor |
| Plant B | Line 1 | Electric Drive Assembly | Supplier Crest | Drive bearing |
| Plant B | Line 2 | Brake Control Assembly | Supplier Orion | Brake valve body |

The lines make automotive assemblies for Contoso's downstream vehicle plants, not completed vehicles. Counts of finished assemblies, incoming components, purchase-order lines and complaints are different populations and must not be added together.

## Measurement conventions

- Each line has **4,800 planned minutes per week**, representing two eight-hour shifts on five days. Runtime and downtime are measured against that same scheduled window: `Runtime Minutes + Downtime Minutes = Planned Minutes`. Changeover is included within downtime, not additional to it.
- The illustrative ideal cycle time is **120 seconds per assembly** for every line. This is a simplified demo assumption, not an industry benchmark. Actual cycle time is runtime in seconds divided by total finished outcomes (`Completed Units + Scrap Units`).
- Completed units are good assemblies after any rework; scrap units are assemblies discarded in the week. The two counts represent completed production outcomes. Opening WIP is a snapshot; new work enters during the week, so opening WIP alone is not a throughput constraint.
- Quality in the OEE calculation is `Completed Units / (Completed Units + Scrap Units)`. First pass yield (FPY) is a separate inspection measure: units passing without rework divided by units presented for the first time. Do not equate FPY with OEE Quality.
- `Defect PPM` describes defects found in inspected **incoming critical components**, per million inspected components. `Scrap Rate` describes finished assembly outcomes. Their denominators and inspection stages differ; they are not interchangeable, and an association does not establish cause.
- `Production Impact Hours` is the supplier-attributed portion of the line's downtime, not an extra time loss to add to downtime. `Estimated Gross Margin USD` is a synthetic weekly contribution estimate, not a loss or a proven effect of a specific incident. The workbook contains no itemized margin bridge.
- On-time delivery is a percentage of customer order lines shipped on the promised date. The workbook does not provide the order-line denominators, so a simple average across lines is **unweighted**, not a company-wide order-weighted rate.

## `Operations_Data`

| Column | Meaning | Unit / interpretation |
|---|---|---|
| Week | ISO production week in 2026 | Text, `W40`–`W43` |
| Plant | Assembly location | Text; one intentional `Plant-A` variant |
| Line | Line within the plant | Text |
| Product Family | Automotive assembly produced on the line | Text; one intentional `E-Drive Assembly` variant |
| Opening WIP Units | Assemblies already in process at the start of the week | Assemblies |
| Completed Units | Good assemblies completed in the week, including those successfully reworked | Assemblies |
| Scrap Units | Assemblies discarded in the week | Assemblies |
| Downtime Minutes | Scheduled minutes when the line was stopped | Minutes; includes changeovers |
| On-Time Delivery % | Share of customer order lines shipped by the promised date | Decimal percentage; higher is better |
| Runtime Minutes | Scheduled time when the line was running | Minutes |
| Planned Minutes | Scheduled line time | Minutes; 4,800 per line-week in this sample |
| Availability | Runtime divided by planned time | Formula; percentage |
| Performance | Total finished outcomes × 120 ideal seconds ÷ runtime seconds | Formula; percentage |
| Quality | Good completed units ÷ total finished outcomes | Formula; percentage |
| OEE | Availability × Performance × Quality | Formula; percentage |
| Cycle Time Sec | Runtime seconds ÷ total finished outcomes | Formula; seconds per assembly |
| Changeover Minutes | Time spent changing the line's setup | Minutes; subset of downtime |
| Estimated Gross Margin USD | Weekly estimated gross contribution from the line | USD; an estimate, not a loss |

The W43 Plant B Line 2 record appears twice with the same displayed values. Its calculated cells use their own row references. The demonstration removes only the second occurrence.

## `Quality_and_Supplier_Risk`

| Column | Meaning | Unit / interpretation |
|---|---|---|
| Week / Plant / Line / Product Family | Identifiers corresponding to the operations sheet | Text; this sheet contains one `Plant-A` and one `E-Drive Assembly` variant |
| Supplier | Fictional supplier of the line's critical material | Text |
| Material Group | Critical purchased component monitored for that line | Text |
| First Pass Yield Target | Desired share passing first inspection without rework | Decimal percentage; 98% illustrative target |
| First Pass Yield Actual | Share passing first inspection without rework | Decimal percentage |
| Scrap Rate | Scrap units ÷ completed plus scrap units for the matching week, plant and line in `OperationsData` | Formula; decimal percentage; the plant label is normalized for the intentional variant |
| Defect PPM | Defective incoming critical components per million inspected | PPM; not finished-assembly scrap |
| Customer Complaints | Recorded complaints from downstream Contoso vehicle assembly plants | Count; not consumer warranty claims |
| Late PO Lines | Supplier purchase-order lines delivered late | Count |
| Expedite Cost USD | Extra cost of expediting the supplier's material that week | USD |
| Production Impact Hours | Supplier-attributed line downtime | Hours; already included in downtime |
| Containment Status | Whether suspect material remains subject to a controlled hold | Open / Closed; Open does not mean release was authorized |
| CAPA Status | Progress of corrective and preventive action | Open / In Progress / Closed |
| Risk Rating | Quality team's illustrative assessment for that line-week | Low / Medium / High / Critical; not the calculated operational risk category |

## `Action_Register`

| Column | Meaning |
|---|---|
| Action ID | Unique reference |
| Week | Week action was recorded |
| Priority | Management priority, High or Medium |
| Action | Proposed or ongoing response |
| Owner Role | Accountable function |
| Owner Name | Fictional accountable person |
| Target Date | Due day in ISO week 44 of 2026 |
| Status | Planned or In Progress |
| Expected Impact | Intended outcome, not a demonstrated result |

## `Email_Distribution`

| Column | Meaning |
|---|---|
| Name | Fictional recipient |
| Role | Job title |
| Function | Team |
| Email | Fictional example address; do not send |
| Primary or CC | Intended role in a draft only |

## Glossary

| Term | Meaning |
|---|---|
| **OEE** | Overall equipment effectiveness: availability × performance × quality. |
| **WIP** | Work in progress: assemblies started but not yet finished. |
| **FPY** | First pass yield: share passing inspection without rework. |
| **PPM** | Parts per million, here measured on inspected incoming components. |
| **PO line** | An individual item on a supplier purchase order. |
| **Containment** | A controlled hold or other process that prevents suspect material from being used before authorized disposition. |
| **CAPA** | Corrective and preventive action; its status is not proof of an effective fix. |
