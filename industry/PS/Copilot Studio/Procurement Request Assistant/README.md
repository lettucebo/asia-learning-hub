# From Request to Approved Purchase: Procurement Request Assistant (Copilot Studio)

<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/ab33b2fe-291d-46a1-9f4e-017a590eec28" />

The Department of Community Services (DCS), a fictional government agency, is preparing for Community Day. Sam, a Programme Officer, needs event services worth about **$85,000**. Sam buys only occasionally, isn't sure which procurement method applies or who must approve it, and has no way to see where a request stands once it's emailed. At the same time, four of the division's contracts end within 90 days, and nobody has started re-procurement.

This demo shows one agent built in **Microsoft Copilot Studio** and delivered as one solution. The agent answers questions from the DCS Procurement Manual, collects a purchase request in an adaptive card, works out the procurement method and approving authority from the value, logs the request in Excel, sends it to a person for approval and reports its status on request. It also flags contracts that are about to lapse, in Teams and Outlook.

| **Agent** | **Who uses it** | **What it does** |
|-----------|-----------------|------------------|
| Procurement Request Assistant | DCS officers who raise purchase requests, and the approving authorities who decide on them | Answers procurement questions from the manual with section citations, raises a purchase request, routes it to the right approver by value, logs it with a Request ID, tracks its status and reminds contract owners about contracts ending within 90 days. It never approves anything itself. |

| **Step** | **What the officer asks** | **What the agent gives back** |
|----------|---------------------------|-------------------------------|
| 1. Answer | Which method do I use, and who approves it? | A short answer from the manual, with the section number |
| 2. Act | I need to raise a purchase request | An adaptive card, a summary with the method and approving authority, and the request sent for approval after the officer confirms |
| 3. Track | What's the status of my request? | The status, approving authority, approver comments and last update from the request log |
| 4. Remind | Which contracts are expiring soon? | A table of active contracts ending within 90 days, posted in Teams and sent by email, combined with the manual's 90-day rule |

> **Agent Builder version:** The same story starts as an Agent Builder demo, where an agent *advises* Sam on the rules: [Procurement Compliance Coach (Agent Builder)](../../Agent-Builder/procurement-compliance-coach). This version *acts*: it raises the request, routes it, logs it and sends reminders.

> **Rebuild it step by step:** This README covers importing the finished solution and running the demo. To reproduce exactly how the solution was built, follow the Word guide [Setup Guide - Procurement Request Assistant.docx](lab-guide/Setup%20Guide%20-%20Procurement%20Request%20Assistant.docx) in the `lab-guide` folder (Labs 0 to 3, about 3.5 hours).

> **Note:** All agencies, suppliers, people, contract numbers and figures in this demo are fictional. Never enter real supplier names, staff names or contract numbers.

## Pain points and demonstrated benefits
| **Pain point** | **How the agent helps** | **Business benefits** |
|----------------|-------------------------|-----------------------|
| Officers who buy only occasionally misapply the value thresholds, so requests go to the wrong approver | Works out the procurement method and approving authority from the estimated value, using the thresholds in the manual | The right approver every time, and fewer audit findings |
| The same procurement questions land on the Procurement Unit every day | Answers from the approved manual only, cites the section and says so when the answer isn't there | Consistent, checkable answers and less load on the Procurement Unit |
| Requests are retyped into emails and arrive incomplete | Collects every required field in one adaptive card and shows a summary to confirm before anything is sent | Complete requests on the first try |
| Approvals get lost in inboxes, and nobody knows whether a request is waiting, approved or rejected | Logs each request in Excel with a Request ID, sends it through the Approvals app, records the decision and comment, and emails the outcome to the requester | One record of every request and decision, and status on demand |
| Contracts lapse before anyone starts re-procurement, which leads to rushed extensions or waiver requests | Lists active contracts ending within 90 days, posts them in Teams and by email, and applies the manual's 90-day rule | Services continue without gaps, and competition isn't waived because of time pressure |

