# Manufacturing Operations Performance & Risk

Contoso is a mid-sized industrial electronics manufacturer. It builds the power, control and motion components that go into factory automation equipment and electric vehicles, and ships them to equipment makers on tight, contract-based delivery dates. Production runs in two plants:

- **Plant A** (electronics assembly): Power Modules on Line 1 and Control Boards on Line 2
- **Plant B** (mechanical and sensor assembly): Drive Trains on Line 1 and Sensor Packs on Line 2

Each line depends on one key supplier for its critical material, so a late or defective shipment quickly turns into downtime, scrap and missed customer deliveries.

The plants report four weeks of data, **W40 to W43**. In **W42**, both plants had a bad week: lines stopped, scrap went up, deliveries slipped and customers complained. In **W43**, the numbers bounced back.

It is the **Monday morning after W43 closed**. The **Operations Performance Manager** has to brief leadership at the **2 p.m. weekly performance and risk review** and get approval for a recovery plan. Leadership wants clear answers: *Was W42 a one-off or a pattern? Is the W43 recovery real? Which lines and suppliers are behind it? What do we need to approve now?*

The challenge is that a credible answer means bringing together several kinds of information that arrived in one workbook from different teams:

- Weekly throughput, scrap and downtime by plant and line
- Equipment effectiveness (OEE, availability, performance, quality) and on-time delivery
- First pass yield, defect rates and customer complaints
- Supplier delivery performance and expedite costs
- Open management actions, owners and due dates
- The leadership distribution list

**The challenge is not data availability. It is turning many operational records into clear priorities and a decision before 2 p.m.**

The **Operations Performance Manager** uses Microsoft 365 Copilot as one connected workflow across **Excel, Word and Outlook** (plus optional **Teams** and **Copilot Analyst** extensions).

---

## Pain points and demonstrated benefits

| Pain point | How Copilot helps | Business benefit |
|---|---|---|
| The workbook was compiled by plant, quality and procurement teams, and the manager did not build it | Copilot in Excel summarizes the sheets, coverage and key columns in plain language | Faster orientation and earlier focus on decisions |
| Data typed by different shifts and systems has inconsistent names, duplicates and unusual values | Copilot in Excel finds the issues first, then fixes them in the source tables | Reliable totals and no awkward questions about the numbers in front of leadership |
| Business rules are given verbally ("more than 3 hours down is Critical") and nested formulas are slow and error-prone | Copilot in Excel turns plain-English rules into formulas and explains them to others | Repeatable risk signals that update automatically every week |
| Row-level review cannot show what is driving week-over-week movement across lines and suppliers | Copilot in Excel builds trends, cross-sheet matches, PivotTables and an executive dashboard | A clear view of what changed, why, and who owns the fix |
| Analysis must become a report leadership can read before the meeting | Copilot in Word drafts the weekly report from the company template using only workbook data | A consistent, decision-ready report in minutes instead of hours |
| Executives read on their phones between meetings and approvals stall | Copilot in Outlook drafts a short, scannable approval request with owners and deadlines | Faster decisions without rewriting the same facts again |


---

## Demo Journey

### Files

| File | Purpose |
|---|---|
| [DATA_DICTIONARY](./DATA_DICTIONARY.md) | Trainer reference: column definitions and manufacturing glossary (not used in prompts) |
| [Manufacturing_Operations_Performance_and_Risk](./Manufacturing_Operations_Performance_and_Risk.xlsx) | One workbook, four sheets: `Operations_Data`, `Quality_and_Supplier_Risk`, `Action_Register`, `Email_Distribution` |
| [Weekly_Operations_Report_Template](./Weekly_Operations_Report_Template.docx) | Company template for the weekly leadership report |

> **Note:** This workbook contains **synthetic sample data** created solely for training and demonstration purposes. It does not represent any real company, plant, supplier or person. All email addresses are fictional (`contoso.com`).

---

### Demo Step

The demonstration follows the natural workflow of the **Operations Performance Manager** on review day:


| Step |  App | Copilot capability | Leadership question it answers |
|---|---|---|---|
| 1. Understand | Excel | Summarize and explain | *What data do I have, and what matters?* |
| 2. Prepare | Excel | Clean and validate data | *Can I trust this data?* |
| 3. Calculate | Excel | Natural language → formulas | *How do raw numbers become risk signals?* |
| 4. Analyze | Excel | Trends, pivots, dashboard | *What is driving performance and risk?* |
| 5. Report | Word | Grounded drafting across files | *What does leadership need to read?* |
| 6. Communicate | Outlook | Audience-aware writing | *What should leadership approve now?* |

<br>

---

**1. Understand the Operations Dataset (Excel)**

#### <u>Scenario</u>
At 8:30 a.m. The workbook arrived overnight from the plant teams. You did not build it, and the review is at 2 p.m.

