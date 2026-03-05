
from autogen import AssistantAgent
from config.llm_config import llm_config

validator = AssistantAgent(
    name="Validator",
    system_message="""You are an independent AI output validator.
Check if every claim is supported by retrieved evidence.
Ensure compliance with business rules.
Return JSON: {verdict: PASS|FAIL|NEEDS_REVIEW, confidence: 0-1}""",
    llm_config=llm_config
)
