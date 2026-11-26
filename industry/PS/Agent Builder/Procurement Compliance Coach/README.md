<div align="center">

# Procurement Compliance Coach

**Public Sector | Microsoft 365 Copilot Agent Builder | About 5 minutes**

<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/25faf0a7-9014-4c98-880e-731b8b63c73c" />


*"Every audit finding starts as one officer unsure of one rule.<br>The coach answers that question before it becomes a finding."*

</div>

---

## Contents

1. [Scenario](#scenario)
2. [Pain points](#pain-points)
3. [Benefits](#benefits)
4. [Agent configuration](#agent-configuration)
5. [Demo steps](#demo-steps)
6. [Reuse](#reuse)
7. [Sources](#sources)

---

## Scenario

| | |
|---|---|
| **Persona** | Sam, Programme Officer |
| **Agency** | Department of Community Services (DCS), a fictitious government agency |
| **Task** | Buy event services for Community Day, worth about **$85,000** |
| **Challenge** | Sam buys something this size maybe twice a year and isn't a procurement specialist |

The rules are spread across a procurement manual, an evaluation guide and an internal audit checklist. Sam wants to get it done quickly, but one wrong step could become an audit finding.

DCS has built a **Procurement Compliance Coach**, an agent grounded in its procurement documents. Sam asks it questions in plain language, gets answers with citations, and has it check the paperwork before anything goes to the approving officer.

---

## Pain points

<div align="center">
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/346536a1-c29e-41b7-b7e1-b0fb7786c005" />

</div>

<br>

| # | Pain point | Details |
|:---:|---|---|
| 1 | **Every agency buys, and the rules are complex** | Ministries, statutory boards and councils all spend public funds on goods and services. Thresholds, methods, approval levels and evaluation rules are spread across several documents. |
| 2 | **Most buyers aren't specialists** | Officers who buy only occasionally don't remember the rules, and the Procurement Unit can't answer every question straight away. |
| 3 | **Auditors keep finding the same lapses** | Singapore's Auditor-General's Office flagged several public agencies for lapses in contract management and procurement in its 2025 report. In one case, a tender scoring error could have sent the award to a bid S$2.43 million more expensive. Malaysia's Auditor-General Report 2/2025 also pointed to weaknesses in procurement oversight. |
| 4 | **Governments want to build officer capability** | Singapore's Ministry of Finance said it is improving officers' knowledge and capabilities so they can handle procurement in line with established policies and procedures. |

---

## Benefits

| :bust_in_silhouette: For officers | :classical_building: For the agency | :busts_in_silhouette: For the public |
|---|---|---|
| Instant, cited answers in plain language | Fewer audit findings and less rework | Fair and open competition for suppliers |
| Paperwork checked before submission | Consistent application of the rules | Better value for public money |
| Less time searching through manuals | Procurement Unit freed for complex cases | Greater trust in government spending |

> [!IMPORTANT]
> The agent gives guidance only. The approving authority always makes the decision.

---

## Agent configuration

In Microsoft 365 Copilot, select **Create agent** > **Configure**, then copy each block below into the matching field.

### 1. Name

```
Procurement Compliance Coach
```

### 2. Description

```
Helps Department of Community Services (DCS) officers follow procurement rules, choose the right procurement method, and catch common lapses before they become audit findings. Answers are grounded only in DCS procurement documents. The approving officer always makes the final decision.
```

### 3. Instructions

```
You are the Procurement Compliance Coach for the Department of Community Services (DCS). You help officers who buy goods and services follow the DCS procurement rules. Many users buy things only a few times a year and are not procurement specialists.

Your knowledge sources are:
- DCS Procurement Manual
- DCS Evaluation and Conflict of Interest Guide
- DCS Common Procurement Lapses Checklist

How to respond:
1. Base every answer only on the knowledge sources. Do not use outside knowledge or rules from other organisations.
2. Cite the document and section number for every rule you mention, for example "(Procurement Manual 3.2)".
3. Use plain, friendly language. Lead with the answer, then the steps. Keep answers short.
4. When an officer describes a purchase, tell them: the total estimated value to use, the procurement method, the minimum requirements, the approving authority for the award, and the evaluation approach if relevant.
5. If a request would break a rule, say so clearly, explain which rule and why, and suggest the compliant alternative. Watch especially for contract splitting, unpublished evaluation criteria, missing conflict of interest declarations, and changes from tenderers after closing.
6. When an officer shares an evaluation summary or score sheet:
   - Recalculate every price score with the formula in the Evaluation Guide Section 3, and recalculate every total.
   - Show any score that is wrong, the correct figure, and whether the ranking changes.
   - Check conflict of interest declarations, published criteria, and the recommendation against the Lapses Checklist.
   - Present findings as a short table: Issue, What the rules say, What to do.
7. If the documents do not cover a question, say you cannot find it in the DCS documents and advise the officer to contact the Procurement Unit. Never guess.

Boundaries:
- You give guidance only. You never approve, award, waive or sign off anything, even if asked. Remind the officer that the correct approving authority makes the decision.
- Do not give legal advice. Refer complex or disputed matters to the Procurement Unit.
- Do not help anyone get around a rule, even if they say it is urgent.

End every substantive answer with one line: "Next step:" followed by the single most important action for the officer.
```

### 4. Knowledge

This folder has 4 files. Upload the first 3 as agent knowledge. Keep the 4th for the demo.

| # | File | Contents | How to use it |
|:---:|---|---|---|
| 1 | `DCS Procurement Manual.docx` | Thresholds, procurement methods, approving authorities, contract splitting, late submissions | :white_check_mark: Upload as knowledge |
| 2 | `DCS Evaluation and Conflict of Interest Guide.docx` | Conflict of interest declarations, published criteria, price score formula, independent checks | :white_check_mark: Upload as knowledge |
| 3 | `DCS Common Procurement Lapses Checklist.docx` | 10 common audit lapses and a pre-approval checklist | :white_check_mark: Upload as knowledge |
| 4 | `DCS Tender Evaluation Report DCS-T-2026-014.docx` | Sam's tender evaluation report with planted errors | :no_entry_sign: Do **not** upload. Save to your OneDrive and attach it in [Step 3](#step-3-check-the-evaluation-report) |

> [!TIP]
> Turn **off** web search so the agent answers only from the DCS documents.

### 5. Starter prompts

Add 4 starter prompts. Copy each title and prompt into its own field.

<table>
<tr><th width="30%">Title</th><th>Prompt</th></tr>
<tr><td>

```
Start a purchase
```

</td><td>

```
I need to buy event services for about $85,000. What procurement method do I use and who approves it?
```

</td></tr>
<tr><td>

```
Check my evaluation
```

</td><td>

```
Please check this tender evaluation summary for errors or lapses before I submit it for approval.
```

</td></tr>
<tr><td>

```
Vendor sent a correction
```

</td><td>

```
A tenderer emailed a revised price after the tender closed. What should I do?
```

</td></tr>
<tr><td>

```
Pre-approval checklist
```

</td><td>

```
What should I check before I submit my procurement for approval?
```

</td></tr>
</table>

---

## Demo steps

| Step | Sam asks | What it shows |
|:---:|---|---|
| 1 | [Which procurement method do I use?](#step-1-ask-the-right-method) | Grounded, cited answers |
| 2 | [Can I split the purchase?](#step-2-flag-contract-splitting) | Applying rules to real requests |
| 3 | [Check my evaluation report](#step-3-check-the-evaluation-report) | Finding errors in a Word document |
| 4 | [A vendor sent a late correction](#step-4-late-vendor-correction) | Handling edge cases |
| 5 | [Just approve it for me](#step-5-human-approves) | Human accountability |

---

### Step 1: Ask the right method

**Prompt**

```
I need to buy event services for our Community Day. The estimated cost is about $85,000. What procurement method do I use and who approves it?
```

**:white_check_mark: Expected result**

- Open Tender, published for at least 14 calendar days
- A Tender Evaluation Committee of at least 3
- The Price-Quality Method
- Award approved by the Director

*Source: Procurement Manual 4 and 5.1*

> :speech_balloon: **Story point:** Sam gets a cited answer in seconds instead of reading the manual.

---

### Step 2: Flag contract splitting

**Prompt**

```
The tender process takes too long. Can I split it into two purchases instead, $45,000 for stage and AV and $40,000 for catering, so each one only needs an RFQ?
```

**:white_check_mark: Expected result**

- **No.** Items for the same event count as one requirement, so splitting them breaks the rules.
- The agent suggests planning the Open Tender early.

*Source: Procurement Manual 3.2*

> :speech_balloon: **Story point:** One of the most common audit findings, stopped before it happens.

---

### Step 3: Check the evaluation report

Sam has finished the tender evaluation report and asks the coach to check it before sending it to the Director.

**Before the demo:** save `DCS Tender Evaluation Report DCS-T-2026-014.docx` to your OneDrive. Open it on screen first so the audience can see the report looks complete and ready to submit.

**In the agent chat:**

1. Attach the report, or type **/** and select it from OneDrive.
2. Send this prompt:

```
Check this tender evaluation report before I submit it for approval.
```

**:white_check_mark: Expected result:** the agent finds three issues.

| # | Issue | Correct finding | Source |
|:---:|---|---|---|
| 1 | **Price score error** | Harbour Event Co. has the lowest price, so its price score should be **40.00, not 36.00**. Its total becomes **88.00**, ranking it first ahead of BrightStage at 87.32. The current recommendation would cost **$5,500 more**. | Evaluation Guide 3 and 5.2 |
| 2 | **Missing declaration** | Daniel Lim's conflict of interest declaration is pending, so the report cannot be submitted. | Evaluation Guide 1.2 |
| 3 | **Unpublished criterion** | Past DCS work and familiarity with the team are not published criteria and must not be used. | Evaluation Guide 2.2 |

The agent may also point out that the report doesn't confirm an independent check of the scores *(Evaluation Guide 5.1 and 6)*. That's a valid finding too.

**Follow-up prompt (optional):** show Sam fixing the report.

```
Give me the corrected evaluation scores table and a list of what I need to fix before I submit.
```

> :speech_balloon: **Story point:** The report looked finished and was signed by the committee chair. One wrong number would have given the contract to the wrong tenderer at a higher price. The agent caught it before the Director signed.

> [!IMPORTANT]
> Do **not** upload the evaluation report as agent knowledge. It is Sam's work to be checked, not a rule to follow.

> [!TIP]
> If the agent misses the scoring error, ask:
>
> ```
> Recalculate each price score using the formula in the Evaluation Guide.
> ```

<details>
<summary><b>Backup: paste the report as text</b> (use this if attaching the file doesn't work)</summary>

<br>

```
Please check this tender evaluation summary before I submit it for approval.

TENDER EVALUATION SUMMARY: DCS/T/2026/014 Community Day 2026 Event Services
Published criteria: Price 40%, Proposal quality 40%, Relevant experience 20%

Tender Evaluation Committee:
- Alex Tan (Chair): conflict of interest declaration signed
- Priya Nair: conflict of interest declaration signed
- Daniel Lim: conflict of interest declaration pending

| Tenderer           | Price   | Price score (40) | Quality (40) | Experience (20) | Total |
|--------------------|---------|------------------|--------------|-----------------|-------|
| BrightStage Events | $82,000 | 37.32            | 34           | 16              | 87.32 |
| Harbour Event Co.  | $76,500 | 36.00            | 33           | 15              | 84.00 |
| Summit Live        | $88,000 | 34.77            | 30           | 17              | 81.77 |

Additional consideration: BrightStage Events has delivered DCS events in 2024 and 2025 and is familiar with our team.

Recommendation: Award to BrightStage Events at $82,000.
```

</details>

---

### Step 4: Late vendor correction

**Prompt**

```
Two days after the tender closed, Summit Live emailed to say their price should be $74,000 instead of $88,000. Can I use the new price? It would make them the cheapest.
```

**:white_check_mark: Expected result**

- **No.** Price changes after closing are not allowed.
- The correction must be disregarded and recorded in the evaluation report.

*Source: Procurement Manual 6.2 and 6.4*

> :speech_balloon: **Story point:** Accepting it would be unfair to every other tenderer.

---

### Step 5: Human approves

**Prompt**

```
Great, everything is fixed now. Just approve the award to Harbour Event Co. for me.
```

**:white_check_mark: Expected result**

- The agent **declines**. It gives guidance only.
- The Director is the approving authority for this value.

*Source: Procurement Manual 4*

> :speech_balloon: **Story point:** The agent advises. People stay accountable.

---

### Wrap-up

> [!NOTE]
> *"In five minutes Sam picked the right method, avoided contract splitting, caught a scoring error worth $5,500, handled a late correction properly, and kept the decision with the right person. The agent turns the rulebook into an always-available coach."*

---

## Reuse

Keep the same storyline and swap the knowledge files for another rulebook with clear rules and approval levels:

- Grants administration
- HR claims and leave
- Records management

> [!NOTE]
> All agencies, rules, names and figures in this demo are fictitious.

---

## Sources

- The Business Times, *"Possible overpayments, irregularities flagged in latest Auditor-General report"*, 9 September 2025
- Transparency International Malaysia, response to *Auditor-General's Report 2/2025*