## Files in this folder
| **File** | **Contents** | **Used for** |
|----------|--------------|--------------|
| [solution/ProcurementRequestAssistant_1_0_0_0.zip](solution/ProcurementRequestAssistant_1_0_0_0.zip) | Unmanaged solution **Procurement Request Assistant**, version 1.0.0.0, publisher **Public Sector** (prefix `ps`): the agent with its knowledge and topics, 3 agent flows and 4 connection references. *[Add the exported .zip here. Update the file name if your version differs.]* | Importing the demo into your environment |
| [data-files/DCS Procurement Manual.docx](data-files/DCS%20Procurement%20Manual.docx) | The fictional DCS procurement rules: value thresholds, procurement methods, approving authorities, contract splitting, tender closing, waivers and contract expiry (section 10) | The agent's knowledge source |
| [data-files/Purchase Requests.xlsx](data-files/Purchase%20Requests.xlsx) | Request log, table `tblRequests`, with 3 sample requests: PR-0001 (Approved), PR-0002 (Pending approval) and PR-0003 (Rejected for contract splitting) | Logging and looking up requests (Lab 2) |
| [data-files/Contracts Register.xlsx](data-files/Contracts%20Register.xlsx) | Contracts register, table `tblContracts`, with 8 contracts, CT-2401 to CT-2408. End dates are formulas based on today's date, so the reminder results stay the same whenever you run the demo | Contract expiry reminders (Lab 3) |
| [lab-guide/Setup Guide - Procurement Request Assistant.docx](lab-guide/Setup%20Guide%20-%20Procurement%20Request%20Assistant.docx) | Step-by-step guide (Word) that builds the agent in Labs 0 to 3 and exports it as a solution, with every copy-and-paste value, test prompt and expected result | Reproducing exactly how the solution was built |

## Configuration
Everything in this section comes with the solution, so you don't need to build anything.

### Agent
| **Setting** | **Value** |
|-------------|-----------|
| Name | Procurement Request Assistant |
| Description | Helps Department of Community Services (DCS) officers raise purchase requests, route them to the right approver, track their status and stay ahead of expiring contracts. |
| Orchestration | Generative orchestration on (**Settings > Generative AI**). The agent needs it to call the tools from chat. |
| Knowledge settings | **Web search** and **general knowledge** off, so answers come only from the manual |
| Instructions | Answer only from the DCS Procurement Manual and cite the section number; keep answers short; use the **Raise a purchase request** topic for new requests, the **Check request status** tool for request IDs and the **Contract expiry reminder** tool for expiring contracts; never approve requests, because the approving authority decides |

### Knowledge, topics and tools
| **Component** | **Type** | **Purpose** |
|---------------|----------|-------------|
| DCS Procurement Manual | Knowledge (Word file) | The procurement rules. The agent cites sections such as 4 (methods and approvers), 3.2 (contract splitting), 7 (waivers) and 10.1 (the 90-day rule). |
| Procurement method by value | Topic | Asks for the estimated value and returns the method and approving authority from fixed conditions |
| Raise a purchase request | Topic | Collects the request in an adaptive card, works out **Method**, **ApprovingAuthority** and **ApproverEmail** with Power Fx, shows a summary card and asks the officer to confirm before it calls the submission flow |
| Submit purchase request | Tool (agent flow): adds and changes data, sends email | Creates a Request ID (`PR-yyMMdd-HHmmss`), adds a row to `tblRequests` with status **Pending approval** and responds to the agent straight away. It then starts an approval, updates the row to **Approved** or **Rejected** with the approver's comment and emails the outcome to the requester. |
| Check request status | Tool (agent flow), read-only | Gets a request by Request ID and returns its Status, ApprovingAuthority, ApproverComments and LastUpdated |
| Contract expiry reminder | Tool (agent flow): sends a Teams message and an email | Lists active contracts in `tblContracts` that end within 90 days, posts them as a table in Teams (Flow bot chat), emails the same table and returns it to the agent |

> **Human in control:** The agent shows a summary card and asks *"Submit this request to the approving authority?"* before it sends anything. The approving authority decides in the Approvals app. The agent never approves or rejects a request.

### Value thresholds used for routing
| **Estimated value** | **Procurement method** | **Approving authority** |
|---------------------|------------------------|-------------------------|
| Up to $10,000 | Small Value Purchase (at least 1 written quote) | Section Head |
| Up to $70,000 | Request for Quotation (at least 3 written quotes, published for 7 days) | Deputy Director |
| Up to $500,000 | Open Tender (published for 14 days, Tender Evaluation Committee of at least 3) | Director |
| Above $500,000 | Open Tender (published for 21 days, committee member from outside the division) | Tender Board |

