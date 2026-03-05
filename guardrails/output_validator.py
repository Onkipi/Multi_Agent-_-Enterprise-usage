
from pydantic import BaseModel, validator
from typing import Literal, List

class AgentOutput(BaseModel):
    verdict: Literal["PASS","FAIL","NEEDS_REVIEW"]
    confidence: float
    answer: str
    sources: List[str]
    unsupported_claims: List[str] = []

    @validator("confidence")
    def confidence_range(cls,v):
        assert 0 <= v <= 1
        return v

    @validator("answer")
    def non_empty(cls,v):
        assert len(v.strip()) > 10
        return v
