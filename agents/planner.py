
from autogen import AssistantAgent
from config.llm_config import config_list

planner = AssistantAgent(
    name="Planner",
    system_message="""You are a strategic AI planner.
Break complex goals into specific sub-tasks.
Assign each sub-task to the most capable agent.
Always define success criteria before execution begins.
Output a structured execution plan in JSON.""",
    llm_config={"config_list": config_list, "temperature": 0}
)