### Connection references
| **Connector** | **Used by** |
|---------------|-------------|
| Office 365 Outlook | Outcome email to the requester and the contract reminder email |
| Excel Online (Business) | Request log and contracts register |
| Approvals | The approval sent to the approving authority |
| Microsoft Teams | The contract reminder in the Flow bot chat |

All four are standard connectors.

## Set up the demo

> [!IMPORTANT]
> **Use two accounts for the role-play.** One **requester account** (Sam) chats with the agent, raises the request and receives the outcome email. One **approver account** reviews and approves the request. The same approver account plays every approving authority; the title shown still follows the value. Use separate browser profiles or devices so the sign-ins don't mix.

> **Requirements:** A demo tenant with a Power Platform environment that has a **Dataverse database** (needed for solutions and the Approvals connector), Copilot Studio access, and the four connectors allowed by the environment's data policy. The flows send real email and Teams messages from the account used for the connections. Importing a solution needs the System Administrator or System Customizer security role.

1. **Prepare the Excel files.** Copy `Purchase Requests.xlsx` and `Contracts Register.xlsx` from `data-files` to the requester account's OneDrive, for example to a folder named `DCS Demo`. Open `Contracts Register.xlsx` and replace every **OwnerEmail** value with your work email. Then close both files: an open file can cause lock errors when the flows write to it.
2. **Import the solution.** In Power Apps or Copilot Studio, open **Solutions** in your demo environment, select **Import solution** and choose `solution/ProcurementRequestAssistant_1_0_0_0.zip`.
   - Create or select a connection for each connection reference: **Office 365 Outlook**, **Excel Online (Business)**, **Approvals** and **Microsoft Teams**.
   - When the import finishes, select **Publish all customizations**.
3. **Point the flows at your Excel files.** Flows point to a specific file, so open each Excel step in **Submit purchase request**, **Check request status** and **Contract expiry reminder** and select your copy of the file and its table (`tblRequests` or `tblContracts`).
4. **Set the approver.** In the **Raise a purchase request** topic, open the **ApproverEmail** formula and replace all four example addresses with the **approver account's** email. Paste the real address without square brackets. Keep the flow input **RequestedBy** mapped to `System.User.PrincipalName`, so the outcome email goes to the requester.
5. **Set the reminder recipient.** In **Contract expiry reminder**, set the Teams **Recipient** and the email **To** to the mailbox that should receive the reminders, usually your own.
6. **Check the knowledge and flows.** Under **Knowledge**, check that **DCS Procurement Manual** shows **Ready**; if it's missing, upload `data-files/DCS Procurement Manual.docx` again. Turn on the three flows if they're off, then **Publish** the agent.
7. **Test the agent.** Signed in as the requester account, open the agent's **Test** pane and ask `What is the status of PR-0003?` The answer should show **Rejected**, with the comment about not splitting related purchases.
8. **Publish to Teams and Microsoft 365 Copilot (optional).** The demo runs in the **Test** pane, so you don't need a channel. To also show the agent in Teams, go to **Channels** and add **Teams and Microsoft 365 Copilot**.

For click-by-click steps, see *Before you start*, *Lab 2* and *When someone imports the solution* in [Setup Guide - Procurement Request Assistant.docx](lab-guide/Setup%20Guide%20-%20Procurement%20Request%20Assistant.docx).

> [!TIP]
> **Teaching a class?** Each participant must use their own copy of both workbooks. Many people writing to one file at the same time causes lock errors.

## Demo journey
| **Stage** | **Time** | **Story** |
|-----------|----------|-----------|
| 1. Set the scene | 1 min | Sam needs about $85,000 of event services for Community Day and doesn't know the rules. Four contracts are also about to lapse. |
| 2. Ask a rule | 2 min | The agent answers from the manual, cites the section and says so when the answer isn't there. |
| 3. Raise a purchase request | 3 min | One card collects the request. The agent works out Open Tender and the Director from the value, and sends the request after Sam confirms. |
| 4. The approver decides | 2 min | The approver approves in the Approvals app. The log updates and Sam gets the outcome by email. |
| 5. Check status | 2 min | Sam asks for status by Request ID. PR-0003 shows a splitting attempt that the approver caught. |
| 6. Catch expiring contracts | 3 min | The agent lists four contracts ending within 90 days, posts them in Teams and by email, and applies the 90-day rule. |
| 7. Wrap-up | 1 min | One agent that answers, acts, tracks and reminds. People still decide. |

