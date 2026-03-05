
from autogen import AssistantAgent
from config.llm_config import llm_config

graph_reasoner = AssistantAgent(
    name="Graph_Reasoner",
    system_message="""You are a Knowledge Graph reasoning specialist.
Use Neo4j to traverse relationships between entities.
Identify connection patterns, dependency chains, and anomalies.
Always explain your reasoning path through the graph.""",
    llm_config=llm_config
)
