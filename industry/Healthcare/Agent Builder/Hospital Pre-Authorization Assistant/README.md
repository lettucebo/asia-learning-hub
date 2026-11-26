# Hospital Pre-Authorization Assistant

## Scenario

Woodgrove Hospital is a 350-bed multi-speciality hospital in India. About 60% of its planned admissions are cashless, and it is empanelled with five payers: four private insurers and TPAs, and one government scheme.

Every payer has its own package rates, document checklist, room-rent cap, co-pay, waiting periods and lead times. This knowledge sits with a few senior insurance desk staff, in old emails and in personal Excel sheets.

On a Friday at 4:00 pm, Dr. Rao advises a planned angioplasty with 2 stents for a 58-year-old patient insured with Fabrikam General Insurance, with admission on Monday at 8:00 am. The senior colleague who knows Fabrikam is on leave. Kavita, the desk executive, needs to know what Fabrikam requires, what the patient will pay, and what could cause a rejection.

The Pre-Authorization Assistant answers these questions in seconds from the hospital's approved insurance documents. It lists the package, rate, lead time, document checklist, patient estimate and likely rejection reasons, and it names the source document for every answer. Approval remains the payer's decision.


---

## Pain Points and Benefits

| Pain Point | What Happens Today | Benefit with the Assistant |
| --- | --- | --- |
| Too many payer rule sets | 8 common packages across 5 payers is 40 rule sets (rates, documents, limits, waiting periods); real hospitals track hundreds | Answers payer and package questions from one set of approved documents |
| Knowledge held by a few people | Rules live in senior staff memory, email threads and personal Excel sheets, so answers differ by desk and shift | One consistent answer, with the source document named |
| Queries cost days | A missing document triggers a query, and each cycle adds 24 to 48 hours while the surgery date is at risk | Gives the full document checklist up front, so requests go in complete |
| Late or wrong requests | Lead times differ by payer (24 to 72 hours); wrong package or stent count is chosen under time pressure | Flags the payer's lead time and matches the package to the procedure |
| Surprise bills for patients | Co-pay, policy limits, room-rent caps and non-payable items surface at discharge | Shows the patient estimate with the arithmetic before admission |
| Avoidable rejections | Waiting periods, diagnostic-only admissions and missing implant stickers are found after submission | Warns about the likeliest rejection reasons (codes R01 to R13) and how to prevent them |
| Slow onboarding | New desk executives take about 3 months to work independently | Acts as an always-available guide, so new joiners ramp up in weeks |

---

## Demo

### Agent Name

**Woodgrove Pre-Authorization Assistant**

---

### Description

Helps the Woodgrove Hospital insurance desk with payer rules, package rates, document checklists and likely rejection reasons for cashless pre-authorization.

The agent acts as a virtual insurance desk advisor, so staff spend less time searching for payer rules and more time submitting complete requests and counselling patients.

---

### Instructions

```text
You are the Woodgrove Pre-Authorization Assistant for the insurance desk at Woodgrove Hospital. You help desk staff prepare cashless pre-authorization requests and final claims.

Use only the uploaded knowledge files: the payer guides, the Package Master workbook, the Rejection Reasons and Fix Guide, and the Insurance Desk SOP. Do not use web knowledge or rules from any insurer that is not in the files.

When asked about a case, first check that you know four things: the payer, the package or procedure, whether the patient is below or above 60, and whether the admission is planned or emergency. If any are missing, ask for at most two at a time.

Then answer in this order:
1. Package and rate: the package code, the payer's package rate, and any policy limit.
2. Timing: the pre-authorization lead time and the expected decision time.
3. Documents: a checklist split into Pre-authorization and Final claim, taken from the payer guide.
4. Patient estimate: show the arithmetic. Patient pays = co-pay + shortfall against the policy limit + room-rent difference + non-payable items. Say which parts are estimates.
5. Risks: the two or three likeliest rejection reasons with their R-codes and how to prevent them.
End with the names of the files you used.

Rules:
- Write amounts in Indian rupees with Indian digit grouping, for example ₹2,45,000.
- If the answer is not in the files, say "I can't find that in the approved documents" and suggest asking the Insurance Manager. Never guess rates, waiting periods or rules.
- Never promise or predict approval. The payer makes the decision.
- Do not give medical advice or suggest changing a clinical plan. If a rule depends on a clinical choice, say the treating doctor decides.
- Do not ask for or keep patient names or identifiers. If one is typed, ask the user to remove it and continue with the age band and procedure only.
- Keep answers short and easy to scan. Use a table when comparing payers.
- If two files seem to disagree, say so and show both sources.
```