Before deeper analysis, the **Operations Performance Manager** needs to understand what information is available, which sheets are relevant, and which columns matter most.


#### <u>Step</u>
- Open `Manufacturing_Operations_Performance_and_Risk.xlsx` 

- **Prompt 1.1 · Worksheet**

```text
As an Operations Performance Manager preparing for a weekly performance review, walk me through each sheet in this workbook: what it contains and why it matters to an operations leader. Explain how the sheets connect.
```

- **Prompt 1.2 · Worksheet**

```text
What does this data cover, and where should I focus this week's review? Give me the top 3 areas and why. Flag anything in the data that looks off, but don't fix it yet.
```

> Key Takeaway & Talking point :
> - The manager quickly establishes what information is available and where to focus the weekly review. 
> - *Copilot didn't just list the sheets. It explained why each one matters to an operations leader. That's the difference between reading data and understanding it.*

---

<br>

**2. Prepare and Validate Data (Excel)**

#### <u>Scenario</u>
An initial review of the workbook shows some possible data issues. For example, "Plant A" and "Plant-A" appear as two different plants, and "Drive Train" and "Drivetrain" as two different products. If these aren't fixed, the numbers get split and the review will tell the wrong story.

Before trusting any analysis, the manager needs to fix the source data, so that every later calculation, pivot table, and report is built on clean numbers. Things to address:
- The same plant or product written in different ways
- Duplicate records
- Unusual downtime, scrap, OEE, or defect values


#### <u>Step</u>
- Open `Manufacturing_Operations_Performance_and_Risk.xlsx` 

- **Prompt 2.1 · Worksheet**

```text
Check Operations_Data and Quality_and_Supplier_Risk for data issues. Don't change any data yet.

In the Plant and Product Family columns, list every value that looks like the same plant or product written differently, with the sheet name and row number.
In Operations_Data, find rows that are exact duplicates of another row. Show their row numbers with Week, Plant, Line and Product Family.
```

- **Prompt 2.2 · Worksheet**

```text
Fix these issues directly in the original sheets:

In both sheets, change "Plant-A" to "Plant A" and "Drivetrain" to "Drive Train".
In Operations_Data, delete the duplicate row. Keep the first occurrence and delete only the second.
Edit the existing cells and tables in place. Don't create a new sheet, table or column, and leave all other data and formatting unchanged. Then confirm:

How many cells changed and how many rows were deleted
Plant contains only "Plant A" and "Plant B", and Product Family contains only Power Module, Control Board, Drive Train and Sensor Pack
How many data rows Operations_Data now has, and that each Week, Plant and Line combination appears only once
```
<br>

> Key Takeaway & Talking point
> - The source tables are now clean and consistent. Every calculation, pivot, report from this point uses the same trusted data.
> - *Copilot found the problems first, and only then fixed them in the original data. Without this step, W43 Sensor Pack output is counted twice and Plant A is split in two, so every number on the dashboard would be wrong.*

---

<br>

**3. Create Calculated Signals (Excel)**

#### <u>Scenario</u>
The Plant Head calls with a rule: "Anything with more than 3 hours of downtime, or that ships late on more than 10% of orders, is Critical." Everything else follows the team's existing High, Medium and Low tiers. The Quality Lead also wants lines with low first pass yield and high scrap flagged for review. These rules have to apply to every line and every week, and they must keep working when next week's data is added.

Before the data can support management decisions, the manager needs to apply these rules to the data. Things to address:
- Apply the rules to every row with a formula, not by hand
- Update automatically when new rows are added


#### <u>Step</u>
- Open `Manufacturing_Operations_Performance_and_Risk.xlsx` 

- **Prompt 3.1 · Worksheet: Operations_Data**

```text
Add a new column at the end of the Operations_Data table named "Operational Risk Category". Use a formula that applies these rules in order and uses the first one that matches:

Critical: Downtime Minutes greater than 180, OR On-Time Delivery % less than 0.90
High: Downtime Minutes from 140 to 180, OR Scrap Units greater than 45
Medium: Downtime Minutes from 100 to 139, OR Scrap Units from 30 to 45
Low: all other rows
Then explain the formula to a new team member who will maintain this workbook, and count how many rows are Critical, High, Medium and Low in each Week.
```

- **Prompt 3.2 · Worksheet: Quality_and_Supplier_Risk**

```text
Add a new column at the end of the Quality_and_Supplier_Risk table named "Quality Watch Flag". Use a formula that returns "Watch" when First Pass Yield Actual is less than 0.96 AND Scrap Rate is greater than 0.035, and "Stable" otherwise.

Then explain the formula and count how many rows are Watch in each Week.
```

<br>