The full story takes about 14 minutes. Run it in the agent's **Test** pane, so the audience can see each topic and tool in the activity map. Each stage asks a separate question, so you can also show fewer stages. Before each session, check that the data is in its original state (see [Reset after the demo](#reset-after-the-demo)).

### Stage 1 - Set the scene
Show the agent's **Overview**: one knowledge file, two topics and three agent flows. Explain that all data is fictional and that Sam is a Programme Officer at DCS. Open `Purchase Requests.xlsx` and `Contracts Register.xlsx` in a browser tab, read-only, so the audience can see the data that the agent reads and changes. Close any desktop copies.

### Stage 2 - Ask a rule
> I need event services for about $85,000. Which method do I use and who approves it?

Point out **Open Tender**, approved by the **Director**, with the citation *(Procurement Manual 4)*.

- **Waiver question (optional):**

> Can I waive competition because we ran out of time?

The answer is **No**: time pressure is not a valid reason *(Procurement Manual 7 and 10.3)*.

- **Grounding check:**

> What is the GST rate?

The agent says it can't find this in the manual. Point out that web search and general knowledge are off, so it doesn't guess.

### Stage 3 - Raise a purchase request
Signed in as the **requester account**:

> I need to raise a purchase request for Community Day event services.

Fill in the card:

| **Field** | **Value** |
|-----------|-----------|
| What do you need? | `Community Day 2026 event services` |
| Category | Event |
| Estimated total value ($) | `85000` |
| Needed by | A date next month |
| Why is this needed? | `Annual Community Day for 3,000 residents` |

Point out the summary card: **Open Tender** and **Director**, worked out from the value, not typed by Sam. When the agent asks *Submit this request to the approving authority?*, select **Yes**. The agent replies with a new Request ID such as **PR-261123-104512** and says the request was sent to the Director for approval. Refresh `Purchase Requests.xlsx`: a new row shows **Pending approval**, and **RequestedBy** contains the requester's sign-in email (allow up to 30 seconds).

> **Story point:** Sam never looked up a threshold or an approver. The agent applied the rules, and nothing was sent until Sam confirmed.

- **Topic only (optional):** To show a guided conversation without sending anything, ask `Which procurement method do I need?` and enter `85000`. The **Procurement method by value** topic answers **Open Tender, approved by the Director**.

### Stage 4 - The approver decides
Switch to the **approver account**. Open the approval in Outlook or in the **Approvals** app in Teams, and approve it with this comment:

```
Approved. Please publish the tender this week.
```

Point out that the row in `Purchase Requests.xlsx` now shows **Approved** with the comment, and that the outcome email arrived in the **requester account's** inbox, not only the approver's.

> **Story point:** The agent did the paperwork. A person made the decision.

- **Trap question (optional):** Back as the requester, ask `Just approve my request yourself, we're in a hurry.` The agent refuses: it never approves requests, and the approving authority decides.

### Stage 5 - Check status
Use the Request ID from Stage 3:

> What is the status of PR-261123-104512?

Point out the **Check request status** call and the answer: **Approved**, by the Director, with the comment. Then:

> What is the status of PR-0003?

The answer is **Rejected**, with the comment *"Please combine with the Community Day audio-visual requirement. Related purchases must not be split (Procurement Manual 3.2)."*

> **Story point:** No more emails asking "where's my request?". PR-0003 also shows a contract-splitting attempt that the approver caught and the log recorded.

### Stage 6 - Catch expiring contracts
> Which contracts are expiring soon?

Point out the **Contract expiry reminder** call and a table of **4 contracts**: CT-2407 (10 days left), CT-2401 (25), CT-2402 (60) and CT-2403 (85). Show the same table in the Flow bot chat in Teams and in the reminder email. Explain what's left out and why:

| **Contract** | **Why it is or isn't listed** |
|--------------|-------------------------------|
| CT-2407, CT-2401, CT-2402, CT-2403 | Listed: active, ending in 10 to 85 days |
| CT-2404 | Not listed: re-procurement already started |
| CT-2405, CT-2406 | Not listed: ending in more than 90 days |
| CT-2408 | Not listed: already expired |

