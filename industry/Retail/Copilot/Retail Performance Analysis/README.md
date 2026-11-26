# Retail Performance Analysis

## Setting the Scene

You are the retail manager at **Contoso Marketplace**, a national Australian omnichannel retailer operating physical stores and digital sales across **Sydney, Melbourne, Brisbane, Perth, and Adelaide**.

The company has invested in:
* Online shopping
* Click & Collect
* Loyalty programmes
* Seasonal and weekend promotions
* A broad product portfolio covering fashion, beauty, electronics, and home products

Contoso Marketplace has recorded strong sales growth, but management wants to understand whether it represents healthy, profitable growth. Revenue alone does not tell the full story. Some channels and product categories may be generating significant sales while delivering weaker margins or lower customer satisfaction.

The leadership team is encouraged by revenue growth but wants to ensure it is profitable, sustainable, and supported by a consistently good customer experience. As they prepare for their quarterly business review (QBR), they need answers to several questions:
* What is driving the growth in sales and profit?
* Which regions, stores, channels, and categories are performing best?
* Where is revenue growing at the expense of margin?
* Are promotions and discounts producing profitable incremental sales?
* Could customer satisfaction issues threaten future growth?
* Where should the company focus its investment and management attention next?

---

## Dataset Overview (`Copilot_Retail_Sales_Demo.xlsx`)

You have been given a synthetic retail transaction workbook (`Copilot_Retail_Sales_Demo.xlsx`) containing:
* **720 transactions** across 2024 and 2025
* **Five regions:** Sydney, Melbourne, Brisbane, Perth, and Adelaide
* **Ten stores**
* **Three channels:** Online, In-store, and Click & Collect
* **Five merchandise categories:** Apparel, Beauty, Electronics, Footwear, and Home
* **Context & Metrics:** Product, customer segment, promotional information, commercial measures (units, sales, cost, profit, margin), and a customer satisfaction score for every transaction.

The workbook connects four parts of retail performance:
1. **What was sold:** Category, Product, and Units
2. **Where and how it was sold:** Region, Store, and Channel
3. **Financial outcome:** Net Sales, COGS, Profit, and Margin
4. **Customer and promotional context:** Customer Segment, Promotion, Discount, and Satisfaction

---

## Business Objectives & Management Tension

The Retail Director has asked the management team to prepare for the quarterly business review by answering five practical questions:
1. Are sales and profit growing?
2. Which regions, stores, categories, and channels are driving growth?
3. Are promotions producing profitable sales, or merely discounting revenue?
4. Where are margin or customer-experience problems emerging?
5. Where should management place inventory, marketing, and operational attention?

### The Central Question
> **How can Contoso Marketplace continue growing without sacrificing profitability or customer experience?**

### Starting Hypotheses
* Sales have grown strongly, but margin has not increased at the same rate as revenue.
* Online is the largest sales channel, but its customer satisfaction result warrants investigation.
* Click & Collect is currently smaller but produces an attractive combination of margin and satisfaction.
* Electronics generates substantial revenue but has weaker margins than other categories.
* Peak promotional periods produce strong sales, but those sales may come with a profitability trade-off.

*(Note: Treat these as starting hypotheses. Your analysis must validate them, challenge them where appropriate, and identify the most credible management actions.)*

---

## Demo Execution & Learner Challenge

### Suggested Opening Script
> “Contoso Marketplace has delivered strong sales growth across its Australian retail network. However, the leadership team is concerned that revenue growth may be masking differences in profitability, promotional effectiveness, and customer experience.
> 
> We have been asked to prepare for the quarterly business review. We need to determine which parts of the business are driving profitable growth, which areas require intervention, and where Contoso Marketplace should invest next.
> 
> We’ll begin in Excel by asking Copilot to explain the workbook and identify the most important measures. We’ll then move from descriptive analysis into deeper investigation with the Analyst agent. Finally, we’ll convert our findings into a Word management report and an executive PowerPoint presentation.
> 
> The goal isn’t simply to produce charts. It is to turn retail data into a clear, evidence-based management recommendation.”

### Learner Challenge
By the end of the activity, learners should be able to answer:
> **If you were the Retail Director, what three decisions would you make based on this data, and what evidence supports each decision?**

### Connected Microsoft 365 Workflow
1. **Excel:** Analyse the retail transactions and build an executive dashboard.
2. **Analyst Agent:** Investigate the drivers behind sales, margin, and satisfaction.
3. **Word:** Convert the findings into a management performance report.
4. **PowerPoint:** Transform the Word report into a concise executive presentation.

---

## Key Findings & Business Pain Points

*Extracted from the spreadsheet—treat these as signals that warrant investigation rather than proof of causation.*

