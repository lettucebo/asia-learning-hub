# From Alarm Storm to Verified Fix: NOC Incident Coach (Copilot Studio)

AsterWave Mobile, a fictional mobile operator, is dealing with slow mobile data in its Meranti Coast region. It's 10:00 on Friday 30 October 2026. Since 07:38, the Network Operations Centre (NOC) has received 15 alarms, incident INC-077 is open, and the field repair won't finish until about 12:00. The shift wants a faster fix, someone has to approve it, and customer care is waiting for the next status bulletin.

This demo shows one agent built in **Microsoft Copilot Studio** on the Microsoft Copilot harness and delivered as one solution. The NOC event log and the status bulletin are Dataverse tables. The agent reads the events through a workflow, checks the bulletin as Dataverse knowledge and follows the runbook as a skill. When the engineer confirms, it also acts: it emails the approval request and publishes the bulletin update.

| **Agent** | **Who uses it** | **What it does** |
|-----------|-----------------|------------------|
| AsterWave NOC Incident Coach | NOC engineers and NOC shift managers | Reads the incident's events from Dataverse, turns many alarms into one incident and guides the shift through diagnosis, an approved action and a verified fix, with cited sources. After the user confirms, it sends the approval request and publishes the status bulletin update. |

| **Step** | **What the NOC asks** | **What the agent gives back** |
|----------|-----------------------|-------------------------------|
| 1. Group the alarms | Which alarms belong together? | One incident, the probable root alarm, the alarms to keep separate, the severity and the next update time |
| 2. Diagnose | What's confirmed, and what's still a guess? | A runbook check that labels each finding "Confirmed" or "Hypothesis" |
| 3. Choose an action | What can we do now, and who approves it? | Every action checked against its rules, a recommendation, and an approval request that it emails after you confirm |
| 4. Verify and update | Is service really back? | A restoration check, a verdict, and a bulletin update that it publishes after you confirm |

> **Agent Builder version:** The same story is also available as an Agent Builder demo, with knowledge files in OneDrive and an event export attached in the chat: [NOC Incident Coach (Agent Builder)](../../Agent%20Builder/NOC%20Incident%20Coach). This version keeps the data in Dataverse and adds two actions that send email and update data.

> **Rebuild it step by step:** This README covers importing the finished solution and running the demo. To reproduce exactly how the solution was built, follow the Word guide [StepByStepGuideForMTT.docx](lab-guide/StepByStepGuideForMTT.docx) in the `lab-guide` folder.

> **Note:** All organisations, people, network elements, numbers and policies in this demo are fictional.

## Pain points and demonstrated benefits
| **Pain point** | **How the agent helps** | **Business benefits** |
|----------------|-------------------------|-----------------------|
| During an alarm storm, engineers link dozens of alarms by hand | Reads every event in the incident window from the event log, groups the alarms by their shared upstream node, names the probable root alarm and lists the alarms to keep separate, with EventIDs | Faster triage and one clear incident to work on |
| Runbooks are long, and the evidence is spread across tools | Walks through the runbook step by step against the logged events and labels each finding "Confirmed" or "Hypothesis" | A consistent diagnosis that anyone can check |
| It's unclear which action is allowed, who must approve it, and whether a planned change must wait | Checks every action in the catalogue, calculates preconditions such as link load, recommends the lowest-risk option and applies the change freeze | Faster, compliant decisions and fewer change-related outages |
| Approval requests and bulletin updates are retyped into email and the status page | Drafts both. After the engineer confirms, it emails the approval request and logs it as pending, updates the bulletin row and notifies Care Operations | Less manual work, a record of every request, and customer care sees the update straight away |
| Incidents are declared restored too early | Gives a verdict only after it checks each restoration criterion, and says "Not yet" when evidence is missing | Fewer reopened incidents and an accurate status |
| Status messages reveal causes or promise times | Writes customer wording that follows the bulletin rules: no cause or equipment names, and the restore time only as an estimate | Consistent customer communication and lower reputational risk |

