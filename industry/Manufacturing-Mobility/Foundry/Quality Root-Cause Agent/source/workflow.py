from agent_framework import AgentResponse
from agent_framework.foundry import FoundryChatClient
from agent_framework.orchestrations import SequentialBuilder

from agents import create_data_agent, create_knowledge_agent, create_report_agent

QUESTION = (
    "Why did fewer products pass their first inspection in W42 on Contoso Plant A Line 1 "
    "(Power Module), and what should we verify before choosing corrective action?"
)


async def investigate(client: FoundryChatClient) -> str:
    workflow = SequentialBuilder(participants=[
        create_data_agent(client), create_knowledge_agent(client), create_report_agent(client),
    ]).build()
    outputs = (await workflow.run(QUESTION)).get_outputs()
    if len(outputs) != 1 or not isinstance(outputs[0], AgentResponse) or not outputs[0].text.strip():
        raise RuntimeError("ReportAgent did not return a non-empty investigation report.")
    return outputs[0].text