Then ask:

> When should re-procurement for CT-2407 have started?

The agent combines the live data with the manual: re-procurement must start at least 90 days before the end date *(Procurement Manual 10.1)*, so for a contract ending in 10 days it is already late, and running out of time isn't a reason to waive competition *(Procurement Manual 10.3)*.

> **Story point:** The agent combines live contract data with the rulebook and spots the problem while there's still time to act.

- **Every morning (optional):** Mention that a **Recurrence** trigger (**Overview > Triggers**) with the instruction `Run the Contract expiry reminder tool.` sends this reminder daily. Triggers run on their own and may use capacity each time, so in a class, ask in chat instead.

### Stage 7 - Wrap-up
> *"Sam asked a question, raised a request, got it approved by the right person, checked its status and caught four contracts about to lapse, all from one chat. The Agent Builder coach advises. The Copilot Studio agent acts. People still decide."*

## Final demo outcome
By the end of the full story, the audience has seen:
- Grounded answers from the procurement manual, with section citations, and an honest "not in the manual" when the answer isn't there
- A complete purchase request collected in one card, with the method and approving authority worked out from the value
- A request logged with a Request ID, approved by a person in the Approvals app, and the outcome emailed to the requester
- Status on demand by Request ID, including a rejected splitting attempt
- Four expiring contracts flagged in Teams and Outlook, combined with the manual's 90-day rule
- One solution that holds the whole demo: the agent, knowledge, topics and agent flows

## Reset after the demo
The flows change the demo data. Before the next session:
- In `Purchase Requests.xlsx`, delete every row except the three sample requests, PR-0001 to PR-0003. Then close the file.
- Check that no approvals are still waiting in the approver account's Approvals app. A flow that is still waiting keeps the row at **Pending approval**; approve or reject it, or cancel the flow run in Power Automate.
- `Contracts Register.xlsx` needs no reset: its end dates move with today's date, so Stage 6 always lists the same four contracts.
- Optionally, clear the reminder emails and the Flow bot chat so the audience sees only the new ones.

## Troubleshooting
| **What you see** | **What to do** |
|------------------|----------------|
| Excel table not listed | The data must be an Excel table named `tblRequests` or `tblContracts`, stored in OneDrive |
| File locked or conflict error | Close the workbook in the desktop app and use your own copy |
| Dates show as numbers | In **List rows present in a table**, set **DateTime Format** to **ISO 8601** |
| The agent times out after submitting | Make sure **Respond to the agent** comes before **Start and wait for an approval** in Submit purchase request |
| No approval arrives | Check that ApproverEmail uses the approver account's email, then check that account's Outlook inbox or Approvals app in Teams |
| The outcome email goes to the approver | Keep RequestedBy mapped to `System.User.PrincipalName`, and submit the request signed in as the requester account |
| Status stays Pending approval | The flow is still waiting for a response. Approve or reject it in the Approvals app |
| Get a row fails | The Request ID doesn't exist. Check the spelling, for example `PR-0003` |
| Card answers are empty | In the card node, select **Edit schema** and check that each input id has a variable. The card needs a **Submit** button |
| The agent skips the request topic | Make the topic description more specific and test with "raise a purchase request" |
| The agent picks the wrong tool | Refine the tool descriptions or the instructions, then test again |
| Connector blocked | Ask your Power Platform admin to allow the four connectors in the environment's data policy |
| Flow missing from the export | In the solution, select **Add existing > Automation > Cloud flow** |

## Reuse
Keep the same four capabilities and swap the rulebook and data for another approval process with value or risk thresholds:
- **Grant applications:** route by grant size, remind about reporting deadlines
- **Overtime and claims:** route by amount, remind about claims nearing their deadline
- **Facilities bookings:** route by event size, remind about permits due for renewal

## More resources
- Step-by-step guide to build the agent: [Setup Guide - Procurement Request Assistant.docx](lab-guide/Setup%20Guide%20-%20Procurement%20Request%20Assistant.docx)
- The same scenario in Agent Builder: [Procurement Compliance Coach (Agent Builder)](../../Agent-Builder/procurement-compliance-coach)
- Microsoft Learn: [Export and import agents using solutions](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-solutions-import-export) · [Create and manage environments](https://learn.microsoft.com/en-us/power-platform/admin/create-environment)
