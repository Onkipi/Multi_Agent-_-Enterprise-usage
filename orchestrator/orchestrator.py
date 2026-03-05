
from agents.planner import planner
from agents.retriever import retriever_agent
from agents.graph_reasoner import graph_reasoner
from agents.tool_executor import tool_executor
from agents.validator import validator

class MultiAgentOrchestrator:

    def __init__(self):
        self.planner = planner
        self.retriever = retriever_agent
        self.graph = graph_reasoner
        self.tools = tool_executor
        self.validator = validator

    def run(self, task:str):
        print("Planning...")
        plan = self.planner.generate_reply(messages=[{"role":"user","content":task}])

        print("Retrieving context...")
        retrieved = self.retriever.generate_reply(messages=[{"role":"user","content":task}])

        print("Graph reasoning...")
        graph = self.graph.generate_reply(messages=[{"role":"user","content":task}])

        print("Executing tools...")
        tools = self.tools.generate_reply(messages=[{"role":"user","content":task}])

        combined = f"""PLAN:{plan}
CONTEXT:{retrieved}
GRAPH:{graph}
TOOLS:{tools}"""

        print("Validating...")
        result = self.validator.generate_reply(messages=[{"role":"user","content":combined}])

        return result
