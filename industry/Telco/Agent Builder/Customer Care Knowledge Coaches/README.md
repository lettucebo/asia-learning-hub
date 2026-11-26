# Fix First, Then Retain: Customer Care Knowledge Coaches

AsterWave Mobile, a fictional mobile operator, is dealing with slow mobile data in its Meranti Coast region. Customer CUS-01042 contacts care for the second time this month (case CARE-2048) and mentions a competitor.

Handling this well means applying many rules at once:
- Plans, roaming and eSIM rules
- Billing adjustments and authority limits
- Current network incidents and approved outage wording
- Service credits and retention offer eligibility
- Rules for vulnerable customers and escalation

This demo shows three agents built with **Agent Builder** in Microsoft 365 Copilot. They all read the same five knowledge files from OneDrive or SharePoint, but each one has different instructions.

| **Agent** | **Who uses it** | **What it does** |
|-----------|-----------------|------------------|
| [AsterWave Care Coach](Care-Coach.md) | Frontline customer care representatives | Fixes the customer's immediate problem with a short, cited answer card |
| [AsterWave Retention Coach](Retention-Coach.md) | Retention specialists and team leads | Fixes the problem first, checks every retention offer against the rules, and drafts a hand-off note |
| [AsterWave Onboarding Coach](Onboarding-Coach.md) | New customer care representatives and trainers | Teaches the same rules through lessons, quizzes and role-plays |

> **You don't need all three agents.** Each agent works on its own. Depending on the time you have, build and show one agent, two, or all three. See [Choose your demo](#choose-your-demo).

> **Note:** In this README, *agent* means an AI agent built in Agent Builder. The people who use the agents are called customer care representatives. All organisations, people, plans, prices, offers and policies in this demo are fictional.

## Pain points and demonstrated benefits
| **Pain point** | **How the agents help** | **Business benefits** |
|----------------|-------------------------|-----------------------|
| Customer care representatives search many documents during live calls and give inconsistent answers | The Care Coach answers from the approved files with steps, customer-ready wording and clause-level citations | Faster, consistent answers that anyone can check |
| Outage calls lead to guesses about causes and restore times | The Care Coach reads the network status snapshot and uses the approved customer message | Accurate outage communication and clear expectations |
| Credits and adjustments go beyond authority limits | Every answer states whether approval is needed and who approves | Fewer policy breaches and less rework |
| Retention offers are chosen inconsistently, or invented | The Retention Coach fixes the problem first, checks every offer against the eligibility rules, and recommends the lowest-cost eligible option | Compliant, cost-aware retention decisions |
| Vulnerable customers can be offered unsuitable contracts | The Retention Coach applies the vulnerable-customer rules before any offer | Fair treatment and lower conduct risk |
| New customer care representatives take a long time to learn the rules | The Onboarding Coach teaches, quizzes and role-plays, with rubric-based feedback | Faster, safer ramp-up on fictional cases |

