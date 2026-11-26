# Store Replenishment & Markdown Advisor

## Scenario

A regional store operations lead reviews stock health every Monday across several stores. Each store has its own stock levels, sales speed, deliveries on order, and promotions. The lead has to decide, for each risky item, whether to transfer stock, expedite a delivery, start a markdown, or do nothing.

The Store Replenishment & Markdown Advisor reads the inventory snapshot, supplier lead times, promotion calendar, and the markdown policy. It returns a prioritised list of actions with the reason for each one, and it says clearly when it cannot decide.

---

## Pain Points

### Stock Problems Found Too Late
- Stockouts and overstocks are spotted in weekly spreadsheets, often after sales have already been lost.
- Each store reviews its own numbers, so regional patterns are missed.

### Transfers and Markdowns Decided Inconsistently
- Some managers transfer stock first, others mark down straight away.
- Policy rules such as markdown caps and promotion conflicts are hard to remember and easy to break.

### Delivery Gaps Go Unnoticed
- An on-order delivery can arrive after the item has already sold out.
- Supplier reliability is rarely taken into account in weekly planning.

---

## Benefits

### Prioritised Weekly Stock Review
- Ranks stockout and overstock cases by risk, so the most urgent ones come first.
- Each recommendation includes the numbers behind it.

### Consistent Application of Policy
- Applies the same transfer-before-markdown and markdown-cap rules to every store.
- Flags conflicts, such as a markdown on an item that is already on promotion.

### Earlier Warning on Delivery Gaps
- Compares weeks of cover with the next delivery date and flags gaps.
- Suggests expedite requests or transfers where a gap is found.

### Clear Limits
- States when data is stale, missing, or outside policy, and does not guess.

---

## Demo

### Agent Name

**Store Replenishment & Markdown Advisor**

### Description

The Store Replenishment & Markdown Advisor helps store operations and merchandising teams review stock health across stores. It turns an inventory snapshot, supplier lead times, promotions, and markdown policy into a prioritised weekly action list with clear reasons.

### Instructions

You are a Store Replenishment & Markdown Advisor for a multi-store retailer.

Your role is to help store operations and merchandising leads reduce stockouts and overstock, using only the approved knowledge sources.

When responding:

- Summarise stock health by store and by category, using the inventory snapshot.
- List every SKU-store pair flagged as "Stockout risk" or "Overstock risk".
- For each stockout risk, check the on-order delivery date against the weeks of cover and say whether there is a gap.
- For each overstock risk, first look for a transfer to another store in the same region that is under 4.0 weeks of cover, and then check the markdown policy.
- Never recommend a transfer to or from a store in a different region.
- Apply the markdown caps and promotion conflict rules from the markdown policy, and name the rule you applied.
- Add one extra week to any cover calculation for suppliers below 90% on-time reliability, as the policy requires.
- Give a prioritised action list for the next 7 days, ordered by risk and then by value.
- The demo as-of date is 2025-06-06, the snapshot date. Treat it as today's date. If the snapshot is more than 7 days older than the as-of date, say so before giving any recommendation. Do not use the real current date.
- If information is missing or unclear, say what is missing. Do not guess.
- End with a short list of items that need a human decision.

### Started Prompts

#### Weekly Stock Health

> Give me a stock health summary for all stores, with the number of stockout and overstock cases by store.

#### Transfer Options

> Which overstock items in Metro North could cover a stockout at another Metro North store?

#### Delivery Gaps

> Which stockout items will run out before their next delivery arrives?

### Knowledge Sources

> **Download the demo knowledge source package from:**
> `data files`
>
> Upload all files from this package as **Knowledge Sources** in Agent Builder before testing the agent. The package contains fictional store, product, inventory, supplier lead time, promotion, and markdown policy data. See [setup.md](./setup.md) for configuration steps.

### Demo Prompt

```text
Prepare the weekly store replenishment review for all stores.

Include:
1. A summary of stockout and overstock cases by store and category.
2. For each stockout case, whether the on-order delivery arrives before the stock runs out.
3. For each overstock case, whether a same-region transfer is possible, and if not, what markdown the policy allows.
4. Any promotion or policy conflicts.
5. A prioritised 7-day action list.
6. The items that need a human decision.

State clearly if the data is stale or incomplete.
```

### Expected Results (for the presenter)

These checks confirm the demo works as intended. The snapshot date is 2025-06-06.

| Case | Expected behaviour |
|------|--------------------|
| Pine Street, Ceramic Mug 4-Pack (stockout, 0.8 weeks cover) | Recommends a transfer from Harbor Central (Metro North, 11.0 weeks cover). Notes the 48 units on order for 2025-06-16, which arrives after the stock runs out. |
| Pine Street, Insulated Water Bottle (stockout, 1.5 weeks cover) | Notes the 36 units on order for 2025-06-18, which arrives after the stock runs out. Recommends an expedite request. Does not recommend a transfer from Harbor Central, which is also short on water bottles (0.8 weeks cover). |
| Hillcrest, Bamboo Cutting Board (stockout, 0.8 weeks cover) | Recommends a transfer from Riverside (Coastal East, 6.0 weeks cover), or an expedite. Notes the 12 units on order for 2025-06-20. |
| Riverside or Hillcrest, any item | Does not recommend a transfer from Metro North, because it is a different region. |
| Harbor Central, Trail Runner Shoe (overstock, 11.0 weeks cover) | Looks for a same-region transfer, finds none (Pine Street is at 7.6 weeks), then applies the markdown caps. |
| Any response | States that the snapshot is current (2025-06-06) and that the recommendations need manager confirmation. |

---

## Files in this use case

| File | Purpose |
|------|---------|
| `README.md` | This file: scenario, agent instructions, prompts, and the demo flow |
| [setup.md](./setup.md) | Step-by-step configuration of the agent in Agent Builder |
| `../data files/Store Replenishment Demo Pack/` | Fictional knowledge source files (Excel and text) |

The data is fictional. Do not use real customer, store, or supplier data in this demo.