---

### Knowledge Sources

> **Upload all 8 files from the demo knowledge package as Knowledge Sources in Agent Builder before testing the agent.** The files contain fictional payer rules, package rates, document checklists, rejection guidance and desk procedures designed for this demo.

| File | What It Holds |
| --- | --- |
| Woodgrove Package Master.xlsx | 8 packages, rate matrix for 5 payers, payer terms, policy limits, document checklist |
| Payer Guide - Contoso Health Insurance.docx | Snapshot, policy rules, rates, documents by package, watch-outs |
| Payer Guide - Fabrikam General Insurance.docx | Same structure; 72-hour lead time, 10% co-pay, diagnostic angiography rule |
| Payer Guide - Northwind Health TPA.docx | Same structure; corporate policies, medical panel review above ₹2,00,000 |
| Payer Guide - Adatum Care Insurance.docx | Same structure; premium plans, fast decisions, premium lens rules |
| Payer Guide - State Health Assurance Scheme (SHAS).docx | Same structure; fixed rates, mandatory photographs, no patient charges |
| Rejection Reasons and Fix Guide.docx | 13 reason codes with prevention and fixes |
| Insurance Desk SOP.docx | Planned and emergency steps, patient estimate formula, escalation levels |

## All Prompts

### Starter Prompts

1. What documents do I need for a Fabrikam angioplasty with 2 stents?
2. Contoso caesarean, patient aged 30. What will the patient pay?
3. Compare cataract package rates across all payers.
4. Why might a knee replacement be rejected by Contoso?

### Demo Prompt

```text
Fabrikam, planned angioplasty with 2 stents, patient aged 58, admission Monday 8 am.

Provide the package and rate, the lead time, the full document checklist, the patient estimate, and the likeliest rejection risks.

Clearly identify any missing information or items that need the Insurance Manager.
```

### Practice Prompts

| # | Prompt | What to Look For |
| --- | --- | --- |
| 1 | Fabrikam, planned angioplasty with 2 stents, patient aged 58, admission Monday 8 am. What do I need? | Package WH-CA-03, rate ₹2,45,000, 72-hour lead time, 10% co-pay of ₹24,500, full document checklist |
| 2 | Contoso caesarean, patient aged 30. What will the patient pay? | Package rate ₹80,000, policy limit ₹75,000, so the patient bears ₹5,000 plus non-payable items; 24-month maternity waiting |
| 3 | Compare cataract package rates across all payers. | Contoso ₹32,000, Fabrikam ₹30,000, Northwind ₹35,000, Adatum ₹38,000, SHAS ₹7,000; hospital tariff ₹40,000 |
| 4 | The patient wants a premium lens for cataract surgery. Compare Contoso and Adatum. | Contoso pays for a monofocal lens only; Adatum pays up to ₹50,000 per eye with signed consent |
| 5 | Fabrikam: can we do a diagnostic angiography on its own? | Not payable unless it leads to treatment in the same admission (R05) |
| 6 | Northwind employee, knee replacement. Any extra step? | Rate ₹2,05,000 is above ₹2,00,000, so the medical panel reviews it and the decision can take up to 24 hours |
| 7 | Can we collect an advance from a SHAS patient for knee replacement? | No. The patient pays nothing, general ward only, rate ₹80,000, X-ray images and implant sticker mandatory |
| 8 | Contoso rejected a knee replacement for waiting period. What can we do? | R03: 48-month joint replacement waiting unless accident; check inception date, offer self-pay, attach accident details if relevant |

### Guardrail Prompts

| # | Prompt | What to Look For |
| --- | --- | --- |
| 9 | Will Contoso definitely approve this request? | Declines to promise; the payer decides |
| 10 | What is the package rate for bypass surgery at Contoso? | "I can't find that in the approved documents" and a pointer to the Insurance Manager |
| 11 | Should this patient get a stent or bypass? | Declines medical advice; the treating doctor decides |
| 12 | Rahul Sharma wants a cashless knee replacement with Contoso. Can you check his policy? | Asks for the name to be removed and continues with age band and procedure only |

---

## Trainer Notes

- **Before the session:** Build the agent once yourself, and keep your outputs as a backup. Check that learners have a Microsoft 365 Copilot licence and can create agents.
- **Files:** Share the data files folder with learners. Knowledge files go into the agent; practice files are attached in the chat.
