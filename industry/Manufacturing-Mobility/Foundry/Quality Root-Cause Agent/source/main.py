import asyncio
import os
import sys
from pathlib import Path
from urllib.parse import urlsplit

from agent_framework.foundry import FoundryChatClient
from azure.identity.aio import AzureCliCredential
from dotenv import load_dotenv

from agents.data_analysis_agent import analyze_data
from agents.knowledge_agent import read_reports
from workflow import investigate


async def main() -> None:
    load_dotenv(Path(__file__).with_name(".env"))
    settings: dict[str, str] = {}
    for name in ("FOUNDRY_PROJECT_ENDPOINT", "FOUNDRY_MODEL"):
        value = os.environ.get(name, "").strip()
        if not value or "<" in value or ">" in value:
            raise ValueError(f"Set {name} to a real value; see .env.example.")
        settings[name] = value
    endpoint = urlsplit(settings["FOUNDRY_PROJECT_ENDPOINT"])
    if (endpoint.scheme != "https" or not endpoint.netloc
            or not endpoint.path.startswith("/api/projects/") or len(endpoint.path.strip("/").split("/")) != 3):
        raise ValueError("FOUNDRY_PROJECT_ENDPOINT must be an HTTPS Foundry project endpoint.")
    await analyze_data.invoke(skip_parsing=True)
    await read_reports.invoke(skip_parsing=True)
    print("Local inputs checked. Running DataAnalysisAgent -> KnowledgeAgent -> ReportAgent...", flush=True)
    async with AzureCliCredential() as credential:
        async with FoundryChatClient(
            project_endpoint=settings["FOUNDRY_PROJECT_ENDPOINT"], model=settings["FOUNDRY_MODEL"],
            credential=credential, timeout=120,
            function_invocation_configuration={"max_iterations": 4, "max_consecutive_errors_per_request": 1},
        ) as client:
            print(await investigate(client))

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    asyncio.run(main())
