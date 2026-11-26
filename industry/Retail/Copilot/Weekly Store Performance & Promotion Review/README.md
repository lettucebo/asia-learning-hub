# Weekly Store Performance & Promotion Review

## Scenario

A retail operations manager reviews store performance every week. The review covers sales against target by store and category, the promotions that ran, and what store managers report from the floor. Today this takes hours of spreadsheet work, and the story behind the numbers often gets lost before it reaches the leadership deck.

This use case shows how Microsoft 365 Copilot can move from raw weekly sales data to a clear review pack. It finds the stores and categories that are off target, checks whether promotions explain the change, connects the numbers to store feedback, and drafts the summary email and leadership slides. The manager reviews and edits everything before it goes out.

The sample data is for a fictional retailer, Juniper Lane Retail, across four stores in two regions for four weeks (2025-W19 to 2025-W22).

---

## Pain Points

### Hours Spent Building the Same Report
- Weekly sales, targets and promotion data arrive in different files and layouts.
- Analysts rebuild the same pivot tables and charts every week.

### Numbers Without Context
- A sales drop is visible, but the reason is often in store feedback or a promotion calendar that nobody has linked to the data.
- Leadership asks "why" and the answer takes another day to find.

### Slow Communication
- Store managers hear about problems late.
- Summaries and presentations are written from scratch, so the message changes from week to week.

---

## Benefits

### Faster Weekly Review
- Copilot finds the biggest gaps against target in minutes, not hours.
- The same prompts can be reused every week with new data.

### Context Connected to Numbers
- Copilot links sales trends to promotions and store feedback, and says where the evidence is weak.

### Ready-to-Edit Communication
- Copilot drafts the store manager email, the leadership summary, and a short slide outline.
- The manager checks facts, adjusts tone, and sends.

---

## Sample Files

All files are in the [sample-files](./sample-files/) folder. They are fictional and contain no real customer or employee data.

| File | What it contains | Rows |
|------|------------------|------|
| [store_weekly_sales.csv](./sample-files/store_weekly_sales.csv) | Weekly net sales, target, units, margin and promo flag by store and category | 64 |
| [promo_calendar.csv](./sample-files/promo_calendar.csv) | Promotions with category, weeks, discount, stores, budget and status | 3 |
| [store_feedback.csv](./sample-files/store_feedback.csv) | Short comments from store managers, by week, store and category | 5 |

**Setup tip:** Open `store_weekly_sales.csv` in Excel and convert it to a table (Ctrl+T). Copilot works best on tables with clear headers. Keep the three files in the same folder or upload them together to Copilot.

---

## Demo Flow

The demo runs in five short stages. Each stage builds on the one before. Allow about 45 minutes for a full run, or 15 minutes for a highlights version (stages 1, 3 and 5).

### Stage 1: Find the Gaps (Excel)

Open `store_weekly_sales.csv` in Excel and use Copilot in the table:

> Summarise net sales against target for each store and category across the four weeks. Show the total gap to target and the percentage achieved. Rank the store and category pairs from the largest gap to the smallest.

**What to look for:** Riverside Footwear is the largest gap. Its sales fall from about $51.9k in W19 to about $35.3k in W22, while the target stays at $54k. Riverside is not in the Footwear Refresh promotion.

> Which store and category had the biggest week-on-week drop in net sales? Is the drop in units, in price, or both?

### Stage 2: Check the Promotions (Excel or Word)

Add `promo_calendar.csv` to the same workbook or open it alongside. Then ask:

> Which promotions were active in each store during the four weeks? For each store and category with a gap to target, say whether an active promotion covered it.

**What to look for:** The Footwear Refresh promotion runs at Metro North (Harbor Central and Pine Street) from W19 to W24. Copilot should notice that Riverside, in Coastal East, has no promotion to explain its footwear decline.

> List the promotions that are planned but not yet started. Which of them cover stores with a current gap to target?

### Stage 3: Add the Store Voice (Word)

Open `store_feedback.csv` and ask Copilot to connect it to the numbers:

> Using the store feedback and the sales gaps you found, write a short note for the regional operations lead. For each gap, say what the data shows, what the store said, and what is still unknown.

**What to look for:** At Riverside, customers asked for wider sizes and some left after not finding size 11. That fits the footwear decline but is not proof of it. Copilot should say so. At Harbor Central, the rain jacket sold out in M and L, and promo signage arrived late.

> Mark each point as "data supports", "store feedback only", or "needs more evidence". Do not state a cause as fact unless the data supports it.

### Stage 4: Build the Leadership Pack (PowerPoint)

Create a short slide outline in PowerPoint with Copilot:

> Create a 5-slide outline for the weekly performance review. Slide 1: the headline result. Slide 2: the biggest gaps to target by store and category. Slide 3: promotion coverage. Slide 4: store feedback and what it adds. Slide 5: the actions proposed for next week, with owners to be confirmed.

**Tip:** Copy the sales gap table from Stage 1 into the deck as a native table, not as an image. Copilot can then reuse the numbers.

### Stage 5: Draft the Store Manager Email (Outlook)

Ask Copilot to draft the follow-up:

> Draft a short email to the Riverside store manager about the footwear sales gap for W19 to W22. Ask two questions: what the stock and size availability looked like, and whether any customer requests were not met. Keep it under 150 words and do not blame the store.

**Review before sending:** Check the numbers, the tone, and that the email does not promise any stock, dates or budget that is not in the data.

---

## Copilot Proposes, You Verify

Copilot is a drafting and analysis partner. It does not decide.

- Check every number against the source file before it goes into a deck or email.
- Treat store feedback as the store's view, not as proof.
- Do not share the review pack outside the business without approval.
- Keep the final conclusions and actions with the people accountable for the stores.

---

## Customising for Your Business

To use this with your own data:

1. Keep the same three file shapes: weekly sales by store and category, a promotion calendar, and a feedback log.
2. Keep the same column names, or change the prompts to match your names.
3. Change the store, region and category names in the files. Do not use real customer or employee data in shared demos.
4. Re-run the prompts each week with the new files.

---

## Files in this use case

| File | Purpose |
|------|---------|
| `README.md` | This file: scenario, sample files, demo flow and guidance |
| [sample-files/](./sample-files/) | Fictional sales, promotion and feedback data |

The data is fictional and synthetic. It is for demonstration only.