> Key Takeaway & Talking point
> - The manager turns verbal business rules into consistent, repeatable risk signals that the analysis and the report will use next.
> - *Copilot didn't just label the rows. It turned the rule into a formula that runs on every row, updates automatically when next week's data arrives, and can be explained to anyone.*
---

<br>

**4. Identify Performance and Risk Drivers (Excel)**

#### <u>Scenario</u>
The Operations Director messages you: "Was W42 a one-off or a pattern? Which line and which supplier? I need one page, not 16 rows."

Now that the data is clean and categorized, the manager needs to answer the bigger question: what is actually driving performance and risk? Things to address:
- Compare weeks to see whether W42 was a one-off or part of a trend
- Identify which lines and suppliers are driving the risk
- Summarize the findings on one page, without changing the source data


#### <u>Step</u>
- Open `Manufacturing_Operations_Performance_and_Risk.xlsx` 

- **Prompt 4.1 · Worksheet: Operations_Data**

```text
Using the Operations_Data table, create a new sheet named "Weekly_Trends" with:
- A summary table by Week: total Completed Units, total Downtime Minutes, average OEE and average On-Time Delivery %
- A second table showing OEE by Week for each Plant and Line
- A line chart of average OEE by Week
Then answer in 3 bullet points: was W42 a one-off or part of a pattern, which lines were hit hardest, and did performance recover in W43? Don't change the source table.
```

- **Prompt 4.2 · Worksheet: Operations_Data & Quality_and_Supplier_Risk**

```text
Create a new sheet named "Risk_Drivers" with two tables:
1. Match Operations_Data and Quality_and_Supplier_Risk by Week, Plant and Line. List the rows where Quality Watch Flag is "Watch" AND OEE is below 0.70, showing Week, Plant, Line, Product Family, Supplier, OEE, First Pass Yield Actual, Scrap Rate, Defect PPM and Operational Risk Category.
2. One row per Supplier with total Late PO Lines, total Expedite Cost USD and total Production Impact Hours across all weeks, sorted by Expedite Cost USD from highest to lowest.
Then tell me in 2–3 sentences which lines appear in more than one week and which two suppliers create the most operational risk. Don't change the source tables.
```

- **Prompt 4.3 · Worksheet: Operations_Data,  Quality_and_Supplier_Risk & Action_Register**

```text
Create a new sheet named "Executive_Dashboard" using the Operations_Data, Quality_and_Supplier_Risk and Action_Register tables. Include:
- KPI tiles: Total Completed Units (W40–W43), Total Downtime Minutes, Average OEE, and Average Scrap Rate (from Quality_and_Supplier_Risk)
- A table by Week with average OEE and average On-Time Delivery %, using red, amber and green indicators: (1). OEE: green at 0.75 or above, amber from 0.60 to below 0.75, red below 0.60 (2). On-Time Delivery %: green at 0.95 or above, amber from 0.90 to below 0.95, red below 0.90
- Top 3 high-risk lines: the 3 rows in W42 with the highest Downtime Minutes, with their Operational Risk Category
- Top 2 supplier risks: the 2 suppliers with the highest total Expedite Cost USD
- Recommended actions: the High priority actions from Action_Register, with Owner Name, Target Date and Status
Use an executive-friendly layout that fits on one page. Don't change the source tables.
```


- **Prompt 4.4 (Optional)· Worksheet: Operations_Data**

```text
Create a PivotTable on a new sheet named "Pivot_Plant_Product" from the Operations_Data table. Put Plant and Product Family in rows, and show the sum of Completed Units, Scrap Units, Downtime Minutes and Estimated Gross Margin USD as values, with a grand total. Don't change the source table.
```

<br>

> Key Takeaway & Talking point
> - The manager moves from "What data do we have?" to "What is driving the business, and who fixes it?", seeing where performance dropped, which lines and suppliers drove W42, what it cost, and who owns each fix..
> - *Copilot didn't just summarize the numbers. The top risks it found, Plant A Line 2, Drive Train, Nova and Apex, are the same names already in the Action Register. That's the difference between reporting a problem and showing leadership the data and the plan agree.*
---



---

<br>

**5. Create the Weekly Leadership Report (Word)**

#### <u>Scenario</u>
Leadership expects the weekly report in the standard template one hour before the review, so they can read it in advance.

Before the review, the manager needs to turn the Excel findings into a concise report leadership can read in minutes. Things to address:
- Follow the standard report template
- Use only data from the workbook
- Make the decision needed this week obvious


#### <u>Step</u>
- Use `Manufacturing_Operations_Performance_and_Risk.xlsx` & `Weekly_Operations_Report_Template.docx`
- Open new Word file

- **Prompt 5.1 : New Word File (Weekly_Operations_Report_W43.docx)**