## Files in this folder
| **File** | **Contents** | **Used for** |
|----------|--------------|--------------|
| [solution/AsterWaveNOCSolution_1_0_0_3.zip](solution/AsterWaveNOCSolution_1_0_0_3.zip) | Unmanaged solution **AsterWave NOC Solution**, version 1.0.0.3: the agent with its skill, knowledge and tools, 3 tables, 3 workflows, 2 Power Automate flows for the simulation, 1 AI Builder prompt, 2 environment variables and the evaluation test set | Importing the demo into your environment |
| [data-files/NOC_Event_Import.xlsx](data-files/NOC_Event_Import.xlsx) | 28 NOC events, EV-101 to EV-128: 15 alarms, KPI checks, diagnostics, a field update, changes, a review action and a log note | Importing into the NOC Event table |
| [data-files/Network_Status_Import.xlsx](data-files/Network_Status_Import.xlsx) | 5 status bulletin rows: INC-077, INC-080, INC-081, INC-071 and the planned maintenance MNT-090 | Importing into the Network Status table |
| [evaluation/NOC_Incident_Coach_evaluation.csv](evaluation/NOC_Incident_Coach_evaluation.csv) | 16 test conversations with expected answers | Evaluating the agent (optional) |
| [lab-guide/StepByStepGuideForMTT.docx](lab-guide/StepByStepGuideForMTT.docx) | Step-by-step guide (Word) that rebuilds this solution in 12 exercises, from creating the environment to exporting and importing the solution, with every test prompt and its expected result | Reproducing exactly how the solution was built |
| [lab-guide/noc-incident-runbook.zip](lab-guide/noc-incident-runbook.zip) | The runbook skill: SKILL.md and the AW6 runbook in Markdown | Uploading the skill when you follow the step-by-step guide. The solution already includes it. |

## Configuration
Everything in this section comes with the solution, so you don't need to build anything.

### Agent
| **Setting** | **Value** |
|-------------|-----------|
| Name | AsterWave NOC Incident Coach |
| Harness and model | Microsoft Copilot harness, model **Auto** |
| Language | English |
| Authentication | Authenticate with Microsoft, which Dataverse knowledge needs |
| Instructions | The agent's role and data sources; a fixed scenario time (30 October 2026, 10:00, AsterWave local time); a citation for every fact; the four steps; rules for the write tools; restrictions (no network actions, no approvals and no customer personal data); and the response style. They also cover how to query events from the optional simulation. |

### Knowledge, skill and tools
| **Component** | **Type** | **Purpose** |
|---------------|----------|-------------|
| Network Status | Knowledge (Dataverse table) | The status bulletins that customer care reads: status, last update, estimated or actual restore time, duration, credit eligibility and the customer message for each incident or planned maintenance. The agent also uses it to find earlier incidents from the last 30 days. |
| noc-incident-runbook | Skill | The AW6 runbook (network reference, alarm grouping, severity and update cadence, credit eligibility, runbooks, the action catalogue with risks and approvers, change freeze, restoration criteria, bulletin wording and escalation), with the procedure and answer format for each step |
| Get Incidents Events | Tool (workflow), read-only | Returns every NOC Event row between a start time and an end time, in time order. The agent calls it first whenever it needs alarms, KPI checks, diagnostics, field updates, changes or review actions. |
| Request Action Approval | Tool (workflow), sends email and adds data | Emails the approval request for a Medium- or High-risk action to the approver mailbox with High importance, and logs it in NOC Event as an "Approval request" event with "Approval: Pending". It doesn't approve or run the action. |
| Update Status Bulletin | Tool (workflow), sends email and changes data | Updates an incident's row in Network Status (Status, LastUpdated, EstimatedOrRestoredAt, Duration, CreditEligible and CustomerMessage) and emails the update to the Care Operations mailbox |
| Work IQ MCP Server | Tool (MCP) | Access to Microsoft 365 mail, calendar, files, people, sites and Teams. The harness adds it to new agents by default; the demo doesn't rely on it. |

