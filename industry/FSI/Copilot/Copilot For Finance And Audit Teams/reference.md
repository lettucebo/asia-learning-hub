# Prompt formula and review questions

[Workshop home](./README.md)

Every Meridian workshop uses the same prompt formula and the same six review questions. Learn them once, then use them in any app.

## The prompt formula

```text
Act as [role]. [Task] using /[file]. Focus on [what matters]. Give me [format]. Keep it [length / tone / audience]. Show where each point comes from.
```

| Part | What it covers | Example from Meridian |
| --- | --- | --- |
| Role | Who Copilot should act as | Act as an audit senior. |
| Task | What you want done | Summarise the three most significant findings |
| Source | The file Copilot must use (type / to reference it) | using /03_Audit_Findings_Draft.docx. |
| Focus | What matters most | Focus on financial exposure and evidence still outstanding. |
| Output | The format you want back | Give me 3 bullet points. |
| Constraints | Length, tone and audience | Keep it under 100 words for the engagement leader. |
| Verification | Ask Copilot to show where each point comes from | Show where each point comes from. |

**The whole example**

```text
Act as an audit senior. Summarise the three most significant findings using /03_Audit_Findings_Draft.docx. Focus on financial exposure and evidence still outstanding. Give me 3 bullet points. Keep it under 100 words for the engagement leader. Show where each point comes from.
```

## Three habits

- Say who it is for, what you want and the format
- Point Copilot at the source file (type / to reference it)
- Always check the answer against the source

Then: **Always ask a follow-up — the first answer is a starting point.**

## Status labels

Use these words when you check an answer, so everyone can see what is solid and what is not.

| Label | Meaning |
| --- | --- |
| ✓ Confirmed | The source states it. Quote it and name the file and place. |
| ≈ Inferred | Worked out from the sources, but not stated. Say that you worked it out. |
| ? Assumed | Taken as true without a source. Check it or leave it out. |
| ⇄ Conflicting | Two sources disagree. Report both. Do not pick one silently. |
| … Unresolved | Still open. Say what evidence would close it. |

## The six review questions

Run your final result through all six, every time. Completing the checks does not approve the result. A person decides.

| Dimension | Question |
| --- | --- |
| Source | Did the learner use the correct controlling file or mock content record? |
| Evidence | Can each fact, number, owner, date, and conclusion be traced to the source? |
| Status | Are confirmed, inferred, assumed, conflicting, and unresolved points distinguished? |
| Audience | Is the result suitable for the intended engagement leader, CFO, Finance Director, or team? |
| Action | Does the output identify the decision, evidence request, owner, due date, or next step? |
| Professional boundary | Does the result avoid an audit opinion, tax advice, unsupported approval, or invented completion claim? |

## Ground rules

- All Meridian data is fictional — no real client information
- Do not add personal or client data to prompts
- Copilot can be wrong: verify numbers before you reuse them
- No personal information about members of the public in prompts
- Follow your agency’s AI-use and classification guidance

## Glossary

| Word | What it means |
| --- | --- |
| Engagement team | The group of auditors working on one client. You have just joined it. |
| Finding | A problem the team spotted, written up: what happened, why it matters, what to do. |
| Evidence | Proof you can point to: a document, a record or a number from the files. |
| Inconsistency | Two places that say different things about the same fact. |
| Executive summary | A short note for busy leaders. Only the main points. |
| Source file | The document an answer came from, so you can check it. |
| Journal entry | One line in the company’s accounting records, in the General_Ledger sheet. Meridian has 1,800. |
| Manual journal | An entry typed in by a person, not created automatically by a till, online shop or system. |
| Self-approved | The same person prepared and approved the entry, so no second person signed it off. |
| Flag | A marker that says look here. It is a pointer for checking, not proof of anything. |
| Related party | A business closely linked to the company or its leaders. Deals with it get extra checking. |
| Dormant vendor | A supplier marked as inactive. A payment to one needs a good explanation. |
| Executive briefing | A short deck for leaders. A few slides, one clear message each. |
| Rating | How serious a finding is: High, Medium or Low. Some are blank in the draft. |
| Owner and target date | The person who will fix a finding, and the day they promise to do it. |
| Speaker notes | Private words under a slide that help the presenter. The audience does not see them. |
| Evidence request | An item asking the client for a document or record that proves something. `06_Supporting_Documents.pdf` lists six. |
| Board meeting | The meeting of Meridian's top decision-makers on 20 February 2027. The audit should finish before it. |
| Blocked item | Stuck until the evidence it needs arrives. The email never says "blocked"; you work that out. |
| Unsupported | Not backed by the email or a file. Leave it flagged, and never fill it in. |
| Diplomatic tone | Polite, team-minded wording that still keeps the ask and the date clear. |
| Draft | A reply that is saved but not sent. Nobody sees it until a person decides to send it. |
| Catch-up summary | A short recap of a busy chat: what was decided, what is open, who owns what. |
| Citation | A link from a point in the summary back to the exact message it came from. |
| Open item | Something still unresolved: evidence not yet received, a question not yet answered. |
| Action owner | The one named person responsible for an action. No name means no owner. |
| Status meeting | A short meeting to check progress on open items with the client. Tomorrow’s lasts 30 minutes. |
| Training chat | A practice chat with fictional data only. Never a real client or team conversation. |
| Evidence trail | The same amount followed from file to file, to see what supports it. |
| Exposure | The money that could be wrong or at risk. A possible amount, not a proven loss. |
| Confirmed or assumed | Confirmed means a document says it. Assumed means someone, or Copilot, supplied it without proof. |
| Year-end revenue | A sale booked right at the year end. The team checks it truly belongs in that year. |

> [!IMPORTANT]
> Copilot proposes; the team verifies. This is a training exercise, not audit or tax advice.
