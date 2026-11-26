# Production Downtime Resolution Assistant

## Scenario

A plant supervisor is preparing for the daily production review after repeated unplanned stoppages on a critical packaging line.

To make fast and safe decisions, the supervisor needs a clear view of machine alarms, maintenance history, shift observations, quality impact, and spare-parts readiness.

However, this information is distributed across multiple systems and documents.

The Production Downtime Resolution Assistant acts as an AI-powered operations advisor that consolidates these signals into a concise downtime briefing in seconds.

---

## Pain Points

### Time-Consuming Incident Preparation
- Supervisors spend significant time gathering downtime facts before each review.
- Critical patterns can be missed when data is spread across tools.

### Fragmented Operational Visibility
- Alarm logs, maintenance tickets, and shift notes are disconnected.
- Teams struggle to build a single, shared view of the same incident.

### Delayed Root-Cause Identification
- Repeating machine failures are often treated as isolated events.
- Preventive actions are delayed because trend signals are not surfaced early.

### Inconsistent Corrective Actions
- Different shifts may apply different responses to similar failures.
- Action plans can vary based on experience instead of data.

---

## Benefits

### Faster Downtime Briefings
- Reduces preparation time from manual review to quick AI summaries.
- Provides a ready-to-use incident context for production reviews.

### Unified Line Health View
- Consolidates alarms, maintenance, quality, and parts signals in one place.
- Helps maintenance and production teams align on facts quickly.

### Better Preventive Maintenance Decisions
- Highlights recurring fault patterns and probable failure drivers.
- Supports shift from reactive fixes to prevention-focused actions.

### Improved Operational Consistency
- Encourages structured incident response across shifts.
- Improves follow-through with prioritized actions and owners.

---

## Demo

### Agent Name

**Production Downtime Resolution Assistant**

### Description

The Production Downtime Resolution Assistant helps plant teams prepare for operational reviews by consolidating downtime context, probable causes, open actions, and preventive opportunities into a single executive-ready incident briefing.

### Instructions

You are a Production Downtime Resolution Assistant for a manufacturing plant.

Your role is to support plant supervisors and reliability teams with concise, actionable incident intelligence.

When responding:

- Summarize downtime context (line, machine, shift, duration, and production impact).
- Identify likely root causes using alarms, maintenance history, and shift notes.
- Surface open maintenance and quality actions with blockers.
- Recommend immediate containment actions and preventive actions.
- Flag safety or compliance risks explicitly.
- Suggest discussion points and next best actions for the review meeting.
- Present findings in a structured operations briefing format.
- Use only approved data available in enterprise sources.
- If information is unavailable, clearly state what data is missing.

### Started Prompts

#### Production Review Preparation

> Prepare a downtime briefing for Line P-204 for the last 7 days.

#### Root Cause Review

> Why did machine FM-12 stop repeatedly on the night shift?

#### Prevention Plan

> What preventive actions should we implement this week to reduce repeat downtime?

### Knowledge Sources

> **Download the demo knowledge source package from:**  
> `data files`
>
> Upload all files from this package as **Knowledge Sources** in Agent Builder before testing the agent. The package contains fictional alarm history, maintenance tickets, shift insights, parts inventory, and quality trends designed for the Production Downtime Resolution Assistant demo.

### Demo Prompt

```text
Prepare me for today's production review for Line P-204.

Include downtime summary, most likely root causes, repeated alarm patterns, open maintenance actions, quality impact, safety/compliance concerns, and recommended immediate and preventive actions.

Clearly identify any missing information or items requiring specialist validation.
```
