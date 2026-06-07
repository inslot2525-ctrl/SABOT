from pydantic import BaseModel


class QueryRequest(BaseModel):
    query: str


class SourceItem(BaseModel):
    file: str
    snippet: str


class QueryResponse(BaseModel):
    intent: str
    answer: str
    confidence: int
    lead_capture: bool
    sources: list[SourceItem]