# Automotive Production Quality & Supplier Risk

Contoso is a fictional automobile manufacturer producing electric-vehicle assemblies for its downstream vehicle plants. Plant A makes battery cooling and inverter assemblies; Plant B makes electric drive and brake control assemblies. Each line depends on a critical purchased component, so incoming quality and delivery problems can affect production and the ability to supply the vehicle plants.

It is **Monday, 26 October 2026**, after week W43 has closed. The Operations Performance Manager must brief leaders at the **2 p.m. weekly production and risk review**. W42 was a difficult week, especially for Plant A's battery cooling line and Plant B's electric drive line. W43 output recovered, but the hold on Supplier Vale's suspect coolant connectors remains open and corrective work is not complete.

Leadership needs to know: *Did production recover? Which lines and suppliers need attention? What remains uncertain? What decisions are needed before the first W44 action is due?* The workbook brings together line output and equipment effectiveness, incoming quality, supplier delivery, open actions and a distribution list. The challenge is to turn these records into an evidence-based decision, not to assume that a statistical association proves a root cause.

> **Synthetic demonstration only.** Contoso, all suppliers, people, plants, figures and events are fictional. The example email addresses are not authorized recipients; **draft only, do not send**. This exercise is not a real vehicle safety, recall or engineering procedure.

## Pain points and demonstrated benefits

| Pain point | How Copilot can help | Business benefit |
|---|---|---|
| Operations, quality and supply-chain records arrive in one unfamiliar workbook | Explain sheets, coverage, keys and measures | Faster orientation before the review |
| Different source labels and a duplicate could distort totals or break joins | Identify and correct the specific issues before analysis | More trustworthy summaries |
| Verbal escalation rules are applied inconsistently | Express the rules as table formulas and explain the boundaries | Repeatable signals as new records are added |
| A recovered output number can hide an open supplier hold | Combine line trends, supplier indicators and action status | A clearer view of both improvement and remaining exposure |
| Findings must become a short report and an approval request | Draft a template-based Word report and an Outlook message from the data | A more useful leadership discussion |

## Demo journey

### Files

| File | Purpose |
|---|---|
| [DATA_DICTIONARY](DATA_DICTIONARY.md) | Definitions, joins, assumptions and trainer notes; not required as a Copilot prompt source |
| [Manufacturing_Operations_Performance_and_Risk](Manufacturing_Operations_Performance_and_Risk.xlsx) | Four tables: operations, quality and supplier risk, actions, and distribution |
| [Weekly_Operations_Report_Template](Weekly_Operations_Report_Template.docx) | Six-section leadership report template |

**Setup:** Use a working copy of the workbook in a writable location accessible to Microsoft 365 Copilot, such as an appropriately permissioned OneDrive or SharePoint location. Use licensed Excel, Word and Outlook capabilities available in your environment. Copilot experiences and file-reference controls vary; select or attach the named files using the interface available to you. Review and save the workbook after changes. All outputs require human verification; no action or email should be sent automatically.

The line-week data covers W40–W43. The workbook begins with intentional label variants and one duplicate. For measures, denominators, the ideal cycle-time assumption and the distinction between supplier incoming PPM and finished-assembly scrap, see the data dictionary. Weekly OEE and on-time delivery averages in this demo are **unweighted line averages**.

| Step | App | Copilot capability | Leadership question |
|---|---|---|---|
| 1. Understand | Excel | Summarize and explain | What data do I have? |
| 2. Prepare | Excel | Find and correct data issues | Can I trust the comparisons? |
| 3. Calculate | Excel | Turn rules into formulas | Which line-weeks need attention? |
| 4. Analyze | Excel | Trends, joins and dashboard | What changed and where is risk concentrated? |
| 5. Report | Word | Grounded drafting | What does leadership need to read? |
| 6. Communicate | Outlook | Audience-aware drafting | What decision is needed, and when? |

---

## 1. Understand the automotive dataset (Excel)

**Scenario.** The workbook arrived from the plant, quality and supply-chain teams. You need to understand it before deciding which issues to bring to the 2 p.m. meeting.

Open `Manufacturing_Operations_Performance_and_Risk.xlsx`.

**Prompt 1.1**

```text
I am Contoso's Operations Performance Manager preparing for a weekly automotive manufacturing review. Explain each sheet and its business purpose. Identify the week, plant and line keys used to connect operational and quality records. Distinguish the existing risk assessment from any calculated risk signal we might add later.
```

**Prompt 1.2**

```text
What weeks, plants, lines, product families and suppliers are represented? Identify three review priorities and flag possible data-quality issues without changing anything. Distinguish observations in the data from unverified explanations.
```

**Talking point:** Copilot can orient the manager to the data and the business question without presenting a suspected cause as a finding.

---

## 2. Prepare and validate the data (Excel)

**Scenario.** A naming variation can split one plant or product into two groups; an extra row can inflate output and cost. Identify the issues before correcting the source tables.

**Prompt 2.1**

