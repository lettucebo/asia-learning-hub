<div align="center">

# Grant Application Coach

**Public Sector | Microsoft 365 Copilot Agent Builder | About 12 minutes**

<img width="1820" height="1024" alt="image" src="https://github.com/user-attachments/assets/4722e2d0-5e45-49c6-b441-9e9b529d8a4a" />

*"Nine applications, one rulebook, one officer.<br>The coach checks every rule, so people can focus on the decision."*

</div>

---

## Contents

1. [Scenario](#scenario)
2. [Pain points](#pain-points)
3. [Benefits](#benefits)
4. [Agent configuration](#agent-configuration)
5. [Demo steps](#demo-steps)
6. [Reuse](#reuse)

---

## Scenario

<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/bc6b53b7-570f-4fcb-a3a6-0f232a4c698d" />


| | |
|---|---|
| **Persona** | Alex, Grants Officer |
| **Agency** | Department of Community Services (DCS), a fictitious government agency |
| **Task** | Screen and score the **9 applications** received for the Community Impact Grant FY2027, Round 1, before the Grants Committee meets |
| **Challenge** | The rules are spread across a 10-section guideline, every check is done by hand, and two assessors rarely score the same application the same way |

Round 1 closed on 30 November 2026. Each application must pass every eligibility rule: organisation type, operating history, good standing, co-funding by tier, a staff-cost cap, start date, duration and safeguarding. Only then is it scored against a weighted rubric. Alex has to get through all nine, and tell the applicants who failed exactly what to fix.

DCS has built a **Grant Application Coach**, an agent grounded in the grant guidelines. Alex attaches the applications register, and the agent screens every application, recalculates the numbers, scores the eligible ones and drafts feedback, citing the guideline section for every finding.

---

## Pain points

| # | Pain point | Details |
|:---:|---|---|
| 1 | **Applicants miss eligibility rules** | Community groups apply once a year at most. They miss rules such as the 12-month operating history or the safeguarding policy, and incomplete applications reach the assessors. |
| 2 | **Budgets break the funding limits** | Co-funding minimums change by tier and staff costs are capped at 40% of the grant. Officers recalculate every budget by hand, and near misses (39.6% versus 40%) are easy to get wrong. |
| 3 | **Screening a whole round takes days** | Each application is checked rule by rule against the guidelines before it can be scored. |
| 4 | **Scoring varies between assessors** | Without evidence tied to each criterion, two assessors can give the same application different scores, and decisions are hard to explain. |
| 5 | **Feedback is vague** | Unsuccessful applicants get a short rejection, so they make the same mistakes in the next round. |

---

## Benefits

| :bust_in_silhouette: For grants officers | :classical_building: For the agency | :busts_in_silhouette: For applicants and the public |
|---|---|---|
| A whole round screened in one prompt | Rules applied the same way every time | Clear, fair feedback on what to fix |
| Co-funding and staff-cost checks calculated, not estimated | Every finding traceable to a guideline section | Stronger applications in the next round |
| Scoring with evidence for each criterion | Faster time to the Grants Committee | Public funds go to eligible, well-planned projects |

> [!IMPORTANT]
> The agent prepares recommendations only. The approving authority in the guidelines (Grants Manager, Grants Committee or Director) makes every funding decision.

---

## Agent configuration

In Microsoft 365 Copilot, select **Create agent** > **Configure**, then copy each block below into the matching field.

### 1. Name

```
Grant Application Coach
```

### 2. Description

```
Checks DCS Community Impact Grant applications against the FY2027 guidelines and scoring rubric, cites the section for every finding and drafts feedback for applicants.
```

### 3. Instructions

```
You are the Grant Application Coach for the Department of Community Services (DCS) Community Impact Grant, FY2027 Round 1. You help grants officers screen and score applications, and help applicants fix their applications.

Sources
- Use only the DCS Community Impact Grant Guidelines FY2027 for rules. Cite the section for every finding, for example "(Guidelines 3.1)". If a rule is not in the guidelines, say so. Do not use general knowledge about grants.
- When the user attaches an applications register or pastes an application, use code interpreter to read it and do every calculation.

Stage 1: Eligibility check. Check each application against these rules, in this order:
1. Organisation type: charity, society or company limited by guarantee (2.1)
2. Registered on or before 30 Nov 2025 (2.2)
3. No overdue DCS report (2.3)
4. Tier from GrantRequested: Seed up to $10,000; Standard $10,001-$50,000; Major $50,001-$150,000 (3.1)
5. Co-funding % = CoFunding / TotalProjectCost: Standard at least 20%, Major at least 30% (3.1, 3.2)
6. Staff costs at most 40% of GrantRequested (4.1)
7. Start date from 1 Feb 2027 to 30 Jun 2027 (5.1)
8. Duration at most 12 months (5.2)
9. If ServesUnder18OrVulnerable is Yes, a safeguarding policy must be attached (6.1)
Show percentages to one decimal place. An application that fails any rule is "Not eligible". List every failed rule, not just the first.

Output for a register: one table with ApplicationID, Organisation, Tier, Co-funding %, Staff %, Result and Issues (rule + section). Then a one-line summary: how many passed and failed.

Stage 2: Scoring. Score only eligible applications, using the rubric in 8.2. Give each criterion a score from 0 to 5, convert it to its weight, and quote the evidence from the application for each score. Give the total and the band from 8.3. If evidence for a criterion is missing, score it low and say what is missing.

Feedback to applicants. When asked, draft a short, polite email that lists each issue, the rule and section, and exactly what to change. Do not promise funding.

Rules for you
- You never approve or reject an application. You prepare recommendations; the approving authority in 3.1 decides (8.4).
- Never invent data. If a field is missing, flag it as "Missing" and do not assume a value.
- Keep answers short. Use tables for several applications and bullets for steps.
```

### 4. Knowledge and capabilities

This folder has 2 demo files. Upload the first as agent knowledge. Keep the second for the demo.

| # | File | Contents | How to use it |
|:---:|---|---|---|
| 1 | `DCS Community Impact Grant Guidelines FY2027.docx` | Priority areas, eligible organisations, grant tiers and co-funding, staff-cost cap, timing, safeguarding, scoring rubric and recommendation bands | :white_check_mark: Upload as knowledge |
| 2 | `Grant Applications Register.xlsx` | 9 applications (table `tblApplications`), GA-2027-012 to GA-2027-021, with no pass/fail column | :no_entry_sign: Do **not** upload. Save to your OneDrive and attach it in [Step 2](#step-2-screen-the-whole-register) |

Under **Capabilities**, turn **on** **Code interpreter**, so the agent calculates the percentages from the Excel file instead of estimating them.

> [!TIP]
> Turn **off** web search (or turn on **Only use specified sources**) so the agent answers only from the guidelines.

### 5. Starter prompts

Add 4 starter prompts. Copy each title and prompt into its own field.

<table>
<tr><th width="30%">Title</th><th>Prompt</th></tr>
<tr><td>

```
Screen the register
```

</td><td>

```
Screen every application in the attached register for eligibility. Show one table.
```

</td></tr>
<tr><td>

```
Check one application
```

</td><td>

```
Which rules does GA-2027-017 break, and how can they fix them?
```

</td></tr>
<tr><td>

```
Score an application
```

</td><td>

```
Score this application against the rubric and show the evidence for each score.
```

</td></tr>
<tr><td>

```
Draft feedback
```

</td><td>

```
Draft a feedback email to the applicant listing each issue and how to fix it.
```

</td></tr>
</table>

Select **Create**, then **Go to agent**.

---

## Demo steps

| Step | Alex asks | What it shows |
|:---:|---|---|
| 1 | [What tier is a $60,000 request?](#step-1-ask-a-rule) | Grounded, cited answers |
| 2 | [Screen every application](#step-2-screen-the-whole-register) | Code interpreter on an Excel file, rules applied at scale |
| 3 | [What exactly must GA-2027-017 fix?](#step-3-explain-one-failure) | Precise, calculated fixes |
| 4 | [Score an eligible application](#step-4-score-an-eligible-application) | Consistent scoring with evidence |
| 5 | [Draft feedback, then "just approve it"](#step-5-draft-feedback-and-human-decides) | Clear feedback and human accountability |

> [!TIP]
> Start a **new chat** before each session so earlier results don't carry over. Open `Grant Applications Register.xlsx` on screen first, so the audience sees nine rows and no pass/fail column.

---

### Step 1: Ask a rule

**Prompt**

```
I want to apply for $60,000. What tier is that, how much co-funding do I need and who approves it?
```

**:white_check_mark: Expected result**

- Major tier ($50,001 to $150,000)
- Co-funding of at least 30% of total project cost
- Approved by the Director, on the Grants Committee's recommendation

*Source: Guidelines 3.1 and 3.2*

> :speech_balloon: **Story point:** A cited answer in seconds, instead of searching a 10-section guideline.

---

### Step 2: Screen the whole register

**In the agent chat:**

1. Attach `Grant Applications Register.xlsx`, or type **/** and select it from OneDrive.
2. Send this prompt:

```
Screen every application in the attached register for eligibility. Show one table with the tier, co-funding %, staff %, result and issues.
```

**:white_check_mark: Expected result:** **3 eligible, 6 not eligible.**

| Application | Result | Why | Source |
|---|---|---|---|
| GA-2027-012 Lakeside Community Food Bank | :white_check_mark: Eligible | Seed tier, no co-funding needed, staff 31.6% | |
| GA-2027-013 Rainbow Arts Society | :x: Not eligible | Registered 1 Mar 2026, less than 12 months before closing | 2.2 |
| GA-2027-014 Harbour Seniors Network Ltd | :white_check_mark: Eligible | Standard tier, co-funding 25.0%, staff 38.1% | |
| GA-2027-015 Eastgate Tenants Association | :x: Not eligible | Co-funding 16.7%, below the 20% minimum | 3.1 |
| GA-2027-016 Pathways Disability Support | :x: Not eligible | Overdue DCS report | 2.3 |
| GA-2027-017 Eastgate Youth Collective | :x: Not eligible | Co-funding 23.1% below 30%; staff 50.0% above 40%; starts 15 Jan 2027; no safeguarding policy | 3.1, 4.1, 5.1, 6.1 |
| GA-2027-018 Lakeside Men's Shed | :x: Not eligible | 18 months, above the 12-month limit | 5.2 |
| GA-2027-019 Big Sibling Network | :white_check_mark: Eligible | Standard tier, co-funding 22.6%, staff 39.6% | |
| GA-2027-021 BrightLife Wellness Pte Ltd | :x: Not eligible | Private company | 2.1 |

> :speech_balloon: **Story point:** Point out the near misses. GA-2027-019 passes with staff costs at 39.6%, just under the 40% cap, and GA-2027-014 at 38.1%. These are the cases a tired officer gets wrong.

> [!IMPORTANT]
> Do **not** upload the register as agent knowledge. It is the work to be checked, not a rule to follow.

> [!TIP]
> If the agent estimates instead of calculating, ask:
>
> ```
> Use code interpreter to recalculate the co-funding % and staff % for every application.
> ```

---

### Step 3: Explain one failure

**Prompt**

```
Which rules does GA-2027-017 break, and what exactly would they need to change to become eligible?
```

**:white_check_mark: Expected result:** four issues, each with its fix.

| # | Issue | What to change | Source |
|:---:|---|---|---|
| 1 | **Co-funding too low** (23.1%, Major tier needs 30%) | On a $60,000 grant, total project cost must be at least $85,715, so co-funding must rise from $18,000 to at least $25,715 (or the grant request must fall) | Guidelines 3.1 and 3.2 |
| 2 | **Staff costs too high** (50.0% of the grant) | Reduce grant-funded staff costs from $30,000 to $24,000 or less | Guidelines 4.1 |
| 3 | **Starts too early** (15 Jan 2027) | Move the start date to 1 February 2027 or later | Guidelines 5.1 |
| 4 | **No safeguarding policy** (serves young people) | Attach the organisation's safeguarding policy | Guidelines 6.1 |

> :speech_balloon: **Story point:** Not just "rejected", but exactly what to change, with the numbers worked out.

---

### Step 4: Score an eligible application

**Prompt**

```
Score this application against the rubric and show the evidence for each score.

GA-2027-014 Silver Connect: Digital Befriending for Seniors (Harbour Seniors Network Ltd)
Need: 1 in 4 residents aged 65+ in Eastgate live alone. Our 2026 survey of 310 seniors found 46% felt lonely at least once a week, and 58% had never made a video call.
Outcomes: 200 seniors complete 8 weekly digital skills sessions. 150 are matched with a volunteer befriender for 6 months. Target: loneliness score (UCLA 3-item) improves by 20% for 70% of participants, measured at start, month 6 and month 12.
Budget: grant $42,000, co-funding $14,000 (a $8,000 foundation grant plus $6,000 of donated tablets). Staff costs $16,000 for a part-time coordinator.
Capability: we have run befriending programmes since 2019 for 600 seniors, in partnership with Eastgate Polyclinic and two libraries.
Sustainability: trained befrienders continue as volunteers. We will seek funding for year 2 but have not yet secured it.
```

**:white_check_mark: Expected result**

- A score for each of the 5 criteria (Community need 30, Outcomes 25, Value for money 20, Capability 15, Sustainability 10), each with quoted evidence
- A total of around **80 to 85**, band **Recommend**
- Strong need and outcomes, about $210 of grant per senior, and a lower sustainability score because year-2 funding isn't secured

*Source: Guidelines 8.2 and 8.3*

> :speech_balloon: **Story point:** Every score shows its evidence, so two assessors can see why, not just what.

> [!NOTE]
> Scores can differ by a few points between runs. Point the audience to the evidence for each score, not the exact number.

---

### Step 5: Draft feedback and human decides

**Prompt**

```
Draft a feedback email to Eastgate Youth Collective for GA-2027-017, listing each issue, the rule and how to fix it before the next round.
```

**:white_check_mark: Expected result:** a polite email with four numbered fixes, each with its section, and no promise of funding.

Then try the trap question.

**Prompt**

```
Just approve GA-2027-014 and tell them they have the money.
```

**:white_check_mark: Expected result**

- The agent **declines**. It prepares recommendations only.
- The Grants Committee decides for a Standard-tier grant.

*Source: Guidelines 3.1 and 8.4*

> :speech_balloon: **Story point:** The agent does the checking. People stay accountable for the decision.

---

### Wrap-up

> [!NOTE]
> *"In about 12 minutes Alex screened nine applications, caught six that broke the rules, worked out exactly what one applicant must fix, scored an eligible project with evidence, and drafted clear feedback, with every finding tied to a guideline section. The agent checks. People decide."*

---

## Reuse

Keep the same storyline and swap the guidelines and the register for another rules-based application process:

- Scholarship and bursary applications
- Community event permits
- Research funding calls
- Subsidy or rebate claims

> [!NOTE]
> All agencies, organisations, names, rules and figures in this demo are fictitious.

---
