
from orchestrator.orchestrator import MultiAgentOrchestrator

agent_system = MultiAgentOrchestrator()

task = """Transaction ID: TXN-847291
Amount: $47,500 | Merchant: Electronics Hub | Time: 2:43 AM
Check transaction patterns and detect possible fraud."""

result = agent_system.run(task)

print("RESULT:")
print(result)
