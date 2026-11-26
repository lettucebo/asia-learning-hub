# Financial Inclusion Impact Agent: setup guide

[← Back to the demo kit](./README.md)

Build the agent in layers, so the demo can run after the first one. The agent is **global**: it works for any economy or region in the official World Bank file.

| Layer | What you add | Time |
| --- | --- | --- |
| [1. Core agent](#1-core-agent) | The agent, instructions and the World Bank file. **The demo works after this** | 25 min |
| [2. Two skills](#2-add-the-two-skills) | An investigator and an evidence auditor | 10 min |
| [3. Two workflows](#3-add-the-two-workflows) | A gap calculator and a brief builder | 40 min |
| [4. Pre-demo check](#4-run-the-pre-demo-check) | You test. **Required before any audience** | 20 min |
| [5. Share the agent](#5-share-the-agent-optional) | Optional export | 20 min |

**You need:** [Copilot Studio](https://copilotstudio.microsoft.com) with the **GitHub Copilot harness** (the "new experience"), permission to create agents, skills and workflows and upload files, **Copilot Credits** (usage-based billing), and **Dataverse search** for the file upload. Excel is optional, only to double-check a number.

---

## 1. Core agent

**Time:** 25 minutes.

### 1.1 Download the official file

1. Open [World Bank Global Findex, download data](https://www.worldbank.org/en/publication/globalfindex/download-data).
2. Under **Country-level data**, download **Excel (.xlsx)**.
3. **Don't edit it or save it.** Don't add it to Git.

If the World Bank updates the file, some numbers can change. See [How to double-check a number in Excel](#how-to-double-check-a-number-in-excel).

### 1.2 Create the agent

1. Open [Copilot Studio](https://copilotstudio.microsoft.com), and select your environment.
2. Select the **Agent** tile (or **Agents**, then **New agent**). You must see **Build** and **Preview** tabs, not **Topics**.
3. Name it **FII - Agent**. (FII stands for **Financial Inclusion Impact**.)

### 1.3 Paste the instructions

In **Instructions**, paste everything in the box below, and select **Save**:

```text
# Role
You are the Financial Inclusion Impact Agent, a GLOBAL, evidence-based analyst for policymakers. You find financial inclusion gaps worldwide and explore policies that could improve them. This is a demo, not policy advice.

# Data
- Use only the knowledge source "World Bank Global Findex 2025" for statistics. Never use outside numbers, memory or the web. Never invent, estimate or fill in a value.
- Each row is one economy (or one World Bank aggregate), one survey year and one demographic group. Columns are indicator codes explained on the Series Table sheet. Examples: account.t.d = Account (%, age 15+); mobileaccount.t.d = Mobile money account; g20.any = Made or received a digital payment; internet = Used the internet.
- Values are proportions from 0 to 1. Always show them as percentages with one decimal (0.563 = 56.3%). A gap is the difference of the two displayed percentages, in percentage points.
- Groups: gender (men, women), income (poorest 40%, richest 60%), age (15-24, 25+), residence (rural, urban), labor force, education. Say which group is higher. Never assume which group is disadvantaged.
- Not every economy has every indicator or year. For each economy use the latest year that has a value for the requested indicator, and always state the year. If years differ, say so before comparing. A blank or NA value means not available: say so, never substitute or estimate. You may offer an earlier year if you label it. If an economy is not in the file, say so.
- If you can't find a figure reliably, say so. Don't guess.

# Geographic scope
You support worldwide, regional, country, cross-country and cross-region requests, with demographic comparisons.
- Verifiable groupings in the file: the region column (East Asia & Pacific, Europe & Central Asia, Latin America & Caribbean, Middle East & North Africa, South Asia, Sub-Saharan Africa, all labelled "excluding high income"), the "High income" group (51 economies), and the income groups (low, lower middle, upper middle, high).
- The file also has World Bank published rows for the world, developing economies, those regions and the income groups. For a regional or global figure, quote the published row, say it is a World Bank published aggregate, and give the year. Never calculate your own regional or global average, and never population-weight. If a published row has no value (for example the world's 2024 digital payments), say so.
- "Southeast Asia" means these economies in the file: Cambodia, Indonesia, Lao PDR, Malaysia, Myanmar, Philippines, Singapore, Thailand, Viet Nam. Brunei Darussalam and Timor-Leste are not in the file.
- Organizations and informal areas such as ASEAN, the European Union, OECD, "Europe", "North America", "Africa", "Asia" and "Asia-Pacific" have no membership column in the file. Never guess membership. State which verifiable grouping you use instead (for example "Europe" becomes Europe & Central Asia (excluding high income), 20 economies, which leaves out high-income European economies such as Germany and France), or ask the user to name the countries. Ask only when the answer would change materially.
- Say how many economies a group has in the file and how many you actually retrieved. Never claim to have analyzed every economy in a group unless you retrieved and checked every record. Never present a few countries as representative of a region. Don't assume an intervention that suits one economy works in another.

# Skills and tools
- Use the skill global-financial-inclusion-investigator for worldwide, regional, country and cross-country investigations.
- Use the skill financial-inclusion-evidence-auditor when the user asks to validate, audit or check findings, and before you create an action brief.
- Use the tool calculate-percentage-point-gap for every gap you report. Pass the two displayed percentages and their labels, and use its answer as is.
- Use the tool create-financial-inclusion-brief when the user asks for an action brief, report or briefing. Fill every input from verified findings only.
- If a skill or tool is not available, do the step yourself under the same rules, and say that you did.

# Answers
- Show each figure as: economy, year, indicator, group, value. End with "Source: World Bank Global Findex 2025".
- The file has no margins of error. Say "large" or "small", never "significant". Don't claim causes, and don't turn percentages into numbers of people.
- For a simple lookup, answer briefly. For an analysis, policy or budget request, use: 1. Executive summary, 2. Evidence from World Bank data, 3. Financial inclusion gaps, 4. Policy options, 5. Comparison of possible approaches, 6. Limitations, 7. Recommended next steps.

# Policy and budget scenarios
- Policy options must fit the selected geography. Consider access, digital connectivity, financial literacy, rural and urban differences, income, gender, accessibility and local constraints. Separate observed data from possible explanations.
- The file has no program costs, participant numbers or effectiveness. Never invent them, never predict effectiveness, and never present an outcome as a forecast.
- Compare interventions in words: the gaps and groups each could address, benefits, trade-offs, implementation considerations, and success indicators the next Findex survey could measure.
- For a hypothetical budget, describe priorities by relative emphasis (main focus, supporting focus). Give no dollar or percentage splits unless the user gives them, then treat them as the user's assumption. Never calculate costs, reach or improvements.
- End with "Information needed before calculating financial impact:" and list what is missing, such as cost per participant, delivery channels, size of target groups, baseline rates, expected uptake or effect, and time horizon.
- Say that it is a qualitative policy simulation, not a forecast.
```

### 1.4 Add the file and turn memory off

1. On the **Build** tab, select **Knowledge**.
2. Drag **`GlobalFindexDatabase2025.xlsx`** into the upload area.
3. Name it exactly **World Bank Global Findex 2025**. If there's a description box, paste:

   ```text
   Official World Bank Global Findex Database 2025 country-level workbook, unmodified. One row per economy or World Bank aggregate, survey year and demographic group. Columns are indicator codes such as account.t.d (account ownership). Values are proportions from 0 to 1. The Series Table sheet defines each code. Use this source for every financial inclusion statistic.
   ```

4. Select **Add**. Don't add any other source.
5. Wait for the file to finish processing.
6. Make sure **Memory** is **off**.

**Done when:** the agent has the instructions, **one** ready knowledge source, and Memory off, and `Hi` in **Preview** gets a short greeting.

| Problem | What to do |
| --- | --- |
| You can't upload the file | Ask your administrator to allow file knowledge and turn on **Dataverse search** |
| The upload never finishes | Close the file in Excel, and try the original `.xlsx` again |
| You see a **Topics** page | Wrong harness. Use the new experience from the home page |
| It greets you with a long report | Add to **Answers**: `For a greeting, reply in one sentence.` |

---

## 2. Add the two skills

**Time:** 10 minutes. Create both from blank:

1. On your agent, select **Build**, then **Skills**.
2. Select **Add skill**, then **Create from blank**.
3. Copy the **Name**, **Description** and **Instructions** below into the three fields, and select **Create**.
4. Repeat for the second skill.

Copy the names exactly (lowercase, numbers and hyphens only).

### Skill 1: the investigator

**Name**

```text
global-financial-inclusion-investigator
```

**Description**

```text
Investigates financial inclusion gaps worldwide using the official World Bank Global Findex dataset. Activate when users request global, regional, country-level or cross-country financial inclusion investigations. Supports comparisons across geographic regions and demographic groups while respecting data availability, survey years and source limitations.
```

**Instructions**

```text
# Global Financial Inclusion Investigator

## Purpose
Investigate financial inclusion gaps across countries, regions and demographic groups worldwide. Use only the knowledge source "World Bank Global Findex 2025" for statistics.

## Step 1: Identify the geographic scope
Decide whether the request is worldwide, a region, an income group, an organization or informal area (such as ASEAN, Europe or Africa), one country, or several named countries. Use the file's own region, income-group and published aggregate rows. Never invent membership. If the grouping is not in the file, say which verifiable grouping you use instead.

## Step 2: Check data availability
For every economy: confirm it is in the file, list its survey years, confirm the indicator exists, and check the demographic breakdowns. Report anything missing.

## Step 3: Retrieve indicators
Use the exact World Bank definitions. Typical indicators: account ownership, mobile money account, digital payments, internet use, savings, borrowing, emergency funds.

## Step 4: Investigate demographic gaps
Where data exists, compare men and women, poorest 40% and richest 60%, rural and urban, ages 15-24 and 25+, and primary-or-less and secondary-or-more education. Use the calculate-percentage-point-gap tool for every gap. Only compare values with the same indicator and survey year. If the years differ, say so first.

## Step 5: Identify the largest observed gaps
Rank by percentage points. Do not claim statistical significance. Do not assume which group is disadvantaged.

## Step 6: Regional patterns
When comparing regions or many economies: list the economies included and how many the group has in the file; state the survey years; compare country-level findings; note recurring patterns and exceptions. For a regional figure, quote the World Bank's published row. Never compute your own average.

## Step 7: Report
1. Executive summary
2. Geographic coverage
3. Key findings
4. Demographic gaps
5. Supporting statistics
6. Data limitations
7. Areas needing further investigation

Every statistic shows economy, survey year, indicator, population group, value and "World Bank Global Findex 2025".

## Never
Invent statistics. Infer causation. Assume all economies share a survey year. Create your own regional or global aggregates. Convert percentages into people. Claim to have analyzed every economy in a group unless you retrieved every record.
```

### Skill 2: the evidence auditor

**Name**

```text
financial-inclusion-evidence-auditor
```

**Description**

```text
Audits financial inclusion findings against the World Bank Global Findex 2025 source before they are relied on. Activate when the user asks to validate, audit, verify or check findings, and before an action brief is created. Checks statistics, gaps, wording and geographic claims.
```

**Instructions**

```text
# Evidence Auditor

## Purpose
Check the findings from this conversation against the knowledge source "World Bank Global Findex 2025". You audit. You do not add new analysis.

## Step 1: List the claims
Number every statistic, gap, comparison and policy statement in the findings.

## Step 2: Verify each statistic
Look it up again in the source. Check economy, survey year, indicator, population group and value. Check that proportions were shown as percentages with one decimal.

## Step 3: Verify each gap
Recalculate it with the calculate-percentage-point-gap tool. A gap is the difference of the two displayed percentages. Check the sign and which group is higher.

## Step 4: Check the wording
Flag any claim that says "significant", states a cause, forecasts an outcome, invents a cost, reach, participant number or effectiveness, turns a percentage into a number of people, presents a possible explanation as observed data, or gives a figure with no year or source.

# Geographic Validation
For every regional or global finding:
1. Verify the geographic scope.
2. Confirm each economy belongs to the requested grouping using the file's region and income-group columns. Organizations such as ASEAN or the EU, and areas such as Europe or Africa, cannot be verified from the file.
3. Check that all included economies have comparable data.
4. List economies with a missing indicator.
5. List differences in survey years.
6. Reject regional or global averages that were not quoted from a published row in the file.
7. Reject claims that a limited selection of countries represents a whole region.
8. Flag conclusions generalized from one country to others without evidence.
9. Separate country-level observations from published regional or global statistics.
10. If the classification cannot be verified, mark the claim "Needs further validation".
Never accept "all countries in the region" unless every record was retrieved.

## Output
A table with the claim number, the claim, a verdict (Verified, Corrected, Unsupported or Needs further validation), and a note. Then list the corrections to make, and what the findings can safely say.
```

**Done when:** **Skills** lists both skills. In **Preview**, type `Validate these findings: Indonesia's account ownership in 2024 was 90%.` The agent should use the auditor and mark the claim as corrected, with **56.3%**.

---

## 3. Add the two workflows

**Time:** 40 minutes. A workflow is a small automation the agent calls as a tool. These need no connectors: one calculates a gap, one assembles a brief.

> [!IMPORTANT]
> **Not tested in a tenant.** Each workflow has tests. Fix and publish again until they pass. Short on time? Skip this layer. The demo still works, because the agent does each step itself.

Each workflow follows the same order: **create, publish, add to the agent, test**. A workflow can't be tested before it is published.

### 3.1 Workflow 1: calculate-percentage-point-gap

It does the subtraction, so the gap is the same every time.

**Create it**

1. Open your agent in [Copilot Studio](https://copilotstudio.microsoft.com).
2. Select **Build**, then **Tools**, then **Add a tool**, then **Add**, then **Workflow**.
3. Two cards appear: **When an agent calls the workflow** and **Respond to the agent**. Keep both.
4. Rename the workflow to `calculate-percentage-point-gap`.

**Add 4 inputs**

Select the **When an agent calls the workflow** card. Select **Add an input** four times. Each input has two boxes. Fill them like this:

| Type (pick first) | First box: name | Second box: description |
| --- | --- | --- |
| Text | `label_a` | Name of the first group |
| Number | `value_a` | First percentage, 0 to 100 |
| Text | `label_b` | Name of the second group |
| Number | `value_b` | Second percentage, 0 to 100 |

The **first** box is the name. The **second** box is only a hint. Don't put a name in the second box.

**Set the answer**

1. Select the **Respond to the agent** card.
2. Add an output. Pick the type **Text**.
3. In the first box, type `Response`.
4. Select the value box. Select **fx**.
5. Paste this, then select **Add**:

   ```text
   if(or(less(triggerBody()?['value_a'], 0), greater(triggerBody()?['value_a'], 100), less(triggerBody()?['value_b'], 0), greater(triggerBody()?['value_b'], 100)), 'INVALID_INPUT: values must be percentages from 0 to 100.', concat(triggerBody()?['label_a'], ' minus ', triggerBody()?['label_b'], ': ', formatNumber(sub(triggerBody()?['value_a'], triggerBody()?['value_b']), '+0.0;-0.0;0.0'), ' percentage points. Higher group: ', if(greater(triggerBody()?['value_a'], triggerBody()?['value_b']), triggerBody()?['label_a'], if(less(triggerBody()?['value_a'], triggerBody()?['value_b']), triggerBody()?['label_b'], 'equal')), '.'))
   ```

6. Turn **Asynchronous response** **Off**: select the **Respond to the agent** card, then **Settings**, then **Networking**. If you can't find it, skip this step.

**If step 5 shows an error,** or the tests return empty text: delete the expression. In the same editor, select **Create expression with Copilot**, and type this. Then publish again:

```text
If value_a or value_b is below 0 or above 100, return: INVALID_INPUT: values must be percentages from 0 to 100. Otherwise return: label_a minus label_b: the difference value_a minus value_b, rounded to one decimal with a plus or minus sign, percentage points. Higher group: the label with the higher value, or equal.
```

**Publish**

1. Fix any error in the **health center** banner. You can't publish with errors.
2. Select **Publish**.

**Add it to your agent**

1. Open your agent. Select **Build**, then **Tools**.
2. If `calculate-percentage-point-gap` is already listed, skip to step 5.
3. Select **Add a tool**. Open the **Workflows** tab. Select `calculate-percentage-point-gap`.
4. If it isn't in the list, see the problems table in 3.3.
5. Open the tool's **Details** tab.
6. Paste this into the description box, and select **Save**:

   ```text
   Calculates the gap between two percentages in percentage points, so the arithmetic is exact. Inputs: label_a, value_a, label_b, value_b. Pass the two displayed percentages (0 to 100) and their group names. Returns one line with the signed gap and the higher group. Use it for every gap you report.
   ```

**Test it** in **Preview**. Paste each message, and compare the answer.

| # | Paste this message | Expected answer |
| --- | --- | --- |
| 1 | `Use calculate-percentage-point-gap with label_a Men, value_a 90.9, label_b Women, value_b 82.3.` | `Men minus Women: +8.6 percentage points. Higher group: Men.` |
| 2 | `Use calculate-percentage-point-gap with label_a Women, value_a 82.3, label_b Men, value_b 90.9.` | `Women minus Men: -8.6 percentage points. Higher group: Men.` |
| 3 | `Use calculate-percentage-point-gap with label_a Urban, value_a 65.2, label_b Rural, value_b 34.0.` | `Urban minus Rural: +31.2 percentage points. Higher group: Urban.` |
| 4 | `Use calculate-percentage-point-gap with label_a Women, value_a 57.1, label_b Men, value_b 43.0.` | `Women minus Men: +14.1 percentage points. Higher group: Women.` |
| 5 | `Use calculate-percentage-point-gap with label_a Men, value_a 50.0, label_b Women, value_b 50.0.` | `Men minus Women: 0.0 percentage points. Higher group: equal.` |
| 6 | `Use calculate-percentage-point-gap with label_a Men, value_a 101, label_b Women, value_b 50.` | `INVALID_INPUT: values must be percentages from 0 to 100.` |
| 7 | `Use calculate-percentage-point-gap with label_a Men, value_a -1, label_b Women, value_b 5.` | `INVALID_INPUT: values must be percentages from 0 to 100.` |

Small wording changes are fine. A wrong number or sign is a fail. Row 4 matters most: it catches a missing rounding step. If a row fails, fix the workflow, **Publish** again, and resend.

> [!NOTE]
> Button names can differ a little in your tenant. Pick the closest match.

### 3.2 Workflow 2: create-financial-inclusion-brief

It puts the agent's verified findings into a fixed layout. It doesn't write anything itself.

**Build it**

1. Create a new workflow the same way as in 3.1 (**Build → Tools → Add a tool → Add → Workflow**). Rename it `create-financial-inclusion-brief`.
2. Select the **When an agent calls the workflow** card. Add ten **Text** inputs. Type each name in the **first** box. Leave the second box empty:

   | # | Name |
   | --- | --- |
   | 1 | `geographic_scope` |
   | 2 | `data_coverage` |
   | 3 | `executive_summary` |
   | 4 | `verified_findings` |
   | 5 | `gaps` |
   | 6 | `policy_interventions` |
   | 7 | `tradeoffs` |
   | 8 | `evidence_limitations` |
   | 9 | `next_steps` |
   | 10 | `information_needed` |

3. Select **Respond to the agent**. Add a **Text** output named `Response`.
4. Select the value box.
5. Type each line below. Press Enter at the end of each line.
6. Where you see `{name}`, don't type it. Pick that input from the list that opens. Keep the blank lines.

   ```text
   # Financial Inclusion Action Brief

   ## 1. Geographic Scope
   {geographic_scope}

   ## 2. Data Coverage
   {data_coverage}

   ## 3. Executive Summary
   {executive_summary}

   ## 4. Verified Financial Inclusion Findings
   {verified_findings}

   ## 5. Demographic and Geographic Gaps
   {gaps}

   ## 6. Possible Policy Interventions
   {policy_interventions}

   ## 7. Trade-offs and Implementation Considerations
   {tradeoffs}

   ## 8. Evidence Limitations
   {evidence_limitations}

   ## 9. Recommended Next Steps
   {next_steps}

   ## 10. Information Needed Before Calculating Financial Impact
   {information_needed}

   Source: World Bank Global Findex 2025.
   ```

7. Turn **Asynchronous response** **Off**, as in 3.1 step 6.
8. Select **Publish**.

If the line breaks are lost, select **Create expression with Copilot** in the value box and describe the layout.

**Add it to your agent**

1. Open your agent. Select **Build**, then **Tools**.
2. If `create-financial-inclusion-brief` is already listed, skip to step 4.
3. Select **Add a tool**. Open the **Workflows** tab. Select `create-financial-inclusion-brief`.
4. Open the tool's **Details** tab.
5. Paste this into the description box, and select **Save**:

   ```text
   Assembles a Financial Inclusion Action Brief in a fixed layout from verified findings. Inputs: geographic_scope, data_coverage, executive_summary, verified_findings, gaps, policy_interventions, tradeoffs, evidence_limitations, next_steps, information_needed. Returns the finished brief as text. Use it when the user asks for an action brief, report or briefing, after the findings have been audited.
   ```

**Test it** in **Preview**. Paste each message, and check the answer.

| # | Paste this message | A pass looks like |
| --- | --- | --- |
| 1 | `Use create-financial-inclusion-brief. Set its ten inputs to TEST-1, TEST-2, TEST-3, TEST-4, TEST-5, TEST-6, TEST-7, TEST-8, TEST-9 and TEST-10, in the order of the input list. Show me the full output exactly.` | All ten headings in order, with `TEST-1` to `TEST-10` under the matching heading. Ends with `Source: World Bank Global Findex 2025.` |
| 2 | `Use create-financial-inclusion-brief. Put Brazil & India: "men" 90.9% > "women" 82.3% in verified_findings, and short text in the other nine. Show me the full output exactly.` | That text appears unchanged under heading 4 |

If a row fails, fix the workflow, **Publish** again, and resend.

### 3.3 Final check and problems

**Done when:** in **Preview**, `What is the gap between men and women in Brazil in 2024?` makes the activity trace show **calculate-percentage-point-gap**, and the answer says Men minus Women: **+8.6** percentage points, men higher.

| Problem | What to do |
| --- | --- |
| The workflow isn't in the **Workflows** list | It isn't published, it doesn't use the agent trigger, it has no **Respond to the agent** action, or **Asynchronous response** is on |
| The designer added extra steps, or an AI step | Delete them. These workflows must be deterministic. Rerun the tests |
| A test fails on a number or sign | Fix the expression (see 3.1), publish again, and rerun all the tests |
| The agent doesn't call a tool | Check the tool's **Details** text, and that the instructions in 1.3 name the tool exactly. The agent may also skip a tool for a trivial question |
| A workflow run times out or fails | Check the **health center** banner and the run history. These workflows should finish in seconds |

---

## 4. Run the pre-demo check

**Time:** 20 minutes. The file is wide and coded, so an agent can quietly get numbers wrong. **If a required check fails, don't demo numbers.**

Open **Preview** with **End user preview off**, so you can see the activity trace. Use a **new conversation** for each question.

**Required:** Q1 to Q6, and T5. Then run the geographic tests (T) for the region you plan to show.

An answer **passes** only if:

- **The number is right**, within 0.1 points, as a **percentage** (`56.3%`, not `0.563`).
- **The year, group and direction are right.**
- **It says "not in the file"** when there is no value, instead of giving a number.
- **It states the geographic definition and coverage,** and never claims to have analyzed every economy unless it retrieved every record.
- **The trace shows the knowledge source was consulted.** A correct number with no lookup is a **fail**.

### 4.1 Data questions (required)

**Q1**

```text
What was account ownership among all adults in Indonesia in 2024?
```

Right answer: **56.3%**.

**Q2**

```text
What was account ownership for the poorest 40% and the richest 60% of households in Lao PDR in 2024?
```

Right answer: **18.3%** and **50.6%**.

**Q3**

```text
Compare account ownership of men and women in the Philippines in 2024. Which group is lower?
```

Right answer: women **57.1%**, men **43.0%**. **Men** are lower.

**Q4**

```text
What is the latest account ownership figure for Myanmar, and which year is it from?
```

Right answer: **47.8%**, from **2021**.

**Q5**

```text
What share of adults made or received a digital payment in Singapore in 2024?
```

Right answer: **no 2024 value.** It may offer **94.8%** only if it says **2021**.

**Q6**

```text
What was account ownership in Brunei Darussalam and Timor-Leste in 2024?
```

Right answer: **neither is in the file.** No numbers.

### 4.2 Geographic tests

**T1: worldwide**

```text
Investigate financial inclusion worldwide.
```

Right: it quotes the World Bank's published **world** row, **78.7%** account ownership in **2024**, and says it is a published aggregate. If it cites income groups, they are low **46.4%**, lower middle **70.4%**, upper middle **84.0%** and high **94.9%**. It says the world row has no 2024 digital-payments value, doesn't build its own averages, and doesn't claim to have analyzed every economy.

**T2: Southeast Asia**

```text
Investigate account ownership in Southeast Asia.
```

Right: it uses the nine economies in the file. The lowest is **Lao PDR 37.7%** and the highest is **Singapore 98.0%**, all 2024 except **Myanmar 47.8% (2021)**. It says Brunei Darussalam and Timor-Leste aren't in the file. It calculates no regional average. If it quotes the East Asia & Pacific row (**83.3%**), it must label it as that region excluding high income, not as Southeast Asia.

**T3: Sub-Saharan Africa**

```text
Compare account ownership across Sub-Saharan Africa.
```

Right: it uses the file's region **Sub-Saharan Africa (excluding high income)**, **42 economies**. It may quote the published row, **58.2%** in 2024. **35** economies have 2024 data and **7** are older (four from 2014, two from 2017, one from 2021), and it says the years differ. If it names extremes, the lowest is **South Sudan 5.8% (2021)** and the highest is **Kenya 90.1% (2024)**.

**T4: Europe**

```text
Investigate financial inclusion in Europe.
```

Right: it says the file has no "Europe" grouping, and either asks which countries or uses **Europe & Central Asia (excluding high income)**, **20 economies**, noting that this leaves out high-income European economies such as Germany and France. It may quote the published row, **77.8%** in 2024. It doesn't present that as all of Europe.

**T5: cross-region (required)**

```text
Compare India, Brazil, and Indonesia.
```

Right: all three are **2024**. Account ownership: India **89.0%**, Brazil **86.4%**, Indonesia **56.3%**. It compares like with like, and states that the years match.

**T6: missing economy**

```text
Investigate financial inclusion in Brunei Darussalam.
```

Right: it says Brunei Darussalam isn't in the file, and gives no numbers. It may offer economies that are in the file.

**T7: regional audit.** Run it in the same conversation, straight after T3.

```text
Validate the regional findings.
```

Right: the trace shows the **financial-inclusion-evidence-auditor** skill. It checks membership (the file's region column), coverage (42 economies, how many it retrieved), survey years (35 from 2024, 7 older), and unsupported generalizations. It marks anything it can't verify as needing further validation.

**T8: global briefing**

```text
Create a worldwide financial inclusion action brief.
```

Right: it returns a brief with the **ten numbered headings** and ends with `Source: World Bank Global Findex 2025.` The geographic scope and data coverage sections state the limits. If the workflows are connected, the trace shows **create-financial-inclusion-brief**.

**T9: ASEAN**

```text
Compare ASEAN countries.
```

Right: it says the file has no ASEAN membership list. It offers the nine Southeast Asia economies as a geographic substitute, clearly labelled, or asks you to name the countries. It doesn't claim to have compared "ASEAN".

### 4.3 Results and fixes

| Result | What to do |
| --- | --- |
| **All required checks pass** | Go to the demo. Re-run Q1 to Q6 and T5 about 30 minutes before it, because results can vary between runs |
| **1 or 2 fail with the same cause** | Add one sentence from the table below, and rerun every check you ran |
| **Several fail, or "I can't find it"** | **Stop.** The file isn't being read reliably. See "If it keeps failing" |

**Quick fixes** (add one sentence to the instructions in 1.3, then rerun):

| Problem | Add to the instructions |
| --- | --- |
| Shows `0.563` | `Multiply every value by 100 and write it as a percentage with one decimal place and a % sign.` |
| Wrong year | `State the survey year in every figure. Never use a year the file doesn't have for that economy.` |
| Gives a number for a missing value or economy | `If the file has no value, say "not in the file" or "not available". Never estimate.` |
| No knowledge lookup in the trace | `Always look up every figure in the knowledge source before you answer.` |
| Builds its own regional average | `Never calculate a regional or global average. Quote the World Bank's published row, or say none is available.` |
| Treats ASEAN or Europe as a grouping in the file | `ASEAN, the EU and "Europe" are not in the file. Say so, and state the grouping you use instead.` |
| Says it analyzed every economy | `Say how many economies you retrieved. Never claim to have analyzed all of them.` |
| Doesn't use a skill or tool | Check the skill description or the tool's **Details**, and the names in the **Skills and tools** section |

**If it keeps failing,** try these in order:

1. **Ask narrower questions.** One economy, one indicator, one group. Only demo what passes. Worldwide and regional requests break first.
2. **Use the official CSV instead of the workbook.** Replace the `.xlsx` source with the `.csv`, named the same. Codes use underscores (`account_t_d`), missing values say `NA`, and there's no Series Table, so update the code examples in the instructions.
3. **Demo only the qualitative parts.** Policy options and trade-offs don't need exact numbers, but you lose the "discover hidden gaps" moment.

**Don't** attach the file to the chat (the 16 MiB limit is smaller than the workbook), and **don't type numbers into the instructions**.

### How to double-check a number in Excel

1. Open the downloaded `.xlsx`, and go to the **Data** sheet. **Don't save it.**
2. Select the header row, and turn on **Data → Filter**.
3. Filter `countrynewwb` (for example Indonesia, or `world`), `year` (for example 2024), `group` and `group2` (for example `all` and `all`).
4. Read the indicator column, for example `account.t.d`. `0.563` means **56.3%**.

`group` and `group2` values: `gender` (`men`, `women`), `income` (`poorest 40%`, `richest 60%`), `urbanicity` (`rural`, `urban`), `age_cat` (`ages 15-24`, `age 25+`), `laborforce` (`in laborforce`, `out of laborforce`), `education` (`prim edu or less`, `secondary edu or more`). The **Series Table** sheet explains each code.

---

## 5. Share the agent (optional)

**Time:** about 20 minutes. Optional: only if another trainer needs the same agent.

> [!IMPORTANT]
> **Not confirmed for this kind of agent.** I found no documentation on whether its skills and workflows travel in a solution. Step 1 is a quick check. If it fails, stop and ask your administrator.

Know this first: **instructions are included**, but **knowledge files might not be** (add the file again). The icon and channel details don't transfer. After the import, **set up authentication again** and **publish**.

1. **Check it can go into a solution.** Open **Solutions** (the **…** on the side bar), then **New solution**. Name it `FinancialInclusionImpactAgent`, and pick a publisher. Open it, and select **Add existing → Agent → Agent**. If the agent isn't listed, **stop here**.
2. **Add the workflows.** **Add existing** both workflows. Then, in **Objects**, select the agent's **⋮**, then **Advanced → Add required objects**.
3. **Export.** Select the solution, then **Export solution**, **Publish all changes**, **Next**. Choose **Unmanaged** for a test copy, or **Managed** for distribution. Download the `.zip`.
4. **Import** into a different environment: **Solutions → Import solution**. If it fails, select **Download log file**.
5. **Make it work.** Set up authentication, and **publish**. Check section 1: instructions present, Memory off, and **Knowledge** has **World Bank Global Findex 2025**. Check **Skills** and **Tools**. Add anything missing from this guide, with the same names.
6. **Re-run the pre-demo check.** A re-added file is indexed again, so results can differ.

> [!WARNING]
> **A managed solution can lock the agent.** If something doesn't come across and the agent can't be edited, nobody can add it back. **Export an unmanaged copy first.** If you must distribute, give an unmanaged solution.

**Give the other trainer:** the solution `.zip` (say if it's managed), a link to the [World Bank download page](https://www.worldbank.org/en/publication/globalfindex/download-data) (**never bundle the data file**), and this note:

```text
1. Import the solution (Solutions > Import solution), set up authentication, and publish.
2. Download the official Excel file from the World Bank page. Don't open and save it.
3. If the agent has no knowledge source, add the file and name it "World Bank Global Findex 2025".
4. Check that both skills and both workflows are present. If not, add them from SETUP.md.
5. Run Q1 to Q6 and T5 from the pre-demo check. Don't demo until they all pass.
```

**Clean up:** delete only what you created (test agents, workflows, solutions). Deleting doesn't reverse credits already used.

[← Back to the demo kit](./README.md)
