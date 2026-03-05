
from autogen import AssistantAgent
from config.llm_config import llm_config

tool_executor = AssistantAgent(
    name="Tool_Executor",
    system_message="""You execute enterprise tools and APIs using FastAPI services.
Call appropriate endpoints and return structured results.""",
    llm_config=llm_config
)
