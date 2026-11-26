# Insurance Claims Assistant

## Scenario

A Claims Adjuster at an insurance company is reviewing a newly lodged home insurance claim. To move the claim forward confidently, the adjuster needs to understand what happened, what the policy covers, which exclusions or excess apply, what evidence has been received, what is still missing, and what the claimant should be told next.

However, this information is spread across policy wordings, claim files, assessor reports, photos, correspondence, and claims handling guidelines.

The Insurance Claims Assistant acts as an AI-powered claims support advisor that brings together the relevant claim and policy information and prepares the adjuster for the next step in seconds.

## Pain Points

### Document-Heavy Claim Review

Adjusters spend significant time reading policy wordings, claim forms, assessor reports, and correspondence before they can act on a claim.

Important details can be missed when evidence is spread across many documents.

### Slow Coverage Validation

Checking a claim against coverage, exclusions, limits, and excess requires cross-referencing long policy documents.

Interpretation can vary between adjusters, leading to inconsistent outcomes.

### Missing Evidence and Rework

Claims often stall because required evidence (quotes, photos, reports, proof of ownership) has not been requested or received.

Repeated follow-up requests frustrate claimants and extend cycle times.

### Inconsistent Customer Communication

Claimants are often anxious after a loss and want clear, timely updates.

Status updates vary in tone, accuracy, and clarity depending on the adjuster's workload and experience.

### Limited Time for Complex Claims

Adjusters spend more time assembling information than applying judgment to complex, high-severity, or potentially fraudulent claims.

## Benefits

### Faster Claim Triage

Reduces claim review time from hours to minutes.

Provides a ready-to-use claim summary for the adjuster.

### Consistent Coverage Checks

Retrieves the relevant policy sections, limits, exclusions, and excess for each claim.

Cites the policy wording so the adjuster can verify every point.

### Fewer Delays from Missing Evidence

Identifies outstanding evidence against the claims handling checklist.

Drafts clear evidence requests to the claimant in one step.

### Improved Claimant Experience

Enables clear, empathetic, and accurate status updates.

Helps adjusters set realistic expectations for next steps and timeframes.

### Better Risk Awareness

Highlights potential fraud indicators, inconsistencies, and items requiring specialist or senior review.

Keeps coverage and settlement decisions with the accountable human adjuster.

### Higher Productivity

Allows adjusters to focus on assessment, judgment, and customer care rather than document searching.

## Demo

### Agent Name

Insurance Claims Assistant

### Description

The Insurance Claims Assistant helps claims adjusters review insurance claims by consolidating claim details, policy coverage, exclusions, excess, evidence received, outstanding requirements, and risk indicators into a single, easy-to-consume claim summary.

The agent acts as a virtual claims support advisor, enabling adjusters to spend less time searching documents and more time applying judgment and supporting claimants.

### Instructions

You are an Insurance Claims Assistant for a general insurance company. Your role is to help claims adjusters review claims by providing concise, accurate, and evidence-based claim insights.

When responding:

- Summarise the claim, including the claimant, policy number, date and cause of loss, and items claimed.
- Check the claim against the policy wording, highlighting relevant coverage, limits, exclusions, and the applicable excess.
- Always cite the policy section or document that supports each coverage point.
- List evidence received and evidence still outstanding, based on the claims handling guide.
- Identify potential risks, inconsistencies, or fraud indicators that need adjuster or specialist review.
- Suggest next steps for the adjuster in line with the claims handling guide.
- Draft claimant communications in a clear, empathetic, and plain-language tone when asked.
- Present information in a structured claim summary format.
- Be factual and use only information available from approved enterprise sources.
- Do not make final coverage, liability, or settlement decisions on behalf of the insurer; flag these for the adjuster's decision.
- If information is unavailable, clearly state what data is missing.

### Starter Prompts

#### Claim Summary

Summarise claim CLM-1042 for me.

#### Coverage Check

Check claim CLM-1042 against the policy wording. What is covered, what exclusions might apply, and what is the excess?

#### Missing Evidence

What evidence is still outstanding for claim CLM-1042, and can you draft a request to the claimant?

#### Risk Review

Are there any inconsistencies, fraud indicators, or items needing senior review on claim CLM-1042?

## Knowledge Sources

Download the demo knowledge source package from:

`industry/FSI/Agent Builder/data files/Insurance Claims Agent Demo Pack.zip`

Upload all files from this package as Knowledge Sources in Agent Builder before testing the agent.

The package contains a fictional home and contents policy wording, product disclosure summary, claim files, assessor reports, claimant correspondence, a claims handling guide, and communication templates specifically designed for the Insurance Claims Assistant demo.

## Demo Prompt

Once the knowledge sources are uploaded, try the following prompt:

```text
Review claim CLM-1042 for me. Provide a claim summary, the relevant policy coverage with citations, any exclusions or limits that may apply, the applicable excess, evidence received and outstanding, potential risks or inconsistencies, recommended next steps, and a draft status update to the claimant. Clearly identify any missing information or items requiring adjuster or specialist decision.
```