## Demo files
[Telco_Customer_Care_Coaches_Demo_Files.zip](https://github.com/CSDSkilling/asia-learning-hub/raw/refs/heads/main/industry/Telco/Agent%20builder/Customer%20Care%20Knowledge%20Coaches/data-files/Telco_Customer_Care_Coaches_Demo_Files.zip)

| **File** | **Contents** | **Used by** |
|----------|--------------|-------------|
| `AW1_Plans_Roaming_eSIM_Guide.docx` | Plans and contracts, roaming zones and passes, eSIM moves and identity checks | All three agents |
| `AW2_Customer_Care_Policy_Handbook.docx` | Billing and authority limits, payments, outage communication, service credits, retention rules, vulnerable customers and escalation | All three agents |
| `AW3_Retention_Offer_Table.xlsx` | 10 retention offers with eligibility rules, cost bands and approval levels | Retention, Onboarding |
| `AW4_Network_Status_Snapshot.docx` | Current and recent incidents with an "As of" time and approved customer messages | All three agents |
| `AW5_Care_Academy_Training_Pack.docx` | Training modules, competency rubric, glossary and practice scenarios | Onboarding |
| `AsterWave Agent Builder Demo Kit - MTT Guide v1.0.docx` | Full trainer guide: build steps, all tests with pass criteria, a lab plan, troubleshooting, and how to build your own kit | Trainers |

## Choose your demo
The stages follow one customer story, but each stage also works on its own. Pick the option that fits your session, build only the agents it needs, and show only those stages. Stage 1 sets the scene in every option.

| **Option** | **Agents to build** | **Knowledge files** | **Stages to show** | **Demo time (about)** |
|------------|---------------------|---------------------|--------------------|-----------------------|
| Care Coach only | Care Coach | AW1, AW2, AW4 | 1, 2 | 6 minutes |
| Retention Coach only | Retention Coach | AW1, AW2, AW3, AW4 | 1, 3, 4 | 8 minutes |
| Onboarding Coach only | Onboarding Coach | All five files | 1, 5 | 5 minutes |
| Fix first, then retain | Care Coach and Retention Coach | AW1, AW2, AW3, AW4 | 1–4 | 12 minutes |
| Full story | All three agents | All five files | 1–5 | 15 minutes |

Demo times include a 1-minute wrap-up. Build the agents before the session; building all three takes about 45 minutes.

## Set up the demo
1. Download the ZIP file and extract it.
2. Create a folder named `AsterWave Demo Kit` in your OneDrive and upload the AW files to it (all five, or only the ones listed for your option). For a demo that several presenters run, use a SharePoint document library instead. Keep the file names unchanged, because the agent instructions refer to the files by name.
3. Build the agents for the option you chose, using their pages: [Care Coach](Care-Coach.md), [Retention Coach](Retention-Coach.md) and [Onboarding Coach](Onboarding-Coach.md). In the **Knowledge** section, add each agent's files from your folder with **Add knowledge**.
4. Wait until no file shows **Preparing**, then test each agent on the **Preview** tab.

> **Requirements:** agents that use SharePoint or OneDrive knowledge need a Microsoft 365 Copilot license or usage-based billing. People you share the agents with also need access to the `AsterWave Demo Kit` folder.

## Demo journey
| **Stage** | **Agent** | **Time** | **Story** |
|-----------|-----------|----------|-----------|
| 1. Set the scene | — | 1 min | Customer CUS-01042 in Meranti Coast contacts care a second time about slow data and mentions a competitor. |
| 2. Fix the immediate problem | Care Coach | 4 min | Check the current incident, offer the right service credit and tell the customer what to expect. |
| 3. Decide on retention | Retention Coach | 5 min | Fix the problem first, check every offer against the rules, and recommend the lowest-cost eligible option. |
| 4. Hand off for action | — | 1 min | These agents are read-only by design; recording the action in a system of record is a Copilot Studio scenario. |
| 5. Train new customer care representatives | Onboarding Coach | 3 min | Practise the same case in a role-play and get rubric-based feedback. |

The full story takes about 15 minutes, including a 1-minute wrap-up. To show fewer stages, see [Choose your demo](#choose-your-demo).

## Stage 1 - Set the scene
Show the knowledge files in your `AsterWave Demo Kit` folder and introduce customer CUS-01042 and case CARE-2048. Explain that all data is fictional and that the network status snapshot (AW4) stands in for a live system: its "As of" time, Friday 30 October 2026, 10:00, is "now" in the story.

## Stage 2 - Fix the immediate problem with the Care Coach
- **Current incident:** Select the **Current incidents** suggested prompt.

> Is there a current incident affecting mobile data in Meranti Coast? What should I tell the customer?

- **Service credit:** Select the **Outage credit** suggested prompt.

> What can I offer a Meranti Coast customer affected by INC-077?

Point out the incident status and Last updated time, the SRV-2.1 credit, the approval line, the customer wording and the clause-level sources.

- **Trap question:** Enter this prompt.

> Can you give this customer 50% off for six months?

The agent doesn't invent an offer. It refers the request to the Retention Coach.

## Stage 3 - Decide on retention with the Retention Coach
- **Check eligibility:** Select the **Check eligibility** suggested prompt.

> CARE-2048: AW-POST-45, 26 months, out of contract, two contacts about slow data in Meranti Coast in the last 10 days (INC-071 and INC-077). Main reason network quality; mentions a competitor; no retention offer in the last 12 months. Which options are eligible?

Point out "fix first", the eligibility table, the offers that fail and why, OFFER-12 as the recommendation, and the hand-off note.

- **Vulnerable customer:** Select the **Vulnerable customer** suggested prompt.

> The CARE-2048 customer has just mentioned financial hardship. How does that change the options?

Offers that need a new contract drop out under VUL-4.2, and the agent adds a payment extension and a referral for a hardship review.

If you skipped Stage 2, the Retention Coach still fixes the problem first: before any offer, it checks INC-077 and the service credit.

## Stage 4 - Hand off for action
Explain that the agents in this demo are read-only: they explain rules and approvals but never change records. Logging OFFER-12 in a system of record after the specialist confirms it needs actions and workflows, which is a Copilot Studio scenario. An Agent Builder agent can be copied to Copilot Studio when it needs those capabilities.

## Stage 5 - Train new customer care representatives with the Onboarding Coach
- **Role-play:** Select the **Outage role-play** suggested prompt.

> Role-play a customer whose data has been slow in Meranti Coast since this morning.

Reply twice as the customer care representative, then enter `end role-play`. Point out the rubric scores and clause citations. This agent uses the same policy files as the other two; only the instructions differ.

## Optional - Show a live status update
If you show the Care Coach, you can also show changing data, because the agents read the files from OneDrive or SharePoint. After Stage 2, open `AW4_Network_Status_Snapshot.docx`, change the INC-077 row to **Restored** (and the Meranti Coast line in the region summary), and save it. At the end of the demo, ask the Care Coach about Meranti Coast again. A change can take several minutes to appear, so test it before the session and restore the original file afterwards.

## Final demo outcome
By the end of the full story, the audience has seen:
- Cited answer cards that state approval limits (Care Coach)
- A rules-based retention decision with a hand-off note (Retention Coach)
- Coaching with rubric-based feedback (Onboarding Coach)
- One set of knowledge files in OneDrive or SharePoint serving three agents, each shaped by its own instructions

If you show fewer stages, the audience sees the outcomes of the agents you show.

## More resources
- The full trainer guide is in the ZIP: build steps, all test prompts with pass criteria, a 60–90 minute lab plan, troubleshooting, and how to build your own kit for another customer or industry.
- Companion Copilot demo with the same AsterWave story: [From Customer Complaints to a Retention Decision](../../Copilot/Customer%20Retention%20Decision)
- Microsoft Learn: [Build agents in Agent Builder](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents) · [Add knowledge sources to an agent in Agent Builder](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge) · [Share and manage agents built in Agent Builder](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-share-manage-agents)
