# Bank Banking Operations Performance & Risk Demo

This demo showcases how a **Banking Operations Analyst** can use **Copilot in Excel** to explore portfolio data, improve data quality, identify trends, investigate risk indicators, and turn a complex banking workbook into decision-ready insights.

---

## Scenario

You are a **Banking Operations Analyst at Bank** supporting periodic reviews of the bank's deposit and lending portfolio.

You have received a workbook containing information about:

- Deposit and loan balances
- Net portfolio flows
- Product lines
- Customer segments
- Regional / zonal performance
- Spread and fee income
- Estimated annual income
- NPA and portfolio risk indicators

The data is available, but the challenge is turning hundreds of operational data points into meaningful insights.

Leadership wants to understand:

- Which products and regions are growing?
- Where are balances or net flows declining?
- Which products are contributing most to income?
- Are there emerging portfolio risks?
- Which areas require management attention?
- Where should the bank investigate further?

The analyst needs to move from **raw portfolio data to actionable banking insights**.

---

## Business Pain Points

The Banking Operations Analyst faces several challenges during a typical portfolio review.

### 1. Understanding a Complex Workbook

Banking analysts often receive workbooks created or maintained by other teams.

Before performing analysis, the analyst needs to understand:

- What information is available
- Which worksheets are relevant
- Which columns are important
- What existing calculations mean
- Where to begin the analysis

**How Copilot helps:**  
Copilot enables the analyst to explore the workbook using natural-language questions and quickly understand the structure and important data points.

**Business benefit:**  
The analyst can orient themselves around the dataset faster and focus on the information most relevant to the portfolio review.

---

### 2. Preparing and Cleaning Data

Portfolio analysis can be slowed down by inconsistent product names, customer segments, duplicate records, or unusual values.

Manually checking hundreds of rows can consume valuable analysis time.

**How Copilot helps:**  
Copilot can assist the analyst in identifying potential data-quality issues and preparing the dataset for analysis.

**Business benefit:**  
Less time is spent manually inspecting rows, allowing the analyst to focus on meaningful business exceptions.

---

### 3. Working with Formulas and Calculations

Operational banking workbooks frequently contain inherited formulas and calculated fields.

The analyst may need to:

- Understand an existing formula
- Create a new classification
- Introduce additional risk calculations
- Apply business logic consistently across the dataset

**How Copilot helps:**  
Copilot can help explain existing formulas and assist with creating additional calculated columns using natural-language instructions.

**Business benefit:**  
The analyst can understand and extend workbook calculations more efficiently.

---

### 4. Identifying Performance Drivers

Individual rows do not immediately reveal what is driving overall portfolio performance.

The analyst needs to determine:

- Which products are driving income
- Which zones are growing
- Where balances are declining
- Whether net-flow patterns are changing
- Which areas appear unusual

**How Copilot helps:**  
Copilot can help analyze trends, summarize patterns, create pivot tables, and generate visualizations.

**Business benefit:**  
The analyst can move from reviewing individual records to understanding **portfolio-level business drivers**.

---

### 5. Identifying Emerging Risk Signals

Portfolio growth does not tell the complete story.

The analyst also needs to investigate risk indicators such as:

- Gross NPA
- Coverage ratio
- Credit cost
- Active spread
- Portfolios approaching predefined risk thresholds

**How Copilot helps:**  
Copilot can help identify and highlight records that match specified risk conditions.

**Business benefit:**  
Potential risk areas can be reviewed alongside growth and income indicators, helping the analyst maintain a balanced view of **performance and risk**.

---

### 6. Turning Analysis into Management-Ready Insight

Leadership does not want to review hundreds of individual rows.

They need a consolidated view showing:

- Overall portfolio position
- Net flows
- Income drivers
- Regional performance
- Risk indicators
- Areas requiring attention

**How Copilot helps:**  
Copilot can help organize workbook information into summaries, pivots, charts, and an executive-oriented dashboard.

**Business benefit:**  
The workbook evolves from a **data repository into a business review tool**.

---

# Copilot in Excel Demo Journey

The demonstration follows the natural workflow of the Banking Operations Analyst:

**Understand → Prepare → Calculate → Analyze → Investigate Risk → Summarize**


## Demo Setup

