### Multi-Agent Enterprise AI System
### 5-Agent Orchestration with Guardrails, Observability & Structured Validation

> Built by **Vijay Kashyab** | Based on production architecture deployed at a global enterprise
> Achieved **44% hallucination reduction** through inter-agent validation

---

## The Agent Team

```
┌─────────────────────────────────────────────────────────┐
│                    USER QUERY                           │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
           ┌─────────────────────────┐
           │     PLANNER AGENT       │  ← Decomposes goal into sub-tasks
           │     (GPT-4o)            │    Creates execution plan
           └────────────┬────────────┘
                        │
          ┌─────────────┼──────────────┐
          │             │              │
          ▼             ▼              ▼
  ┌──────────────┐ ┌──────────┐ ┌──────────────┐
  │  RETRIEVER   │ │  GRAPH   │ │    TOOL      │
  │   AGENT      │ │ REASONER │ │  EXECUTOR    │
  │ (pgvector)   │ │ (Neo4j)  │ │ (FastAPI     │
  │              │ │          │ │  tools)      │
  └──────┬───────┘ └────┬─────┘ └──────┬───────┘
         │              │              │
         └──────────────┼──────────────┘
                        │
                        ▼
           ┌─────────────────────────┐
           │    VALIDATOR AGENT      │  ← Independent verification
           │    (GPT-4o)             │    Checks faithfulness + compliance
           └────────────┬────────────┘
                        │
                        ▼
              STRUCTURED RESPONSE
              + AUDIT LOG ENTRY
```

---

## Quickstart

```bash
git clone https://github.com/Onkipi/multi-agent-enterprise
cd multi-agent-enterprise
pip install -r requirements.txt
cp .env.example .env

# Run the fraud detection demo
python examples/fraud_detection_demo.py

# Run the supply chain agent demo
python examples/supply_chain_demo.py

# Run the project management agent
python examples/pm_agent_demo.py
```

---

## Agent Definitions

```python
# agents/planner.py
planner = autogen.AssistantAgent(
    name="Planner",
    system_message="""You are a strategic AI planner.
    Break complex goals into specific sub-tasks.
    Assign each sub-task to the most capable agent.
    Always define success criteria before execution begins.
    Output a structured execution plan in JSON.""",
    llm_config={"config_list": config_list, "temperature": 0}
)

# agents/graph_reasoner.py
graph_reasoner = autogen.AssistantAgent(
    name="Graph_Reasoner",
    system_message="""You are a Knowledge Graph reasoning specialist.
    Use Neo4j to traverse relationships between entities.
    Identify connection patterns, dependency chains, and anomalies.
    Always explain your reasoning path through the graph.""",
    llm_config=llm_config
)

# agents/validator.py
validator = autogen.AssistantAgent(
    name="Validator",
    system_message="""You are an independent AI output validator.
    Check: (1) Is every claim supported by retrieved context?
    (2) Does the output comply with business rules?
    (3) Are there any hallucinated facts?
    Return: {"verdict": "PASS|FAIL", "issues": [], "confidence": 0.0-1.0}""",
    llm_config=llm_config
)
```

---

## Built-in Guardrails

```python
# guardrails/output_validator.py
from pydantic import BaseModel, validator
from typing import Literal

class AgentOutput(BaseModel):
    verdict: Literal["PASS", "FAIL", "NEEDS_REVIEW"]
    confidence: float
    answer: str
    sources: list[str]
    unsupported_claims: list[str] = []

    @validator("confidence")
    def confidence_range(cls, v):
        assert 0.0 <= v <= 1.0, "Confidence must be 0-1"
        return v

    @validator("answer")
    def no_empty_answer(cls, v):
        assert len(v.strip()) > 10, "Answer too short"
        return v
```

---

## Use Case Examples

### 🔍 Fraud Detection Agent Team
```python
# 5 agents collaborate to detect and explain fraud patterns
result = fraud_agent_team.run(
    task="""
    Transaction ID: TXN-847291
    Amount: $47,500 | Merchant: Electronics Hub | Time: 2:43 AM
    
    1. Check transaction patterns (Retriever Agent)
    2. Traverse account network for fraud rings (Graph Reasoner)
    3. Assess risk score (Decision Agent)
    4. Generate compliance report (Validator Agent)
    """
)
```

### 📦 Supply Chain Optimizer
```python
# Multi-agent demand forecasting + inventory optimization
result = supply_chain_team.run(
    task="Optimize inventory for SKU-4821 across 50 warehouses for Q4 peak demand"
)
```

### 📊 AI Project Manager
```python
# PM agent that monitors projects and escalates risks
result = pm_agent.run(
    task="Review all active AI projects. Flag At-Risk ones. Generate executive summary."
)
```

---

## Observability Integration

```python
# Every agent interaction is traced with LangSmith
from langsmith import traceable

@traceable(name="fraud_detection_pipeline")
def run_fraud_pipeline(transaction_data: dict) -> AgentOutput:
    # Full agent orchestration with automatic tracing
    ...
```

---

## Performance Benchmarks (Production)

| Metric | Value |
|---|---|
| End-to-end latency (p95) | 3.2 seconds |
| Hallucination rate | < 3% (inter-agent validation) |
| Task completion rate | 91% |
| Validator pass rate | 89% first-pass |
| Cost per complex query | ~$0.08 (GPT-4o routing) |

---

`Python 3.11` `AutoGen` `LangChain` `Neo4j` `pgvector` `LangSmith` `FastAPI` `Pydantic`