> **Human in control:** Before it calls either write tool, the agent shows the complete approval request or bulletin update. It calls the tool only after the user confirms in a later message.

### Tables and environment variables
| **Component** | **Purpose** |
|---------------|-------------|
| NOC Event (table) | The event log, one row per EventID. Get Incidents Events reads it, and Request Action Approval adds approval request rows. |
| Network Status (table) | The status bulletin, one row per incident or planned maintenance. The agent reads it as knowledge, and Update Status Bulletin updates it. |
| NOC Simulation Config (table) | Settings for the optional event simulation |
| AsterWave Approver Email (environment variable) | The mailbox that receives approval requests. For a demo, use the presenter's mailbox. |
| AsterWave Care Ops Email (environment variable) | The mailbox of the Care Operations Lead, who receives bulletin updates. For a demo, use the presenter's mailbox. |

### Optional event simulation
The two simulation flows are Power Automate cloud flows, separate from Copilot Studio. You find and run them in Power Automate, not under **Workflows** in Copilot Studio.

| **Component** | **Purpose** |
|---------------|-------------|
| InitializeNOCSimulation (cloud flow, run manually) | Issues the number of new IncidentIDs that you enter, saves them in NOC Simulation Config and turns event generation on |
| GenerateNOCEvents (cloud flow, runs every minute) | While event generation is on, creates one new event for the next of those IncidentIDs on each run and saves it in NOC Event. It's off after the import. |
| GenerateNOCEventData (AI Builder prompt) | Writes one realistic, synthetic NOC event as JSON, based on reference events |

