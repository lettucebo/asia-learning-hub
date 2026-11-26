# Campaign Launch Readiness

**Microsoft 365 Copilot | Chat, Excel, Word, PowerPoint, Teams, Outlook | 20 minutes**

## Scenario

Juniper Lane Retail, a fictitious retailer, plans an **Everyday Essentials** campaign for 16 November 2026. The commercial lead needs a go/no-go recommendation before spending launch budget. Creative assets can look finished while an incorrect offer or an untested checkout still blocks release.

The decision: **what must be cleared before launch, and who needs to verify it?** This is a readiness review, not another sales-performance report.

## Pain points and benefits

| Pain point | Benefit demonstrated |
|---|---|
| Readiness is scattered across email and task lists | One cross-channel evidence view |
| A completion percentage hides mandatory blockers | Explicit gates and severity, not majority voting |
| Owners receive vague follow-ups | Evidence requests with accountable roles and deadlines |

## Files and preparation

| File | Purpose |
|---|---|
| [launch_readiness.xlsx](sample-files/launch_readiness.xlsx) | Excel table `LaunchChecks`, 12 checks |
| [launch_checks.csv](sample-files/launch_checks.csv) | Editable source for the same table |
| [launch_brief.txt](sample-files/launch_brief.txt) | Scope, launch gate, and exact readiness rules |
| [meeting_script.txt](sample-files/meeting_script.txt) | Roles and decisions for a short Teams review |

Use licensed Microsoft 365 Copilot in the six apps. Save the workbook and brief to a writable OneDrive or SharePoint demo folder. Use a copy of the workbook; confirm the Excel table. Select or attach files using available controls. If another app cannot reference a source file, paste the brief and checked findings. Teams requires an actual meeting with permitted transcription; the supplied role-play is not a pre-existing recap.

The fixed review time is **13 November 2026, 12:00**, in a fictional shared business time zone. All records and policies are synthetic; no real campaign is changed.

## Demo steps

### 1. Frame the decision - Chat

Attach `launch_brief.txt`:

```text
Explain the Everyday Essentials launch decision, mandatory launch gate,
review time, and definition of overdue. List what we must not infer from a
task marked Complete. Use only this brief; do not invent campaign results.
```

### 2. Expose hidden blockers - Excel

Open `launch_readiness.xlsx`, with the brief available as context (paste its rules if needed):

```text
Using LaunchChecks, count checks by status and channel. Create a blocker
table of Mandatory = Yes AND Status <> Complete. Mark Overdue only when
Status <> Complete AND DueAt is strictly before 2026-11-13 12:00.
Count completed mandatory checks separately from all completed checks.
Do not round a readiness percentage into launch approval. Keep evidence
references and owner roles in the blocker table; do not change source status.
```

**Key takeaway & talking point:** The campaign is 75% complete, but mandatory checkout and offer gates remain open.

### 3. Draft the decision and leadership view - Word and PowerPoint

Paste the verified blocker table and launch brief into Word:

```text
Draft a one-page launch recommendation: current gate verdict, mandatory
blockers with evidence IDs, overdue work, decisions required, and proposed
next steps. No-go is a current recommendation, not a cancellation.
Do not claim a waiver, test pass, budget saving, or owner agreement.
```

Save the reviewed document as `Launch_Decision_Brief.docx`. In PowerPoint, reference it or paste its text:

```text
Create four slides: launch decision, channel readiness, mandatory blockers,
and evidence required to revisit the decision. Include the 13 November
12:00 review time. Clearly separate mandatory gates from optional work.
```

### 4. Confirm ownership - Teams

Read [meeting_script.txt](sample-files/meeting_script.txt) in a transcribed meeting. Ask Teams Copilot:

```text
List the decisions, agreed owner roles and deadlines. Distinguish the
agreed evidence-gathering actions from actual test completion or launch
approval. What decision must be revisited at 16:00?
```

### 5. Request evidence - Outlook

Paste the reviewed recap:

```text
Draft an internal email under 150 words asking the two mandatory blocker
owners for the agreed evidence by 15:00 on 13 November 2026. Mention the
16:00 re-review and the current no-go recommendation. Do not imply the
tests passed, waive a gate, add recipients, or send.
```

## Expected results

| Check | Expected |
|---|---|
| All checks | 12; 9 Complete, 2 Blocked, 1 In progress; 75% complete |
| Mandatory checks | 10; 8 Complete, 2 Blocked; 80% complete |
| Mandatory blockers | LC-04, checkout discount mismatch (E-04); LC-07, unapproved store offer artwork (E-07) |
| Overdue at fixed review time | LC-04 and LC-11 only; LC-07 is due at 15:00, not overdue at noon |
| Optional open check | LC-11, creator captions; overdue but not a mandatory launch gate |
| Current gate verdict | No-go until LC-04 and LC-07 are Complete with approved evidence |
| Teams decisions | Digital Commerce Lead and Brand Lead supply evidence by 15:00; Commercial Lead re-reviews at 16:00 on 13 November |
| No fabricated outcomes | No checkout pass, artwork approval, or launch approval recorded by the agent |

**Boundary tests:** "Launch anyway because 75% is good enough" must not override the brief. "LC-07 is already overdue at noon" must be corrected. A peer must check these cases and run the flow; tenant execution and peer verification remain pending.

## Public reference

The public [GS1 2D retail systems playbook](https://ref.gs1.org/sme-guidance/2d-retail-systems-playbook/) gives background on retail-system readiness and pricing accuracy. It does not prescribe this campaign's launch process. All tasks, timings, rules, and figures are fictional; no GS1 certification is claimed. Platform reference: [Copilot in Excel FAQ](https://support.microsoft.com/en-us/excel/copilot/frequently-asked-questions-about-copilot-in-excel).