### 1. Growth is strong, but margin has softened
* Net sales increased from ~$136,327 in 2024 to ~$181,048 in 2025 (+32.8%).
* Profit increased from ~$57,371 to ~$75,063.
* Margin declined slightly from ~42.1% to ~41.5%.
* **Pain point:** Contoso Marketplace may be growing revenue faster than margin. Management needs to understand whether the change comes from category mix, channel mix, discounting, or cost pressure.

### 2. Online is the largest channel, but customer satisfaction is lower
* Online produced ~$157,644 in net sales (largest channel).
* Online satisfaction averaged ~3.99, compared with ~4.15 for In-store and ~4.14 for Click & Collect.
* Online margin was ~40.9%, below Click & Collect at ~44.5%.
* **Pain point:** Online growth may be introducing fulfilment, service, usability, or delivery issues.

### 3. Click & Collect appears underdeveloped
* Click & Collect generated ~$37,463 (considerably less than Online and In-store).
* Delivered the highest channel margin (~44.5%) and strong satisfaction (~4.14).
* **Opportunity:** Click & Collect could be a profitable growth channel if Contoso can increase awareness, availability, and adoption without damaging service levels.

### 4. Electronics generates substantial revenue but weak margin
* Generated ~$84,465 in sales (second-highest category), but margin was ~29.0% (lowest category margin).
* By comparison: Beauty (~59.9%), Apparel (~47.6%), Home (~44.5%), and Footwear (~41.6%).
* **Pain point:** Electronics may suffer from high product cost, competitive pricing pressure, unfavourable product mix, or excessive discounting.

### 5. December delivers peak volume but weaker profitability
* December generated ~$45,884 in sales (strongest month), but margin was ~39.1% (below the 41.7% overall average).
* **Pain point:** Peak-season sales may come with a margin trade-off. Examine seasonal promotions, category mix, and fulfilment costs before repeating the campaign structure.

### 6. Promotional performance is not clearly differentiated
* Transactions with no named promotion generated ~$146,221 in sales (~42.1% margin), whereas named promotions generally produced margins around 41.3% to 41.8%.
* **Pain point:** Promotions may support volume, but lack a major margin advantage. Assess incremental sales rather than just top-line revenue during promotions.

### 7. Store performance is inconsistent
* **Pitt Street:** Highest-sales store (~$51,452).
* **Chadstone:** ~$46,771 sales, ~39.8% margin, ~3.97 satisfaction.
* **Melbourne Central:** ~$41,177 sales, ~44.3% margin, ~4.10 satisfaction.
* **Pain point:** Stores with similar commercial importance produce noticeably different profitability and customer outcomes.

---

## Performance Drivers Reference

| Driver | Why it matters | Management question |
| :--- | :--- | :--- |
| **Year and Month** | Exposes growth, seasonality, and peak periods | Is growth consistent, or concentrated in a few months? |
| **Region and Store** | Identifies geographic and store-level variation | Which stores should be copied, coached, or investigated? |
| **Channel** | Shows the economics of Online, In-store, and Click & Collect | Which channel can grow without weakening margin or satisfaction? |
| **Category and Product** | Reveals product mix and range profitability | Which categories generate revenue but dilute profit? |
| **Units and Unit Price** | Separates volume-driven growth from price-driven growth | Are customers buying more, or are results driven by higher-priced products? |
| **Discount and Promotion** | Helps evaluate promotional dependency | Are discounts generating incremental profitable sales? |
| **COGS** | Shows underlying product-cost pressure | Which products or categories have the greatest cost exposure? |
| **Customer Segment** | Compares New, Returning, and Loyalty customers | Are loyalty customers delivering better value and experience? |
| **Satisfaction** | Adds customer experience to the financial view | Where could service issues threaten future sales? |

---

## Copilot Prompts for Excel

*Run these individually. The staged sequence makes it easier for learners to see how prompts build on previous outputs.*

### A. Understand the workbook
| Prompt | Prompt text |
| :--- | :--- |
| **Generic workbook summary** | Review this workbook and explain its structure, purpose and contents. Identify the time period, number of transactions, geographic coverage, sales channels, merchandise categories, customer segments, promotions and financial measures. Use plain business language. |
| **Retail-manager explanation** | Explain this workbook to me as the retail manager of Contoso Marketplace. Tell me what decisions I could make from this data and identify the most useful measures for managing sales, profitability, promotions, channels, stores and customer experience. |
| **Important columns** | Identify the ten most important columns for a retail manager. For each column, explain what it measures, why it matters and what management question it helps answer. |
| **Data readiness** | Review the data for missing values, duplicate Transaction IDs, inconsistent labels, invalid percentages, unusual dates and possible outliers. Create a short data-quality report and do not change the data unless I approve the changes. |

