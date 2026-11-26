from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient


def create_report_agent(client: FoundryChatClient) -> Agent:
    return Agent(client, name="ReportAgent", instructions=(
        "Write a concise English investigation report for Contoso Plant A Line 1 / Power Module using only "
        "the preceding tool evidence and agent findings. If either is missing, explicitly report an incomplete "
        "investigation instead of inventing findings. Use these Markdown headings: Summary; Ranked hypotheses; "
        "Evidence gaps; Next checks; Decision boundary. Include the W40-W43 first-inspection pass rates. "
        "Under Ranked hypotheses, use a table: Rank | Hypothesis | Qualitative confidence | Evidence | Validation. "
        "Assess oven heating conditions, a material-batch contribution, and the new-operator explanation. "
        "Cite CSV filenames/columns and report filenames/sections. Explain W43 recovery with SP-002 still in use, "
        "the lack of high-defect W42 shifts for OP-04, and unbalanced observational comparisons. "
        "Separate historical evidence from current observations. Confidence labels are not calibrated probabilities. "
        "Current defect types, sensor calibration, full heating curves, and controlled material trials are missing. "
        "Recommend engineering-approved checks, not automatic production changes. Do not confirm a root cause "
        "or blame an operator. End: These are hypotheses; the Quality Engineer makes the final judgment."
    ))
