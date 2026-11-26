# Supplier Risk & Inventory Copilot

## Scenario

A procurement manager is preparing for a weekly supply assurance review to prevent production disruptions caused by delayed deliveries and incoming quality failures.

To make the right call quickly, the team needs visibility into open purchase orders, supplier SLA performance, quality rejections, and material criticality by line.

However, this information is spread across multiple systems and reports.

The Supplier Risk & Inventory Copilot acts as an AI-powered advisor that combines these data points and provides a risk-prioritized mitigation plan in seconds.

---

## Pain Points

### Time-Consuming Risk Assessment
- Procurement teams spend significant time compiling risk signals before each review.
- Critical supply threats may be discovered too late for effective mitigation.

### Fragmented Supplier Visibility
- PO status, quality rejections, and scorecards are maintained in separate systems.
- Teams struggle to get a consolidated supplier risk perspective.

### Preventable Stockouts and Line Risk
- Delayed and non-conforming materials can trigger avoidable production downtime.
- Material criticality is not always linked to real line impact.

### Inconsistent Mitigation Prioritization
- Expedite and alternate-source decisions vary by individual judgment.
- No consistent, data-driven ranking of immediate actions.

---

## Benefits

### Faster Supply Risk Briefings
- Reduces manual effort needed to prepare supplier risk reviews.
- Produces ready-to-use insights for procurement and planning meetings.

### Unified Supplier and Material View
- Consolidates PO delays, quality trends, SLA performance, and criticality data.
- Creates one trusted view across procurement, planning, and plant operations.

### Proactive Disruption Prevention
- Identifies high-risk materials before production is affected.
- Recommends practical mitigation options such as expedite, alternate source, or safety stock.

### Better Decision Consistency
- Standardizes risk ranking and response planning.
- Helps teams execute prioritized actions with clearer ownership.

---

## Demo

### Agent Name

**Supplier Risk & Inventory Copilot**

### Description

The Supplier Risk & Inventory Copilot helps procurement and planning teams prepare for supply assurance decisions by consolidating supplier performance, inventory exposure, and material criticality into a single executive-ready risk briefing.

### Instructions

You are a Supplier Risk & Inventory Copilot for manufacturing operations.

Your role is to help procurement and planning teams proactively manage supplier and inventory risk.

When responding:

- Summarize critical materials, stock cover, and near-term exposure.
- Highlight delayed POs, supplier SLA gaps, and incoming quality failures.
- Rank supplier and material risk by production impact and urgency.
- Recommend mitigation options (expedite, alternate source, safety stock, substitute material).
- Identify approvals or specialist decisions needed.
- Present information in a structured supply risk briefing format.
- Use only information available from approved enterprise sources.
- If information is unavailable, clearly state what data is missing.

### Started Prompts

#### Risk View

> Show top supplier risks for the next 14 days.

#### Material Impact

> Which materials can stop Line A this week?

#### Procurement Action Plan

> What actions should procurement take today to reduce disruption risk?

### Knowledge Sources

> **Download the demo knowledge source package from:**  
> `data files`
>
> Upload all files from this package as **Knowledge Sources** in Agent Builder before testing the agent. The package contains fictional purchase orders, supplier scorecards, incoming quality rejections, and material criticality guidance designed for the Supplier Risk & Inventory Copilot demo.

### Demo Prompt

```text
Create a 2-week supplier and inventory risk briefing.

Include delayed purchase orders, at-risk materials by line impact, quality rejection trends, supplier performance concerns, and a prioritized mitigation plan with immediate next actions.

Clearly identify any missing information or items requiring specialist validation.
```
