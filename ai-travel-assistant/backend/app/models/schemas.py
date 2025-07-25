# app/models/schemas.py

from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str

class QueryHistoryItem(BaseModel):
    question: str
    answer: str

class QueryHistoryResponse(BaseModel):
    history: List[QueryHistoryItem]