```text
Using /Weekly_Operations_Report_Template.docx as the structure and /Manufacturing_Operations_Performance_and_Risk.xlsx as the only data source, draft the weekly manufacturing operations report.

Header:
- Reporting Week: 2026-W43
- Prepared By: Operations Performance Manager

Use exactly the six sections of the template, in the same order:
1. Executive Summary
2. Throughput and OEE Movements: compare W43 with the W42 low point and the W40 baseline, by plant and line, including the change in weekly Estimated Gross Margin USD
3. Quality and Supplier Risk Watchlist: FPY, scrap and defect PPM signals, plus the two suppliers with the highest total expedite cost
4. Top Root-Cause Hypotheses: three hypotheses, each supported by specific numbers from the workbook
5. Top 3 Management Actions: the three High priority actions from Action_Register, each with Owner Name, Target Date, Status and Expected Impact
6. Leadership Approval Needed: what leadership must approve this week, with timing based on the Target Dates in Action_Register

Guidelines:
- Use only numbers from the workbook. Don't invent data.
- Keep it concise, with headings and bullet points.
- Focus on business impact and the decision needed this week.
```

- **Prompt 5.2 : Select the Executive Summary section**

```text
Rewrite this to about 150 words. Cover three points: what improved in W43, whether the recovery is sustainable given that two of the three High priority actions are still only Planned, and what leadership needs to approve this week.
```

<br>

> Key Takeaway & Talking point
> - The manager turns the Excel findings into a management-ready weekly report that leadership can read before the meeting.
> - *Copilot didn't just report the recovery. It surfaced the risk that remains: two of the three fixes that prevent another W42 haven't started yet. That's the difference between summarizing results and making the decision leadership needs to make obvious.*
---

<br>

**6. Send Leadership Communication (Outlook)**

#### <u>Scenario</u>
The Plant Head won't open a six-section report on their phone between meetings. They need a short email that says what is urgent and what they must approve, before the first action is due on Wednesday of W44.

Before the review, the manager needs to turn the report into a concise message leaders can act on. Things to address:
- Separate urgent risks from normal follow-ups
- Keep it short enough to read on a phone
- End with a clear approval request and deadline


#### <u>Step</u>
- Open `Outlook (New email)` 
- Use `Manufacturing_Operations_Performance_and_Risk.xlsx` & `Weekly_Operations_Report_W43.docx`

- **Prompt 6.1**

```text
Draft an email to the leadership team using /Weekly_Operations_Report_W43.docx and /Manufacturing_Operations_Performance_and_Risk.xlsx.

Address the greeting to the people marked Primary in the Email_Distribution sheet, and mention that the people marked CC are copied.

Include:
- Key operational highlights for W43 compared with W42
- Major quality and delivery risks
- The three High priority actions from Action_Register, with owner names and target dates

Requirements:
- Under 200 words, easy to read on a phone
- Professional executive tone
- Two clearly labeled parts: "Urgent risks" and "Follow-ups"
- End with a clear approval request, due before the earliest Target Date of the High priority actions
- Mention that the full weekly report is attached
```

<br>

> Key Takeaway & Talking point
> - The manager sends leadership a clear, action-oriented message with the decision needed, the owners, and the deadline.
> - *Copilot didn't just shorten the report. It separated what's urgent from what can wait and ended with a clear ask.*
---

<br>

**Advanced Extension: Copilot Analyst**

#### <u>Scenario</u>
After the review, the Operations Director asks: "W42 surprised us. Could we have seen it coming, and what should we watch in W44?"

Now that the manager understands what happened, the next question is: are there early-warning patterns we should watch, and what might happen next? Things to address:
- Find which indicators moved before the W42 drop
- Set early-warning thresholds leadership can monitor weekly
- Give an indicative outlook for W44, with its limitations stated clearly


#### <u>Step</u>
- Open Copilot Agent : **Analyst**

- **Prompt**

```text
Using Python, analyze /Manufacturing_Operations_Performance_and_Risk.xlsx. Join Operations_Data and Quality_and_Supplier_Risk on Week, Plant and Line.

1. For each week from W40 to W43, total Downtime Minutes, Scrap Units, Changeover Minutes and Late PO Lines, and calculate average OEE and average Defect PPM.
2. Identify which indicators had already risen in W41, one week before the W42 drop in OEE.
3. Recommend 3 early-warning thresholds leadership should monitor weekly, based on the W41 values.
4. Give a simple, indicative W44 outlook for OEE by line.

Show trend charts, explain the results in plain business language, and clearly state the limitations of having only four weeks of data.
```

<br>

> Key Takeaway & Talking point
> - The manager extends the weekly review from looking back to looking ahead, with leading indicators that flagged W42 a week early and thresholds leadership can monitor every week.
> - *Copilot didn't just explain what happened. It showed what to watch so it doesn't happen again, and was honest about what four weeks of data can and can't tell us.*


