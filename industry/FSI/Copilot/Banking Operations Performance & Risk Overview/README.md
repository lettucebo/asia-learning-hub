# Bank Banking Operations Demo

This demo uses Copilot in excel, word and outlook.

**Scenario:**
You're a banking operations analyst at Bank reviewing deposit and loan book movements, balances, fee and spread income, customer segments, and portfolio risk signals across zones.

## Demo Setup

**Workbook:** [Bank Portfolio Insights Demo](https://github.com/CSDSkilling/asia-learning-hub/blob/897c068de60f6282b2eae9fd842b4806071efb9a/industry/FSI/Copilot/Banking%20Operations%20Performance%20%26%20Risk%20Overview/Bank_Portfolio_Insights_Demo.xlsx)

> **Note:** This workbook contains **synthetic sample data** created solely for training and demonstration purposes. It does not represent any real customers, accounts, transactions, or financial institutions.
>

> **Demo Objective:** Use this workbook to demonstrate how Microsoft Copilot can analyze banking operations, portfolio performance, risk indicators, customer trends, and business outcomes through natural language prompts, helping business

## Copilot in Excel

### Workbook Orientation

[Worksheet: any]

```text
Summarize this workbook in 30 seconds.
```

[Worksheet: any]

```text
Explain this workbook as if I am a retail banking operations head.
```

[Worksheet: any]

```text
What are the most important columns in this workbook?
```

### Data Cleanup

[Worksheet: Branch Flows]

```text
Normalize similar product line or customer segment names.
```

[Worksheet: Branch Flows]

```text
Identify duplicate records in this table.
```

[Worksheet: Branch Flows]

```text
Find unusual or outlier values in Net Flows, Closing Balance, or Spread / Fee.
```

### Calculated Columns

[Worksheet: Branch Flows]

```text
Create a new column called Flow Impact Category based on Net Flows. Use High Inflow, Moderate Inflow, Outflow, and Stable.
```

[Worksheet: Risk Metrics]

```text
Create a formula to identify portfolios with Gross NPA above the risk watch threshold and a coverage ratio below 0.70.
```

[Worksheet: Branch Flows]

```text
Explain this inherited formula in the Estimated Annual Income column.
```

### Trend Analysis

[Worksheet: Branch Flows]

```text
Analyze balance and net flow trends by month.
```

[Worksheet: Summary]

```text
Identify product lines with the highest estimated annual income.
```

[Worksheet: Summary]

```text
Create a pivot table by Region (Zone) and Product Line showing Net Flows, Closing Balance, and Estimated Annual Income.
```

[Worksheet: Summary]

```text
Create a chart showing Estimated Annual Income by Product Line.
```

### Risk Analysis

[Worksheet: Risk Metrics]

```text
Highlight all portfolios approaching risk review status.
```

[Worksheet: Risk Metrics]

```text
Apply conditional formatting for portfolios where credit cost exceeds the active spread.
```

[Worksheet: Risk Metrics]

```text
Identify portfolios that need leadership attention and explain why.
```

## Executive Dashboard Challenge

[Worksheet: Summary]

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

---

## Copilot Premium / Analyst

```text
Using Python, forecast next quarter net flows and identify clusters of recurring portfolio or customer-segment risks. Create a clear summary, show the forecast trend, and explain which areas need leadership attention.
```

## Copilot in Word


### 🏦 Demo Prompt: Create a Leadership-Ready Portfolio Report

Creating executive summary in Word

```text
Create a leadership-ready portfolio performance summary based on the analysis from the Excel workbook [Attach the excel here].

Include:

- Executive Summary
- Key Portfolio Movements
- Product Lines Driving Income
- Regional Observations
- Risk Watchlist
- Recommended Management Actions

Guidelines:
- Keep the report concise and insight-driven.
- Use clear headings and bullet points.
- Highlight significant trends, risks, and business implications.
- Base all observations only on the data available in the workbook.
- Present all financial figures in INR crore (₹ Cr).
- Use a professional tone suitable for senior banking leaders.
```
``

Save the document.

```text
Write a 150-word executive risk summary based on this workbook for Bank leadership.
```

## Copilot in Outlook

After generating the Word report, the report is ready but business value is still not created. Somebody needs to read it. Now we move from documentation to communication.

The Head of Retail Banking does not want:
	• 10 worksheets
	• 30 charts
	• 5 pages of data
They want:
	• What happened?
	• What should I worry about?
	• What action do I need to take?

Give the below prompt in the Copilot in Outlook:

### 📧 Demo Prompt: Draft an Executive Email

```text
Draft an email to the Head of Retail Banking summarizing the portfolio review.

Reference the attached executive summary. [Attach the saved word document from the previous step]

Include:
- Key portfolio highlights
- Income opportunities
- Risk areas requiring attention
- Three recommended actions

Requirements:
- Keep the email under 200 words.
- Use a professional and executive-friendly tone.
- Focus on business impact and decision-making insights.
- Highlight material changes in portfolio performance.
- Clearly distinguish growth opportunities from risk concerns.
- Present recommendations as actionable management priorities.
- Do not include technical analysis details unless they directly impact business outcomes.
```