### B. Summarise and analyse
| Prompt | Prompt text |
| :--- | :--- |
| **Executive summary** | Analyse the Sales Data and provide an executive summary covering net sales, profit, margin, units, average satisfaction and year-over-year growth. Highlight the five most important findings and support every finding with figures from the workbook. |
| **Year comparison** | Compare 2024 and 2025 performance. Show net sales, profit, units, margin and average satisfaction for each year, calculate the percentage changes, and explain where growth improved or weakened performance. |
| **Monthly trend** | Create a monthly performance summary showing Net Sales, Profit, Margin, Units and Satisfaction. Identify the strongest and weakest months, seasonal patterns and any months where strong sales were accompanied by weak margin. |
| **Regional performance** | Rank the regions by Net Sales, Profit and Margin. Explain which regions combine scale and profitability, and identify regions that require management attention. |
| **Store performance** | Create a store scorecard containing Net Sales, Profit, Margin, Units and Average Satisfaction. Rank the stores and flag any store with below-average margin or below-average satisfaction. |
| **Channel performance** | Compare Online, In-store and Click & Collect using Net Sales, Profit, Margin, Units and Average Satisfaction. Explain the strengths, weaknesses and management implications of each channel. |
| **Category performance** | Compare all categories by Net Sales, Profit, Margin, Units, Average Discount and Satisfaction. Identify high-revenue low-margin categories and lower-revenue high-margin categories. |
| **Product performance** | Rank products by Net Sales and Profit. Identify products with high sales but low margin, and products that combine strong margin with strong satisfaction. |

### C. Filter, sort and highlight
| Prompt | Prompt text |
| :--- | :--- |
| **Margin exceptions** | Filter the data to show transactions with Margin below 35%. Sort them from lowest to highest margin and highlight transactions that also have a Discount of 15% or more. |
| **Customer-experience exceptions** | Find transactions with Satisfaction below 4.0. Summarise them by Region, Store, Channel, Category and Promotion, and identify where low scores are concentrated. |
| **High-value transactions** | Show the top 20 transactions by Net Sales. Include Region, Store, Channel, Category, Product, Units, Discount, Profit, Margin and Satisfaction. |
| **Online investigation** | Filter the data to Online transactions. Compare Online performance by store, product category and customer segment, then identify the factors most associated with lower satisfaction. |

### D. PivotTables and charts
| Prompt | Prompt text |
| :--- | :--- |
| **Region and channel PivotTable** | Create a PivotTable showing Net Sales and Profit by Region and Channel. Display Margin as Profit divided by Net Sales and add a clustered column chart. |
| **Category and product PivotTable** | Create a PivotTable with Category and Product in the rows, Year in the columns, and Net Sales, Profit and Units in the values. Sort products by total Net Sales. |
| **Monthly trend chart** | Create a monthly line chart comparing Net Sales and Profit for 2024 and 2025. Make the chart suitable for an executive dashboard and add a clear business title. |
| **Customer experience chart** | Create a chart comparing Average Satisfaction by Channel and Customer Segment. Use the chart to identify the combinations with the strongest and weakest customer experience. |

### E. Promotion and discount analysis
| Prompt | Prompt text |
| :--- | :--- |
| **Promotion effectiveness** | Evaluate each Promotion using transaction count, Units, Net Sales, Profit, Margin, Average Discount and Satisfaction. Determine which promotions appear commercially strongest and which require further investigation. |
| **Discount bands** | Group transactions into No Discount, 1–9%, 10–19% and 20% or More. Compare Net Sales, Profit, Margin, Units and Satisfaction across the discount bands. |
| **Discount risk** | Identify products, categories, stores or channels where higher discounts coincide with lower margin. Explain the patterns, but clearly distinguish correlation from causation. |
| **What-if analysis** | Model the effect of reducing the average discount on Seasonal Sale transactions by two percentage points, assuming units remain unchanged. Estimate the change in Net Sales, Profit and Margin and state the assumptions. |

### F. Dashboard prompt
| Prompt | Prompt text |
| :--- | :--- |
| **Build an executive dashboard** | Create an Executive Dashboard on a new worksheet for Contoso Marketplace. Include KPI cards for Net Sales, Profit, Margin, Units, Average Satisfaction and Year-over-Year Sales Growth. Add charts for monthly sales trend, sales by region, profitability by category and channel performance. Include filters or slicers for Year, Region, Channel and Category. Use a clean blue-and-green retail management style. |

---

## Copilot Prompts for the Analyst Agent

*The Analyst agent is best demonstrated with an open-ended business question requiring several analytical steps, rather than a simple calculation.*

