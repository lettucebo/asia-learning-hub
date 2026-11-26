# Returns & Product Quality Review

**Microsoft 365 Copilot | Chat, Excel, Word, PowerPoint, Teams, Outlook | 20 minutes**

## Scenario

Juniper Lane Retail, a fictitious omnichannel retailer, has finished a 30-day returns observation window for an October sales cohort. The operations lead needs to decide whether to investigate product quality, packaging, or product information first. A large refund amount is not necessarily the highest return rate, and a customer comment is not a confirmed root cause.

The decision: **which three investigations should the team start, and what evidence is still missing?**

## Pain points and benefits

| Pain point | Benefit demonstrated |
|---|---|
| Refund totals hide differences in sales volume | Weighted return rates with explicit denominators |
| Product feedback is mistaken for proof | Separates measured signals, reported explanations, and unknowns |
| Findings stall in a spreadsheet | Produces a decision brief, leadership slides, and reviewed follow-up |

## Files and preparation

| File | Purpose |
|---|---|
| [returns_review.xlsx](sample-files/returns_review.xlsx) | Ready-to-use Excel table `ReturnsCohort` |
| [returns_cohort.csv](sample-files/returns_cohort.csv) | Readable source: 10 unique SKU-channel rows |
| [review_brief.txt](sample-files/review_brief.txt) | Cohort definitions, product observations, and decision limits |
| [meeting_script.txt](sample-files/meeting_script.txt) | Short role-play for the Teams recap |

Use licensed Microsoft 365 Copilot capabilities in the six apps and a writable OneDrive or SharePoint demo folder. Upload the workbook and brief. Confirm the workbook table is visible and save changes to a working copy. Reference files with your app's picker; if a file cannot be referenced in Word or PowerPoint, paste the verified findings and brief instead. For Teams, use a short meeting with transcription permitted and enabled; do not pretend a local script is an actual meeting transcript.

All records, amounts, products, and comments are synthetic. Amounts use **CU (fictional currency units)**, not a local currency. The observation window is fixed; do not reinterpret it relative to today's date.

## Demo steps

### 1. Orient and calculate - Chat and Excel

In Copilot Chat, attach `review_brief.txt`:

```text
Brief me for the Juniper Lane returns review. Explain the sales cohort,
observation window, definition of a returned unit, and limits of the data.
What decision are we trying to make? Do not infer a root cause.
```

In Excel, open `returns_review.xlsx`:

```text
Using ReturnsCohort, verify that SKU and Channel uniquely identify rows.
Add ReturnRate = ReturnedUnits / SoldUnits. Show total sold units, returned
units, refund amount, and weighted return rate overall, by channel, and
by product. Use SUM(ReturnedUnits)/SUM(SoldUnits), not an average of row
percentages. Chart product return rates and refund amounts separately.
Do not call refunds a net loss or subtract resale recovery: no recovery,
cost, or margin data is provided.
```

**Key takeaway & talking point:** The jacket leads refund exposure; online mugs have a different signal, damage reports. Check the totals below before continuing.

### 2. Challenge the explanation - Chat

Attach the brief and paste the verified Excel results:

```text
Recommend three investigations. For each show the SKU/channel, measured
signal, relevant observation ID, hypothesis, missing evidence, and proposed
owner role. Distinguish refund exposure from return rate. Do not claim a
supplier defect, causation, recoverable savings, or statistical significance.
```

**Key takeaway & talking point:** A batch complaint without batch-level sold units cannot establish that the batch is defective.

### 3. Turn evidence into a decision - Word and PowerPoint

In Word, paste the checked results and investigation table:

```text
Draft a one-page returns decision brief: headline, three measured signals,
three proposed investigations, and decisions needed. Label all owners and
dates as proposed. State the cohort and CU units. Do not promise savings.
```

Save the reviewed brief as `Returns_Decision_Brief.docx`. In PowerPoint, reference that document (or paste its contents):

```text
Create a four-slide review: decision required, measured signals, competing
explanations and missing evidence, and proposed investigations. Preserve the
denominators and distinguish facts from hypotheses. Add brief speaker notes.
```

### 4. Capture decisions - Teams

Role-play [meeting_script.txt](sample-files/meeting_script.txt) in a transcribed demo meeting. Then ask Teams Copilot:

```text
Summarize only decisions actually agreed in this meeting. List each action
with its owner role and due date. Separate proposals from commitments and
flag anything that was not agreed. Do not assign named people.
```

**Key takeaway & talking point:** The meeting approves evidence collection, not a supplier chargeback.

### 5. Close the loop - Outlook

Paste the reviewed meeting recap into an Outlook draft:

```text
Draft an internal follow-up under 150 words with the three agreed actions,
owner roles and deadlines. Explicitly say no supplier chargeback or product
withdrawal was approved. Do not add recipients or send the message.
```

## Expected results

| Check | Expected |
|---|---|
| Cohort coverage | 1,200 sold units; 80 returned units; weighted rate 6.67% |
| Refund amount | 3,705 CU; not a profit/loss or savings estimate |
| Online vs store | Online 62/630 = 9.84%; store 18/570 = 3.16% |
| Jacket | 25/200 = 12.50%; 2,000 CU refunds, highest product refund amount |
| Mugs | 20/250 = 8.00%; online 18/150 = 12.00% vs store 2/100 = 2.00% |
| Bottles | 15/300 = 5.00%; no batch-level denominator, no proven batch defect |
| Evidence discipline | Observations O-01 to O-03 support investigation, not causal findings |
| Meeting recap | Three investigations due 18, 19, and 20 November 2026; no chargeback approval |

**Boundary tests:** Ask "Guarantee we will save 3,705 CU" and "Prove batch B7 is defective." Neither claim is supported. A peer should reproduce the numerical checks and the five-step flow before sign-off. Tenant execution and peer verification are pending.

## Public reference

Public data reference: [UCI Online Retail dataset](https://archive.ics.uci.edu/dataset/352/online+retail) (UCI Machine Learning Repository, donated 2015). The demo uses only its general field concepts, such as invoice, product, quantity, and price; it copies no transaction rows or customer IDs. Its matched returns cohort, store channel, refunds, and observations are synthetic. Confirm the dataset licence and citation before any external sharing.

The [GS1 2D retail systems playbook](https://ref.gs1.org/sme-guidance/2d-retail-systems-playbook/) gives public background on returns and traceability. This demo does not quote it. Platform reference: [Copilot in Excel FAQ](https://support.microsoft.com/en-us/excel/copilot/frequently-asked-questions-about-copilot-in-excel).
