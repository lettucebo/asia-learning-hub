# Relationship Manager Assistant

## Scenario

A Relationship Manager (RM) in a bank is preparing for an upcoming meeting with a corporate customer. To have a meaningful discussion, the RM needs to understand the customer's business profile, existing banking relationships, recent interactions, outstanding service requests, credit exposure, and potential growth opportunities.

However, this information is spread across multiple systems, documents, and communication channels.

The Relationship Manager Assistant acts as an AI-powered advisor that brings together relevant customer insights and prepares the RM for the conversation in seconds.

---

## Pain Points

### Time-Consuming Preparation
- Relationship managers spend significant time searching multiple systems before every customer meeting.
- Critical information may be overlooked due to fragmented data sources.

### Incomplete Customer View
- Customer information is spread across CRM systems, service tickets, emails, product records, and meeting notes.
- RMs struggle to obtain a consolidated customer perspective.

### Missed Revenue Opportunities
- Potential cross-sell and upsell opportunities may remain undiscovered.
- Product recommendations often depend on individual experience rather than data-driven insights.

### Inconsistent Customer Engagement
- Meeting quality can vary depending on the RM's preparation and experience.
- Important customer concerns or risks may be missed.

### Limited Time for Relationship Building
- RMs spend more time gathering information than engaging strategically with customers.

---

## Benefits

### Faster Meeting Preparation
- Reduces preparation time from hours to minutes.
- Provides a ready-to-use customer briefing.

### 360-Degree Customer View
- Consolidates information from multiple business systems.
- Surfaces customer profile, products, interactions, and service history in one place.

### Increased Revenue Opportunities
- Identifies relevant cross-sell and upsell opportunities.
- Recommends products based on customer needs and behavior.

### Improved Customer Experience
- Enables more personalized and informed conversations.
- Helps RMs proactively address customer concerns.

### Better Risk Awareness
- Highlights overdue actions, service issues, and potential risk indicators.
- Ensures customer discussions are both growth-focused and risk-aware.

### Higher Productivity
- Allows RMs to focus on advisory and relationship-building activities rather than information gathering.

---
## Demo

### Agent Name

**Relationship Manager Assistant**

---

### Description

The Relationship Manager Assistant helps banking relationship managers prepare for customer engagements by consolidating customer information, relationship history, product usage, service interactions, risks, and growth opportunities into a single, easy-to-consume briefing.

The agent acts as a virtual banking advisor, enabling relationship managers to spend less time gathering information and more time building customer relationships and identifying business opportunities.

---

### Instructions

You are a Relationship Manager Assistant for a financial institution.

Your role is to help relationship managers prepare for customer engagements by providing concise, actionable, and data-driven customer insights.

When responding:

- Summarize the customer's profile and relationship history.
- Highlight products and services currently used.
- Surface recent customer interactions and open service requests.
- Identify potential risks, compliance requirements, or pending actions.
- Recommend relevant cross-sell or upsell opportunities where appropriate.
- Suggest discussion topics and next best actions.
- Present information in a structured executive briefing format.
- Be factual and use only information available from approved enterprise sources.
- Do not make investment recommendations or financial decisions on behalf of the bank.
- If information is unavailable, clearly state what data is missing.

---

### Started Prompts

#### Customer Meeting Preparation

> Prepare me for tomorrow's meeting with ABC Manufacturing.

#### Account Review

> Summarize the current banking relationship with ABC Manufacturing.

#### Opportunity Identification

> What growth opportunities should I discuss with ABC Manufacturing?

#### Risk Assessment

> Are there any risks, service issues, or pending actions that I should be aware of before my meeting?

---

### Knowledge Sources

> **Download the demo knowledge source package from:**  
> `industry/FSI/Agent Builder/data files/Relationship Manager Agent Demo Pack.zip`
>
> Upload all files from this package as **Knowledge Sources** in Agent Builder before testing the agent. The package contains fictional customer profiles, meeting notes, product portfolios, service requests, risk summaries, and relationship management guidance specifically designed for the Relationship Manager Assistant demo.

### Demo Prompt

Once the knowledge sources are uploaded, try the following prompt:

```text
Prepare me for my upcoming meeting with ABC Manufacturing.

Provide the customer profile, products currently used, recent discussions, open service requests, risks, potential growth opportunities, recommended questions, and next actions.

Clearly identify any missing information or items requiring specialist validation.
```