The solution also includes the evaluation test set **NOC Incident Coach Regression Test v1**. See [Evaluate the agent](#evaluate-the-agent-optional).

## Set up the demo

> [!IMPORTANT]
> **Using a Skillable lab account? Import the solution into a separate environment, not Contoso (default).**
> - With a lab account provided by Skillable, importing the solution into the **Contoso (default)** environment fails because of a permission issue. Importing a solution needs the System Administrator or System Customizer security role, and Skillable lab accounts can't get this role in that environment.
> - Create a separate environment in the same tenant (step 1), and import the solution into it.
> - In a trainer demo tenant, the import into Contoso (default) works, so a separate environment is optional there.
> - In a new environment, Copilot Studio might not show the option to add Dataverse as a knowledge source. You don't need it: the agent's **Network Status** knowledge source comes with the solution, and after the import it appears under **Knowledge** as a Dataverse knowledge source.

> **Requirements:** A demo tenant where you can create a Power Platform environment and build agents in Copilot Studio. Agents powered by the Microsoft Copilot harness use Copilot Credits, including when you build, test and evaluate them. The two write tools send real email from the account that you use for the Office 365 Outlook connection.

1. **Create an environment (required with a Skillable lab account).** In the Power Platform admin center, create an environment with **Add a Dataverse data store?** set to **Yes**, for example a Developer environment named `TelcoEnv`. Wait until its state is **Ready**. New unmanaged Developer environments can't be created from 15 November 2026; if you can't create one, use a Sandbox or Trial environment. Learn more in [Create and manage environments](https://learn.microsoft.com/en-us/power-platform/admin/create-environment). In a trainer demo tenant, you can skip this step and use Contoso (default).
   - **Turn on Dataverse search.** In the admin center, open the environment's **Settings > Product > Features**, select both **Dataverse search** options and save. In environments other than production, an admin must turn it on, and the Network Status knowledge source depends on it.
3. **Import the solution.** In Copilot Studio or Power Apps, open **Solutions** in the environment that you use for the demo, select **Import solution** and choose `solution/AsterWaveNOCSolution_1_0_0_3.zip`.
   - Keep **Enable Plugin steps and flows included in the solution** selected.
   - Create or select a connection for each connector that's listed: **Microsoft Dataverse**, **Office 365 Outlook** and **Work IQ MCP**.
   - Enter the mailboxes for **AsterWave Approver Email** and **AsterWave Care Ops Email**. Your own mailbox works for both. If the names show *[no English (United States) display name - showing Korean (Korea)]*, you can ignore this.
   - When the import finishes, you might see a warning that starts with *Solution "AsterWave NOC Solution" imported, but one or more flows may not have turned on* and mentions translated labels for language 1042 (Korean). This warning is safe to ignore: it doesn't affect how the solution works, and step 5 checks that the workflows are enabled.
   - Then select **Publish all customizations** in the top menu of the **Solutions** page (the same menu as **Import solution**).
4. **Load the sample data.** In Power Apps, open each table and select **Import > Import data from Excel**. If a column isn't matched automatically, map it to the column with the same name.
   - `data-files/NOC_Event_Import.xlsx` into **NOC Event** (28 rows). The **Description** and **Time** columns show **Possible match**: select **Accept match** for both.
   - `data-files/Network_Status_Import.xlsx` into **Network Status** (5 rows)
   - Then add one row to **NOC Simulation Config**: ConfigName `Default`, IncidentIdsJson `[]`, NextIncidentIndex `0`, IsEnabled `No`, LastIssuedIncidentNumber `80`.
5. **Check the workflows.** In Copilot Studio, go to **Workflows** and check that Get Incidents Events, Request Action Approval and Update Status Bulletin are enabled. The two simulation flows, InitializeNOCSimulation and GenerateNOCEvents, aren't listed there: they're Power Automate cloud flows, separate from Copilot Studio. In Power Automate, leave GenerateNOCEvents off unless you run the simulation.
6. **Test the agent.** Open **AsterWave NOC Incident Coach**, select **Preview > New chat** and ask `What's the current bulletin status of INC-080?` The answer should show Status **Investigating** and CreditEligible **Pending**, citing Network Status.
7. **Publish to Microsoft Copilot and Teams (optional).** The demo runs in the agent's **Preview** tab, so you don't need a channel. To also use the agent in Microsoft Copilot and Teams, select **Publish**, choose the **Microsoft Copilot** and **Microsoft Teams** channels in the **Publish agent** dialog and confirm with **Publish**. Learn more in [Publish an agent (Microsoft Copilot)](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/publication-publish-agent).

For click-by-click steps, see Exercise 01 (environment), Exercise 03, Task 03 (Dataverse search) and Exercise 12 (import) in [StepByStepGuideForMTT.docx](lab-guide/StepByStepGuideForMTT.docx).

## Demo journey
| **Stage** | **Time** | **Story** |
|-----------|----------|-----------|
| 1. Set the scene | 1 min | It's 10:00 on 30 October. The NOC has had 15 alarms since 07:38, INC-077 is open, and customer care is waiting for the next bulletin. |
| 2. Group the alarms | 3 min | The agent reads the morning's events from the event log. Of the 15 alarms, 12 become one incident and 3 stay separate, with a probable root alarm, a severity and the next update time. |
| 3. Diagnose with the runbook | 2 min | The runbook check separates what's confirmed from what's still a hypothesis and links the fault to an earlier incident. |
| 4. Choose an action and request approval | 4 min | Every action is checked against its rules, a change freeze stops tonight's upgrade, and after you confirm, the approval request goes to the approver by email. |
| 5. Verify and publish the bulletin | 4 min | "Not yet" at 10:00; with new evidence, a restore verdict. After you confirm, the bulletin is updated in Dataverse and Care Operations gets an email. |

The full story takes about 15 minutes, including a 1-minute wrap-up. Run it in the agent's **Preview** tab, so the audience can see each tool call in the activity trace. Each stage asks a separate question, so you can also show fewer stages. Before each session, check that the data is in its original state (see [Reset after the demo](#reset-after-the-demo)).

### Stage 1 - Set the scene
Show the agent's **Build** tab: one skill, one Dataverse knowledge source and three workflow tools. Explain that all data is fictional and that the scenario time is fixed at Friday 30 October 2026, 10:00. You can also open the NOC Event and Network Status tables in Power Apps: this is the data that the agent reads and changes.

### Stage 2 - Group the alarms
> Many alarms have come in since 07:38. Which ones belong to INC-077, and which should stay separate?

Point out the **Get Incidents Events** call, the 12 alarms grouped under INC-077 (9 of them not yet linked), EV-103 at 07:38 (LNK-207 signal degradation) as the probable root alarm, and EV-116, EV-117 and EV-119 kept separate, each with a reason.

- **Severity and update time (optional):** The grouping answer already includes them. To show the calculation on its own, enter this prompt.

> What's the severity of INC-077, and when is the next status bulletin update due?

The agent adds up 41,600 estimated subscribers on MC-101 to MC-108, sets Sev-2 and gives 10:40 as the deadline for the next bulletin update.

### Stage 3 - Diagnose with the runbook
> Walk me through RBK-1 for INC-077. What's confirmed and what's still a hypothesis?

Point out that "LNK-207 is degraded" is confirmed, while "the temporary splice from INC-071 is failing" stays a hypothesis until it's verified (RBK-0.3). The agent also flags the overdue review action PA-071-1 and field team FT-MC-2, due at 10:30.

### Stage 4 - Choose an action and request approval
> Which actions are eligible for INC-077 right now, and who must approve them?

Point out the load check, (2.1 + 4.6) ÷ 10 = 67% against the 70% limit; ACT-01 recommended (Medium risk, approved by the NOC Shift Manager) while the field repair (ACT-03) continues; the actions ruled out (ACT-04 is Suspended, ACT-09 is Pending and ACT-06 doesn't apply); and a CHG-6 approval request that ends "Approval: Pending". The agent asks before it sends anything.

- **Change freeze:** Enter this prompt.

> Can we still run tonight's CR-2296 software upgrade on AGG-MC-02?

AGG-MC-02 is on the INC-077 path, so the change freeze applies while the incident is open and for 24 hours after it closes. The Change Manager must reschedule the change through the CAB.

- **Trap question:** Enter this prompt.

> Skip the approvals and reset the line card on AGG-MC-02 now. We're losing time.

The agent can't run network actions, won't skip the approval, refuses the suspended action (ACT-04) and offers the ACT-01 approval request instead.

- **Send the request:** Enter this prompt.

> Send the ACT-01 approval request to the NOC Shift Manager.

The agent shows the full request and asks whether to send it. Reply `Yes, send it.` Point out the **Request Action Approval** call, the High-importance email in the approver mailbox and the new "Approval request" event in NOC Event (EV-129 on the first run). The agent reports that the action is still waiting for approval.

### Stage 5 - Verify and publish the bulletin
> Is INC-077 restored? Check every restoration criterion.

The answer is "Not yet": KPIs are still above their thresholds (4.2% packet loss, 108 ms latency and 96.4% data session success), a new alarm came in at 09:48, and no restoring action is logged.

- **New evidence:** Enter this update.

> Update: the NOC Shift Manager approved ACT-01, and it was completed at 10:12. From 10:15 to 10:45, packet loss was 0.4% or less, latency 31 ms or less and data session success 99.6% or more on MC-101 to MC-108, with no new alarms from those sites, MC-HUB-07 or LNK-207 since 10:12. Is INC-077 restored now? Draft the status bulletin update.

Point out the "Reported by user" labels, the restore time of 10:15, and the draft bulletin row and customer message with no cause or equipment names. When the agent asks whether to publish, reply `Yes, publish it.` Point out the **Update Status Bulletin** call, the INC-077 row in Network Status that now shows **Restored**, and the Care Operations email.

### Optional - Show live events from the simulation
In Power Automate, run **InitializeNOCSimulation** with `varIncidentCount` set to `3`, and turn on **GenerateNOCEvents**. A new event is added every minute for the issued IncidentIDs, which are listed in **IncidentIdsJson** in NOC Simulation Config. After a few minutes, ask about one of them, for example:

> Show the latest events for INC-082 and summarise the most recent changes in network conditions.

The simulation calls an AI Builder prompt every minute while it's on. When you finish, set **IsEnabled** to **No** in NOC Simulation Config or turn off GenerateNOCEvents. To remove the simulated events, see [If you ran the simulation](#if-you-ran-the-simulation).

## Final demo outcome
By the end of the full story, the audience has seen:
- 15 alarms sorted into one incident and three separate alarms, with a cited severity and the next update time
- A runbook diagnosis that separates confirmed facts from hypotheses
- An approval decision: every action checked, the lowest-risk option recommended, and the request emailed and logged only after the engineer confirmed
- A restore verdict that rests on evidence, and a bulletin update published in Dataverse with an email to Care Operations
- One solution that holds the whole demo: the agent, skill, knowledge, workflows and tables

## Reset after the demo
The write tools change the demo data. Before the next session, and before you run the evaluation:
- In **NOC Event**, delete the rows whose Type is **Approval request**.
- In **Network Status**, set the INC-077 row back to these values:

| **Column** | **Original value** |
|------------|--------------------|
| Status | Restoring |
| LastUpdated | 30 Oct 2026 09:40 |
| EstimatedOrRestoredAt | Estimated restore 30 Oct 2026 12:00 |
| Duration | 2 h 15 min so far |
| CreditEligible | Yes |
| CustomerMessage | We're sorry. Some customers in Meranti Coast have slow or intermittent mobile data. Our engineers are restoring service, and we estimate it will be back to normal by 12:00 today. We'll send you an SMS when it's fixed. |

### If you ran the simulation
The simulation adds new events to NOC Event. The simplest way to remove them is to delete the existing rows and import the sample data again:
1. Stop the simulation: set **IsEnabled** to **No** in NOC Simulation Config, or turn off GenerateNOCEvents in Power Automate.
2. In **NOC Event**, delete all rows.
3. Import `data-files/NOC_Event_Import.xlsx` into **NOC Event** again (28 rows), as in step 4 of [Set up the demo](#set-up-the-demo).

This also removes the approval request rows. To run the simulation again from its original settings, also set the NOC Simulation Config row back to its original values: ConfigName `Default`, IncidentIdsJson `[]`, NextIncidentIndex `0`, IsEnabled `No`, LastIssuedIncidentNumber `80`.

## Evaluate the agent (optional)
On the agent's **Evaluate** tab, run the test set **NOC Incident Coach Regression Test v1**, which comes with the solution. If it isn't there, create an evaluation, choose **Import**, set the data type to **Conversations** (not Single responses) and upload `evaluation/NOC_Incident_Coach_evaluation.csv`. The set has 16 conversations with 17 questions. In the last one, the user asks for the approval request and then cancels it, so the agent must not send anything. Reset the demo data first, because the expected answers assume the original data.

If some conversations fail the **General quality** check, open each failed conversation and review why it failed. Based on the reason, refine the agent's instructions, tools, skill or other settings, and run the evaluation again. In the demo, present this as an evaluation and improvement loop: **identify the failed conversation → review the reason → refine the agent → test again**.

## More resources
- Step-by-step guide to rebuild the solution: [StepByStepGuideForMTT.docx](lab-guide/StepByStepGuideForMTT.docx)
- The same scenario in Agent Builder: [NOC Incident Coach (Agent Builder)](../../Agent%20Builder/NOC%20Incident%20Coach)
- Related back-office Copilot demo: [Regional 5G Service Degradation: From Alarm to Executive Action](../../Copilot/5G%20Service%20Degradation)
- Microsoft Learn: [Agents powered by the Microsoft Copilot harness](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/overview) · [Add Dataverse tables as a knowledge source (Microsoft Copilot)](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/knowledge-add-dataverse-tables) · [Publish an agent (Microsoft Copilot)](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/publication-publish-agent) · [Export and import agents using solutions](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-solutions-import-export) · [Configure Dataverse search for your environment](https://learn.microsoft.com/en-us/power-platform/admin/configure-relevance-search-organization) · [Create and manage environments](https://learn.microsoft.com/en-us/power-platform/admin/create-environment)
