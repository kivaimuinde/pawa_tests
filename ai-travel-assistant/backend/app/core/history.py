# app/core/history.py

from typing import List, Dict
from app.models.schemas import QueryHistoryItem

# In-memory storage: {session_id: [history items]}
query_history: Dict[str, List[QueryHistoryItem]] = {}

def save_to_history(session_id: str, question: str, answer: str):
    item = QueryHistoryItem(question=question, answer=answer)
    query_history.setdefault(session_id, []).append(item)

def get_history(session_id: str) -> List[QueryHistoryItem]:
    return query_history.get(session_id, [])
