
from langsmith import traceable

@traceable(name="agent_pipeline")
def trace_pipeline(data):
    return data
