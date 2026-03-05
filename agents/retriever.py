
from autogen import AssistantAgent
from config.llm_config import llm_config

retriever_agent = AssistantAgent(
    name="Retriever",
    system_message="""You retrieve relevant enterprise data from vector databases.
Use pgvector similarity search and return relevant context snippets.""",
    llm_config=llm_config
)
