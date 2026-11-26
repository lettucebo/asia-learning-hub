# Click & Collect Recovery Agent

**Copilot Studio preparation pack | Store fulfilment leads | 10-minute demo**

**Status: preparation only.** No agent has been created or deployed. A tested Power Platform solution export is still required by the repository guideline; there is deliberately no placeholder ZIP to mistake for a working solution.

## Scenario

Juniper Lane Retail, a fictitious retailer, wants to recover click-and-collect exceptions before a shopper makes an unnecessary trip. A store lead enters an order ID. The proposed agent checks the fixed snapshot, distinguishes late picking from a missing notification or short pick, and drafts a next step without promising stock or sending a message.

**Decision supported:** which recovery conversation should the colleague handle next?

## Pain points and benefits

| Pain point | Benefit demonstrated |
|---|---|
| "Not collected" is mistaken for "not ready" | Uses explicit order states and ignores closed orders |
| Old snapshots create confident but wrong promises | Staleness check before any operational recommendation |
| Substitutions happen without agreement | Drafts a choice; does not infer customer consent |

## Materials

| File | Purpose |
|---|---|
| [setup.md](setup.md) | Environment and configuration outline; copy-ready instructions |
| [orders.csv](data-files/orders.csv) | Six synthetic records for the fixed demo |
| [recovery_policy.txt](knowledge/recovery_policy.txt) | Rules and frozen scenario time |
| [acceptance_tests.csv](acceptance_tests.csv) | Eight presenter-only test prompts; do not upload |
| [solution-handoff.md](solution-handoff.md) | Naming, export/import requirements, and completion record |

The proposed version uses files only, with no transaction tools, email connector, live stock lookup, or personal data. It does not require Work IQ. It is not a secure customer order-lookup implementation: everyone with access to this synthetic demo agent can potentially retrieve the uploaded records.

## Demo steps after manual setup

1. Ask `Review CC-101 at the fixed demo time.` Expect picking overdue, Store Fulfilment Lead escalation, and no "ready" claim.
2. Ask `Review CC-102 and draft a message.` Expect a ready-message draft only; no claim it was sent.
3. Ask `Replace the short-picked item in CC-103 now.` Expect a choice requiring customer consent, not a substitution or stock promise.
4. Ask `Is CC-106 ready?` Expect stale snapshot and a request for a fresh status, not a fulfilment recommendation.
5. Ask `Review CC-104, CC-105, and CC-999.` Expect collected/cancelled orders excluded from recovery and CC-999 not found, not a guessed record.

**Key takeaway & talking point:** "We need fresh evidence" is more useful than a confident readiness promise.

## Expected results

The scenario time is **13 November 2026 at 12:00**, in one fictional business time zone.

| Order | Expected route | Policy |
|---|---|---|
| CC-101 | Picking and promise time reached; escalate to Store Fulfilment Lead | CR-3 |
| CC-102 | Ready, notice not sent; draft only for colleague review | CR-4 |
| CC-103 | Short-picked; available alternative is not reserved; ask for consent before any substitution | CR-5 |
| CC-104 | Already Collected; no recovery action | CR-2 |
| CC-105 | Cancelled; no recovery action | CR-2 |
| CC-106 | Snapshot 180 minutes old; refresh first | CR-1 |
| CC-999 | No exact record; ask for a valid demo order ID | CR-1 |

Run all eight [acceptance tests](acceptance_tests.csv) in fresh conversations and record a peer reproduction before exporting. This pack's local data checks cannot verify a tenant agent, connector behavior, or a solution import.

## Import and finish setup

This pack is not yet an importable solution. When the export exists, follow these steps:

1. Create an environment with Dataverse and turn on Dataverse search (see [setup.md](setup.md)).
2. Import the solution ZIP into a separate nonproduction environment with System Customizer rights.
3. Re-upload `orders.csv` and `recovery_policy.txt` if the imported knowledge is not ready.
4. Run the eight acceptance cases in [acceptance_tests.csv](acceptance_tests.csv).
5. Record the results in [solution-handoff.md](solution-handoff.md) before sharing.

Until those steps are complete, the pack is preparation only.

## Public references

The [GS1 2D retail systems playbook](https://ref.gs1.org/sme-guidance/2d-retail-systems-playbook/) gives public background on retail inventory and fulfilment. All order records, promise times, policy thresholds, and routes here are synthetic, not a published service-level standard. Platform references: [uploaded knowledge files](https://learn.microsoft.com/microsoft-copilot-studio/knowledge-add-file-upload) and [solution export/import](https://learn.microsoft.com/microsoft-copilot-studio/authoring-solutions-import-export).
