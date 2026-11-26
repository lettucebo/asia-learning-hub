# Dealer Service & Recall Readiness Assistant

## Scenario

A regional field service manager is preparing for a campaign execution review and needs a clear view of recall readiness across dealers.

To run an effective review, the manager must understand campaign closure progress, dealer backlog aging, parts ETA constraints, and customer complaint themes.

However, this information is distributed across campaign trackers, service systems, logistics reports, and customer feedback channels.

The Dealer Service & Recall Readiness Assistant acts as an AI-powered field operations advisor that consolidates this data and produces a prioritized readiness briefing in seconds.

---

## Pain Points

### Time-Intensive Recall Preparation
- Regional teams spend significant time collecting status updates from multiple sources.
- Delays in preparation reduce the quality and speed of field decisions.

### Fragmented Dealer Performance Visibility
- Campaign progress, backlog metrics, and parts availability are tracked separately.
- Field teams struggle to compare dealer execution risk on one screen.

### Campaign Delay and Compliance Risk
- Part shortages and aging backlog can slow recall closure rates.
- Late risk detection can increase customer dissatisfaction and audit exposure.

### Inconsistent Regional Prioritization
- Dealer escalation decisions can vary by manager and region.
- Actions are not always ranked by business impact and urgency.

---

## Benefits

### Faster Readiness Briefings
- Reduces manual effort required for campaign review preparation.
- Delivers a ready-to-use regional status summary.

### 360-Degree Dealer Execution View
- Consolidates closure rates, backlog aging, parts ETA, and complaint trends.
- Helps field operations teams align on a common risk picture.

### Better Short-Term Field Decisions
- Identifies high-risk dealers early.
- Recommends practical actions for the next 24-48 hours.

### Improved Customer Experience Outcomes
- Supports proactive communication on delays and ETAs.
- Helps reduce repeat visits and unresolved service complaints.

---

## Demo

### Agent Name

**Dealer Service & Recall Readiness Assistant**

### Description

The Dealer Service & Recall Readiness Assistant helps automotive field operations teams prepare for recall governance by consolidating dealer execution insights, parts constraints, and customer signals into a single executive-ready readiness briefing.

### Instructions

You are a Dealer Service & Recall Readiness Assistant for an automotive OEM.

Your role is to help regional service teams improve recall completion and reduce service backlog risk.

When responding:

- Summarize campaign status by region and dealer.
- Highlight open recall cases, aging backlogs, and part shortages.
- Identify high-risk dealers based on throughput and complaint trends.
- Recommend prioritized actions for the next 48 hours.
- Include suggested customer communication themes where relevant.
- Present findings in a structured field operations briefing format.
- Use only information available from approved enterprise sources.
- If information is unavailable, clearly state what data is missing.

### Started Prompts

#### Regional Readiness

> Prepare recall readiness summary for the South region.

#### Dealer Risk

> Which dealers are highest risk for RC-47 delay?

#### 48-Hour Field Plan

> What should field operations do in the next 2 days to improve closure rate?

### Knowledge Sources

> **Download the demo knowledge source package from:**  
> `industry/Automotive/Agent Builder/data files/Recall Readiness Demo Pack`
>
> Upload all files from this package as **Knowledge Sources** in Agent Builder before testing the agent. The package contains fictional campaign status data, dealer backlog metrics, parts ETA constraints, and complaint theme summaries designed for the Dealer Service & Recall Readiness Assistant demo.

### Demo Prompt

```text
Prepare an executive recall readiness briefing for campaign RC-47.

Include dealer-wise closure progress, backlog aging, parts ETA constraints, complaint trend themes, top risk dealers, and prioritized 48-hour actions.

Clearly identify any missing information or items requiring specialist validation.
```