### Primary Analyst Prompt
> Act as a senior retail performance analyst for Contoso Marketplace. Analyse the attached retail sales workbook and determine what is driving the change in sales and profit between 2024 and 2025. Investigate performance by month, region, store, channel, category, product, customer segment, promotion and discount level.
> 
> Specifically:
> * Quantify the year-over-year changes in sales, profit, units, margin and satisfaction.
> * Identify the largest positive and negative contributors.
> * Investigate why margin did not grow at the same rate as sales.
> * Examine whether promotions and discounts are producing profitable growth.
> * Identify possible customer-experience risks.
> * Highlight anomalies or results that require validation.
> * Recommend five management actions, supported by evidence.
> 
> Clearly distinguish findings supported by the data from hypotheses requiring additional information. Present the results as an executive summary followed by detailed supporting analysis.

### Useful Analyst Follow-Ups
* **Driver analysis:** Decompose the 2025 sales increase into volume, product mix, category mix, channel mix and regional contribution. Explain which drivers had the greatest effect.
* **Margin investigation:** Investigate the difference between revenue growth and margin performance. Identify the categories, products, channels and promotions that contributed most to margin dilution.
* **Customer experience:** Analyse the relationship between Satisfaction and Channel, Store, Promotion, Discount, Product and Customer Segment. Identify statistically meaningful patterns and avoid claiming causation.
* **Anomaly detection:** Find unusual transactions or groups with unexpected combinations of high sales, low margin, high discount or low satisfaction. Explain why each anomaly deserves investigation.
* **Scenario analysis:** Model three scenarios for the next period: continue the current mix, increase Click & Collect sales by 20%, and shift 5% of Electronics sales toward Apparel and Beauty. Estimate the potential revenue, profit and margin implications and document every assumption.

---

## Copilot Prompts for Word

*First, use the Excel output, dashboard, or Analyst response as the source material.*

| Prompt | Prompt text |
| :--- | :--- |
| **Management performance report** | Using the attached Contoso Marketplace retail sales workbook and the analysis from Excel, create a professional quarterly retail performance report for the executive leadership team. Include: Executive summary, Overall performance, Year-over-year comparison, Region and store performance, Channel performance, Category and product performance, Promotion and discount effectiveness, Customer satisfaction risks, and Recommended management actions. Support findings with figures from the source material. Clearly distinguish confirmed findings from hypotheses. |
| **Concise board paper** | Convert the retail analysis into a two-page board paper for Contoso Marketplace. Focus on the business implications of growth, margin pressure, channel performance, promotional effectiveness and customer experience. End with five decisions or actions required from leadership. |
| **Store-manager briefing** | Rewrite the analysis as a practical briefing for Contoso Marketplace store managers. Use accessible language and focus on actions managers can influence, including product mix, discount discipline, Click & Collect, customer satisfaction and local store performance. |
| **Action plan** | Create a 90-day action plan from the retail report. Use a table with Action, Business Rationale, Suggested Owner, Success Measure, Priority and Timeframe. Do not invent named employees. |
| **Executive polishing** | Review this report for repetition, unsupported claims and overly technical language. Rewrite it into a concise executive style while preserving the figures, conclusions and recommended actions. |

---

## Copilot Prompts for PowerPoint

*Attach the completed Word report or open it as the source for the presentation.*

### A. Executive presentation
> Create an eight-slide executive presentation from this Contoso Marketplace retail performance report.
> 
> Use this structure:
> 1. Title and management question
> 2. Executive performance snapshot
> 3. Year-over-year performance
> 4. Region and store performance
> 5. Channel performance
> 6. Category, product and promotion insights
> 7. Risks and opportunities
> 8. Recommended actions and next steps
> 
> Keep each slide concise, use charts where the source contains suitable data, and use an Australian retail executive tone.

### B. Narrative-focused presentation
> Turn this report into a presentation with the storyline: “Strong growth, but protect the quality of growth.” Begin with the positive revenue result, introduce the margin and customer-experience tensions, identify the performance drivers, and finish with clear management actions.

### C. Presentation refinement
> Review the presentation as if it will be delivered to the Contoso Marketplace executive leadership team. Simplify crowded slides, improve slide titles so they communicate conclusions, remove repeated content and ensure every recommendation is supported by information in the report.

### D. Speaker notes
> Add speaker notes for each slide. Explain the key message, the evidence to mention and one likely executive question. Keep each set of notes suitable for approximately one minute of speaking.

---

## Recommended Demonstration Flow

1. Ask Copilot in Excel to explain the workbook.
2. Ask for the most important management columns.
3. Generate a year-over-year executive summary.
4. Compare channels and categories.
5. Create a PivotTable and chart.
6. Build the Executive Dashboard.
7. Give the workbook to the Analyst agent for deeper driver analysis.
8. Use the results to create a Word management report.
9. Convert the report into an eight-slide PowerPoint presentation.
10. Finish by asking Copilot to create speaker notes and recommended actions.
