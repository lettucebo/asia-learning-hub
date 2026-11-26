# Setup: Returns & Exchange Policy Coach

## Environment

Use Microsoft 365 Copilot Agent Builder with permission to create agents and access to the knowledge-upload capability. Tenant licensing and administrator settings must support the selected knowledge features. This demo needs no connectors, customer system, Azure resource, deployment tooling, or Work IQ.

## Configure

1. Create an agent in Agent Builder. Copy the name, description, instructions, and three starter prompts from [README.md](README.md).
2. Add **only** `knowledge/returns_policy.txt` and `knowledge/service_playbook.txt` as uploaded knowledge. Both are supported text files. Wait until both are available, then ask for their titles, versions, and RP-2. Do not upload the README or expected answers.
3. Turn off web search and **Reference people in organization**, and do not add email, Teams, broad SharePoint sites, or transaction tools. If your tenant exposes an option to prioritize or restrict answers to selected sources, enable it. This is a demo configuration, not a security guarantee that the model cannot use general knowledge; verify citations.
4. In a new conversation for each case, run all ten rows of [acceptance_tests.csv](acceptance_tests.csv). A pass needs the expected route, the specified rules, no forbidden claim, and the missing-facts behavior. Run the five-step demo after those checks.
5. Have another team member repeat setup and tests. Record verifier, date, and results below before sharing with a limited internal demo group. Uploaded knowledge can be exposed through the agent to people you share it with; these files contain only synthetic policy.

## Acceptance record

| Check | Status |
|---|---|
| Both policy sources retrieved with correct version | Pending tenant test |
| All ten acceptance cases pass | Pending tenant test |
| No actions or external knowledge enabled | Pending tenant inspection |
| Second-person reproduction | Pending; verifier and date not yet recorded |

If a rule is not retrieved, check that both files finished processing and ask for the relevant section. If a response ignores RP-2 or invents an approval, correct the configuration and repeat the failing case in a fresh conversation; do not present it as verified.

No publishing or deployment is performed by this repository pack. Reference: [Microsoft's Agent Builder knowledge guidance](https://learn.microsoft.com/microsoft-365/copilot/extensibility/agent-builder-add-knowledge).
