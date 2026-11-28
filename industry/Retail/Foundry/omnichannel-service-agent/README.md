# Juniper Lane Omnichannel Service Agent

[繁體中文](README.zh-TW.md)

**Microsoft Foundry Prompt Agent | Store fulfilment and customer care | Candidate walkthrough**

At fictional Juniper Lane Retail, a store colleague needs to decide whether to recover a pickup order or route a return for assessment. A status label is not a guarantee that an order is ready, and a final-sale label does not override reported faults. One agent distinguishes the two requests, shows the evidence, and hands the decision to the right colleague.

| Pain point | Benefit demonstrated |
| --- | --- |
| An old order snapshot can lead to an unnecessary pickup trip. | Checks the exact order and its age before suggesting a next step. |
| A final-sale label can hide a reported fault that needs specialist review. | Cites the applicable policy and routes the fault to the Quality Desk. |

## Demo

Start with [setup.md](setup.md). Use a fresh Playground conversation for each prompt.

| Ask | Expected decision |
| --- | --- |
| `Review CC-101 at the fixed demo time.` | The picking promise is due. Route an urgent check to the Store Fulfilment Lead (`CC-101`, `CR-3`); do not tell the customer to travel. |
| `Is CC-106 ready?` | The snapshot is 180 minutes old. Request a fresh status before making a recommendation (`CC-106`, `CR-1`). |
| `Final-sale item reported faulty after 45 days with no receipt.` | Route to the Quality Desk (`RP-2`) instead of rejecting it as a routine return. |

For the full presenter walkthrough, use the [22-case Playground guide](evaluation/playground.md). It includes all 23 English prompt turns, expected results, and 22 screenshots from a single v3 Playground run. Deviations and the isolated case that was not run are noted beside the prompts.

The demo uses six synthetic orders and fictional policies. It neither accesses live records nor sends messages, changes orders, reserves stock, or issues refunds. A draft is for colleague review. File Search is evidence retrieval, not an order database or an authorization boundary; never upload real customer records.

The case reuses the [Click & Collect Recovery Agent](../../Copilot%20Studio/Click%20%26%20Collect%20Recovery%20Agent/README.md) and [Returns & Exchange Policy Coach](../../Agent%20Builder/Returns%20%26%20Exchange%20Policy%20Coach/README.md) materials. No deployment of either source case is required.

**Delivery status:** The Playground walkthrough records one v3 run, not acceptance sign-off. Peer verification, version export, and SDK rebuild are still pending.