```text
In Operations_Data and Quality_and_Supplier_Risk, find inconsistent Plant and Product Family labels that appear to describe the same entity. Show the worksheet, row, original value and proposed standard value. In Operations_Data, identify duplicate records by displayed values, even if equivalent formulas use different row references. Do not change data yet.
```

**Prompt 2.2**

```text
In both source tables, replace Plant-A with Plant A and E-Drive Assembly with Electric Drive Assembly. In Operations_Data, remove only the second of the duplicate W43 Plant B Line 2 rows, retaining the first.

Edit existing cells and rows in place, preserving the tables, formulas and formatting. Do not create a replacement sheet. Report the number of cells changed and rows removed; confirm the data-row count in each sheet and that Week, Plant and Line uniquely identify each line-week in each table.
```

**Verify before proceeding:** Four text cells should change and one operations row should be removed. Each data sheet should then contain 16 rows. The quality-sheet scrap formulas should still match operations records by week, plant and line. Save the cleaned workbook.

**Talking point:** A dashboard made before cleanup would double-count the W43 brake-control row. A join made before normalizing `Plant-A` would miss a matching line-week.

---

## 3. Create calculated signals (Excel)

**Scenario.** The Plant Head wants consistent escalation rules for every line-week. These are **illustrative demo thresholds**, not safety limits or industry standards.

**Prompt 3.1 — Operations_Data**

```text
Add a calculated column at the end of the OperationsData table named Operational Risk Category. Use a formula and apply the first matching rule in this order:

Critical: Downtime Minutes greater than 900 OR On-Time Delivery % less than 0.90.
High: Downtime Minutes at least 720 OR Scrap Units greater than 60.
Medium: Downtime Minutes at least 480 OR Scrap Units at least 40.
Low: all remaining rows.

Explain the formula and count Critical, High, Medium and Low rows by Week. Make it a table calculated column so it can extend to new rows. Do not change existing source values.
```

**Prompt 3.2 — Quality_and_Supplier_Risk**

```text
Add a calculated column at the end of the QualitySupplierRisk table named Quality Watch Flag. Return Watch when First Pass Yield Actual is less than 0.96 AND Scrap Rate is greater than 0.035; otherwise return Stable.

Explain the formula, count Watch rows by Week, and make it a table calculated column. Do not change existing source values.
```

**Verify:** In W42, Plant A Line 1 and Plant B Line 1 are Critical; the quality watch flag is also Watch for those two line-weeks. `Risk Rating` is the quality team's separate assessment and need not equal either new signal. Check the threshold boundaries, not just the labels.

**Talking point:** The manager has made the escalation logic explicit and repeatable rather than applying it differently for each plant.

---

## 4. Identify performance and supplier-risk drivers (Excel)

**Scenario.** The Operations Director asks: “Was the recovery real, which lines and suppliers need attention, and what is still open? Show me one page.”

**Prompt 4.1 — Operations_Data**

```text
Using the cleaned OperationsData table, create a Weekly_Trends sheet with:
- By Week: total Completed Units, total Downtime Minutes, average OEE and average On-Time Delivery %.
- OEE by Week for each Plant and Line.
- A line chart of average OEE by Week.

Use unweighted line averages. In three bullets, compare W41, W42 and W43 and identify the lines with the biggest W42 downtime. Do not change the source table.
```

**Prompt 4.2 — Operations_Data and Quality_and_Supplier_Risk**

```text
Create a Risk_Drivers sheet. Match the cleaned tables on Week, Plant and Line and list rows where Quality Watch Flag is Watch AND OEE is below 0.70. Show Week, Plant, Line, Product Family, Supplier, OEE, First Pass Yield Actual, Scrap Rate, Defect PPM, Operational Risk Category, Containment Status and CAPA Status.

Also summarize each supplier's total Late PO Lines, total Expedite Cost USD and total Production Impact Hours over W40–W43, sorted by expedite cost. Identify the two suppliers with the highest total expedite cost. Distinguish incoming-component PPM from finished-assembly scrap and avoid claiming either proves a root cause. Do not change source tables.
```

**Prompt 4.3 — executive dashboard**

```text
Create an Executive_Dashboard sheet from the cleaned OperationsData, QualitySupplierRisk and ActionRegister tables. Fit it on one page and include:
- Total Completed Units, total Downtime Minutes, average OEE and average Scrap Rate for W40–W43. Label the averages as unweighted.
- A table by Week with average OEE and average On-Time Delivery %. For this demo only, use OEE green at or above 0.70, amber from 0.60 to below 0.70, and red below 0.60; use delivery green at or above 0.95, amber from 0.90 to below 0.95, and red below 0.90.
- The three W42 rows with the most downtime, including their Operational Risk Category.
- The two suppliers with the highest total expedite costs.
- All High-priority actions, including owner, target date and status.
Do not modify the source tables.
```

**Prompt 4.4 — optional PivotTable**