**Workbook:** [Bank Portfolio Insights Demo](https://github.com/CSDSkilling/asia-learning-hub/blob/897c068de60f6282b2eae9fd842b4806071efb9a/industry/FSI/Copilot/Banking%20Operations%20Performance%20%26%20Risk%20Overview/Bank_Portfolio_Insights_Demo.xlsx)

> **Note:** This workbook contains **synthetic sample data** created solely for training and demonstration purposes. It does not represent any real customers, accounts, transactions, or financial institutions.

> **Demo Objective:** Use the workbook to demonstrate how Copilot in Excel can support a banking operations analyst as they move from understanding portfolio data to identifying performance drivers, investigating risk indicators, and creating management-ready insights.


---

# 1. Understand the Portfolio

## Business Challenge

The analyst has received the workbook but does not yet fully understand its structure or which fields are important.

Before performing deeper analysis, the analyst first needs to understand the data.

## How Copilot Helps

Use natural-language questions to explore the workbook and quickly establish what information is available.

## Workbook Orientation

**Worksheet: Any**

```text
Summarize this workbook in 30 seconds.
```

**Worksheet: Any**

```text
Explain this workbook as if I am a retail banking operations head.
```

**Worksheet: Any**

```text
What are the most important columns in this workbook?
```

### Business Outcome

The analyst quickly establishes what information is available and where to focus the portfolio review.

---

# 2. Prepare the Data

## Business Challenge

Before trusting the analysis, the analyst needs to investigate the quality and consistency of the underlying data.

Potential issues could include:

- Similar product lines using different names
- Inconsistent customer segment labels
- Duplicate records
- Unusual balance or flow values

## How Copilot Helps

Copilot assists the analyst in identifying potential data-quality issues that should be reviewed before deeper analysis.

## Data Cleanup

**Worksheet: Branch Flows**

```text
Normalize similar product line or customer segment names.
```

**Worksheet: Branch Flows**

```text
Identify duplicate records in this table.
```

**Worksheet: Branch Flows**

```text
Find unusual or outlier values in Net Flows, Closing Balance, or Spread / Fee.
```

### Business Outcome

The analyst can improve confidence that subsequent portfolio analysis is being performed on a more consistent dataset.

---

# 3. Enrich the Analysis with Calculations

## Business Challenge

Raw financial measures sometimes need additional business classifications before they can support management analysis.

For example, the analyst may want to distinguish significant inflows from moderate inflows, stable portfolios, and outflows.

The analyst may also inherit formulas created by another team member without immediately understanding the underlying logic.

## How Copilot Helps

Copilot can assist with creating calculated fields and explaining existing formulas.

## Calculated Columns

**Worksheet: Branch Flows**

```text
Create a new column called Flow Impact Category based on Net Flows. Use High Inflow, Moderate Inflow, Outflow, and Stable.
```

**Worksheet: Risk Metrics**

```text
Create a formula to identify portfolios with Gross NPA above the risk watch threshold and a coverage ratio below 0.70.
```

**Worksheet: Branch Flows**

```text
Explain this inherited formula in the Estimated Annual Income column.
```

### Business Outcome

Raw financial measures can be transformed into understandable business classifications that support portfolio review.

---

# 4. Identify Portfolio Performance Drivers

## Business Challenge

Now that the data is understood and prepared, the analyst needs to answer the more important business question:

> **What is actually driving portfolio performance?**

Reviewing rows individually makes it difficult to identify patterns across products, zones, and time periods.

## How Copilot Helps

Copilot can help summarize patterns, analyze trends, aggregate information, and create visualizations that make portfolio movements easier to understand.

## Trend Analysis

**Worksheet: Branch Flows**

```text
Analyze balance and net flow trends by month.
```

**Worksheet: Summary**

```text
Identify product lines with the highest estimated annual income.
```

**Worksheet: Summary**

```text
Create a pivot table by Region (Zone) and Product Line showing Net Flows, Closing Balance, and Estimated Annual Income.
```

**Worksheet: Summary**

```text
Create a chart showing Estimated Annual Income by Product Line.
```

### Business Outcome

The analyst can identify:

- Where portfolio growth is coming from
- Which products are driving estimated income
- How performance differs across zones
- Where further investigation may be required

This shifts the analysis from **"What data do we have?"** to **"What is driving the business?"**

---

# 5. Investigate Portfolio Risk

## Business Challenge

Strong growth or income performance does not necessarily mean that a portfolio is healthy.

The analyst also needs to ask:

> **Are there emerging risks behind the performance numbers?**

Risk indicators need to be considered alongside balance, flow, and income measures.

## How Copilot Helps

Copilot can help the analyst identify portfolios that meet defined risk conditions and make those records easier to investigate.

## Risk Analysis

**Worksheet: Risk Metrics**

```text
Highlight all portfolios approaching risk review status.
```

**Worksheet: Risk Metrics**

```text
Apply conditional formatting for portfolios where credit cost exceeds the active spread.
```

**Worksheet: Risk Metrics**

```text
Identify portfolios that need leadership attention and explain why.
```

### Business Outcome

The analyst can review portfolio performance and risk together rather than looking at growth metrics in isolation.

This helps identify situations where strong performance may require closer risk monitoring.

---

# 6. Create a Management View

## Business Challenge

At this stage, the analyst has explored:

- Portfolio balances
- Net flows
- Product performance
- Income
- Regional differences
- Risk indicators

However, management should not have to repeat all of the analysis themselves.

They need a consolidated view that answers a simpler set of questions:

- How is the portfolio performing?
- What is driving performance?
- Where are the risks?
- What deserves attention?

## How Copilot Helps

Copilot can help bring multiple portfolio measures together into an executive-oriented dashboard.

---

# Executive Dashboard Challenge

**Worksheet: Summary**

```text
Create an Executive Banking Operations Dashboard from this workbook.

Include:
- Total Closing Balances
- Total Net Flows
- Estimated Annual Income
- Top Income Product Line
- Product Line trend
- Zonal balance view
- NPA / risk watchlist
- Executive summary with recommended actions

Use an executive-friendly layout with red, amber, and green indicators.
```

### Business Outcome

The analyst brings multiple portfolio measures into one consolidated management view, making it easier to support portfolio review discussions.

The journey has now moved from:

**Raw Data → Analysis → Insight → Management View**

---

# Copilot Premium / Analyst

Once the analyst understands historical portfolio performance, the next question becomes:

> **What might happen next, and are there recurring patterns we should investigate?**

For a more advanced analytical experience, use Copilot Analyst to explore forecasting and recurring portfolio risk patterns.

```text
Using Python, forecast next quarter net flows and identify clusters of recurring portfolio or customer-segment risks.

Create a clear summary, show the forecast trend, and explain which areas need leadership attention.
```

## Business Value

This extends the portfolio review from analyzing historical information to exploring:

- Potential future net-flow patterns
- Recurring portfolio risks
- Customer-segment risk concentrations
- Areas that may require additional management attention

---

# End-to-End Demo Story

The demonstration is designed as one connected banking operations workflow rather than a collection of individual Excel features.

## Step 1: Understand

**Question:**  
What data do I have?

**Copilot experience:**  
Summarize and explain the workbook.

**Outcome:**  
Understand the portfolio dataset.

---

## Step 2: Prepare

**Question:**  
Can I trust and consistently analyze the data?

**Copilot experience:**  
Investigate duplicates, inconsistent categories, and unusual values.

**Outcome:**  
Prepare the dataset for analysis.

---

## Step 3: Calculate

**Question:**  
Can I enrich the raw data with useful business classifications?

**Copilot experience:**  
Create calculated columns and explain formulas.

**Outcome:**  
Convert raw measures into useful business indicators.

---

## Step 4: Analyze

**Question:**  
What is driving portfolio performance?

**Copilot experience:**  
Analyze trends, compare products, create pivots, and visualize income.

**Outcome:**  
Identify important portfolio and business drivers.

---

## Step 5: Investigate Risk

**Question:**  
Where should we pay closer attention?

**Copilot experience:**  
Identify portfolios matching defined risk conditions.

**Outcome:**  
Surface areas requiring further review.

---

## Step 6: Summarize

**Question:**  
What does management need to see?

**Copilot experience:**  
Create an executive banking operations dashboard.

**Outcome:**  
Bring performance, income, regional insights, and risk indicators into one management view.

---

# Demo Takeaway

This demonstration is not simply about asking Copilot questions in Excel.

It demonstrates how a Banking Operations Analyst can use Copilot throughout a realistic portfolio review:

> **Understand the data → Prepare the data → Build calculations → Identify performance drivers → Investigate risk → Create a management view**

The value of Copilot is not just completing individual Excel tasks.

The broader value is helping the analyst move more efficiently from **portfolio data to business insight**, while spending more time interpreting performance, investigating risk, and identifying areas that deserve management attention.

---

```
