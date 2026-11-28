# Setup: Juniper Lane Omnichannel Service Agent

[繁體中文](setup.zh-TW.md)

## Before using a Foundry project

Use an existing, approved nonproduction [Microsoft Foundry](https://ai.azure.com/) project. Confirm the selected region, compatible model deployment, quota, and access to File Search and request evidence. Use Microsoft Entra sign-in and the **Foundry User** role on the project. Where project-backed storage is used, confirm the required **Storage Blob Data Contributor** access on that storage account. Ask the project owner to approve resource creation, synthetic file uploads, and model and File Search charges. Do not create or change shared infrastructure for this demo.

[Foundry RBAC](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry) · [File Search setup and supported formats](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/file-search)

## A. Build and verify in the Foundry portal

If an authorized operator already created a candidate with Azure CLI, skip steps 1 and 2. Open that agent and verify the saved version, approved deployment, instructions, and File Search binding before proceeding. CLI creation does not replace Playground acceptance.

1. Open the new Foundry experience. On the project home page, select **Create an agent** under **Build an agent**. Use a new name such as `juniper-lane-omnichannel-portal`; stop on a name collision. Keep the default managed Prompt Agent runtime, not the Copilot harness. Pick the approved deployment and paste [instructions.txt](portal/instructions.txt).
2. Add **File Search** with a case-specific vector store. Upload only the four files below and wait until all four are indexed. Keep the store unchanged during verification. Do not add other tools, sources, or skills. If the portal cannot complete the setup, stop; do not substitute SDK provisioning for the portal build. If the portal offers only a Toolbox-backed binding, confirm that SDK-only recreation of its dependencies is supported before adopting it.
3. Save and note the exact version. Run the cases in [evaluation](evaluation/README.md) against that saved version, except `FD-04`, which uses the isolated configuration described there. Check response details and traces against the required evidence; a claimed citation is not proof. Have another team member reproduce the setup and record the results. Do not publish to a channel.
4. After the checks pass, use the official [Get an agent version](https://learn.microsoft.com/en-us/azure/foundry/reference/rest/agents-get-agent-version) API to retrieve that exact name and version, not `latest`. Preserve behavior settings and the tool binding in a sanitized version JSON. Pair it with an asset manifest (paths, hashes, model and tool requirements, and any vector-store or Toolbox settings needed to reproduce the binding) and the acceptance record. Replace project-specific IDs, private endpoints, and deployment names with documented logical references; do not include tokens, tenant IDs, or raw traces. This is a version snapshot plus dependencies, not an importable ZIP.

| Upload | Purpose |
| --- | --- |
| [orders_lookup.txt](knowledge/orders_lookup.txt) | Keyed snapshot of the six [original CSV records](data/orders.csv). File Search uses text, not the CSV. |
| [recovery_policy.txt](knowledge/recovery_policy.txt) | Pickup rules `CR-1`–`CR-6` and the fixed scenario clock, `2026-11-13 12:00`. |
| [returns_policy.txt](knowledge/returns_policy.txt) | Return assessment, exceptions, and escalation rules `RP-1`–`RP-6`. |
| [service_playbook.txt](knowledge/service_playbook.txt) | Return response format, draft wording, and data boundaries. |

The CSV and three policy text files are verbatim source snapshots; their origins are the two cases linked in the [README](README.md). The tabular lookup is derived from the CSV without adding records. [SHA256SUMS](SHA256SUMS) records the case-relative hashes for the data, uploaded knowledge, and inherited acceptance files. Hashes apply to the canonical LF files. Do not upload evaluation inputs or answers as knowledge.

## B. Rebuild with the SDK after accepting the export

Pending. After the portal baseline is accepted, use the [Azure AI Projects Python SDK](https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/prompt-agent) to recreate the knowledge dependencies and a separate managed Prompt Agent in Foundry Agent Service. The SDK version must run the same acceptance matrix without using the portal agent or its knowledge resources. No SDK implementation ships with this preparation pack.