```text
On a new Pivot_Plant_Product sheet, create a PivotTable from the cleaned OperationsData table. Put Plant and Product Family in rows, and sum Completed Units, Scrap Units, Downtime Minutes and Estimated Gross Margin USD. Include grand totals. Do not change the source table.
```

**Verify:** After deduplication, completed units are 6,900 in W40, 5,550 in W42 and 6,900 in W43. The W42 downtime leaders are Plant A Line 1, Plant B Line 1 and Plant A Line 2. Supplier Vale and Supplier Crest have the highest cumulative expedite costs. W43 improvement does not close Vale's containment or CAPA.

**Talking point:** The recovery is visible, but open containment and planned actions mean that the underlying issue is not yet demonstrated to be resolved.

---

## 5. Create the weekly leadership report (Word)

**Scenario.** Leadership expects a concise report before the review. The analyst must separate evidence and hypotheses and identify decisions rather than inventing a financial or engineering conclusion.

Save the cleaned and analyzed workbook. In Word, create a new report and select both `Weekly_Operations_Report_Template.docx` and `Manufacturing_Operations_Performance_and_Risk.xlsx` as sources using the available file-reference controls.

**Prompt 5.1 — new Word report**

```text
Using the selected Weekly_Operations_Report_Template.docx as the structure and the selected Manufacturing_Operations_Performance_and_Risk.xlsx as the only data source, draft the weekly report.

Header: Reporting Week 2026-W43; Prepared By Operations Performance Manager.

Use the six template sections in order:
1. Executive Summary.
2. Throughput and OEE Movements: compare W43 with W42 and the W40 baseline, including plant/line movements and estimated gross margin.
3. Quality and Supplier Risk Watchlist: include FPY, scrap, incoming defect PPM, containment and CAPA, and the two suppliers with the largest total expedite cost.
4. Top Root-Cause Hypotheses: provide three possible explanations supported by specific workbook evidence. Label them unverified; do not claim that correlation establishes causation.
5. Top 3 Management Actions: use the three High-priority Action_Register rows, including owner, due date, status and expected impact.
6. Leadership Approval Needed: identify the decisions implied by those actions and request a decision before the earliest due date.

Use only workbook facts. Explain that gross margin is an estimate, not a quantified incident loss. Do not invent an approval amount, a confirmed root cause, or a safety conclusion. Use concise headings and bullets.
```

Save the reviewed report as `Weekly_Operations_Report_W43.docx`.

**Prompt 5.2 — select the Executive Summary**

```text
Rewrite this section in about 150 words. Describe the W43 recovery, the continuing open Vale containment and corrective work, the two High-priority actions that are still Planned, and the leadership decisions needed before the first W44 deadline. Use only facts already supported by the workbook.
```

**Talking point:** The output should be a decision-ready narrative with cited source figures, not a claim that the suspected defect or financial effect has been proven.

---

## 6. Draft leadership communication (Outlook)

**Scenario.** The Plant Head needs a short mobile-friendly message, not a copy of the whole report. This exercise produces a draft only.

Start a new Outlook draft and select the reviewed report and cleaned workbook as sources if available.

**Prompt 6.1**

```text
Draft, but do not send, an email to Contoso leadership based only on the selected Weekly_Operations_Report_W43.docx and Manufacturing_Operations_Performance_and_Risk.xlsx.

Use the Email_Distribution sheet to identify Primary and CC roles; these are fictional example addresses, so do not actually send. Include the W43 versus W42 operational highlights, the remaining Vale and Crest risks, and the three High-priority actions with owners and target dates.

Use fewer than 200 words, a professional executive tone, and two labels: Urgent risks and Follow-ups. End by requesting the necessary decisions before the earliest action due date and mention that the full report will be attached. Do not invent a budget amount, a confirmed root cause or a safety conclusion.
```

**Talking point:** A short draft can show the difference between improved production and unresolved risk. A person must verify the data, recipients, attachment and decision request.

---

## Advanced extension: Copilot Analyst (optional)

**Scenario.** The director asks whether the W42 drop had earlier warning signs. Four weeks are a small sample, so any forward-looking calculation is illustrative only.

**Prompt**

```text
Using the cleaned Manufacturing_Operations_Performance_and_Risk.xlsx, join Operations_Data and Quality_and_Supplier_Risk on Week, Plant and Line. For W40–W43, calculate total Downtime Minutes, Scrap Units, Changeover Minutes and Late PO Lines, plus unweighted average OEE and unweighted average incoming Defect PPM.

Identify indicators that worsened from W40 to W41 before the W42 OEE drop, citing the values. Propose three illustrative warning thresholds, explaining that they are demo heuristics rather than validated controls. Show a clearly labeled, simple W44 scenario by line using a stated method, not a prediction or commitment. Show trend charts and describe the limitations of four observations, missing order-line denominators, differing measurement populations and possible confounding.
```

**Talking point:** Early-warning discussion is useful only when its data limitations and uncertain causal explanations remain visible.
