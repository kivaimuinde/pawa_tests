# app/api/v1/endpoints/query.py

from fastapi import APIRouter, HTTPException, Query
from app.models.schemas import QueryRequest, QueryResponse, QueryHistoryResponse
from app.core.llm_client import query_gemini
from app.utils.prompt_engineering import build_prompt
from app.core.history import save_to_history, get_history

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
async def handle_query(request: QueryRequest, session_id: str = Query("default")):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")

    prompt = build_prompt(request.question)

    try:
        print("🔍 Prompt sent to Gemini:\n", prompt)
        answer = await query_gemini(prompt)
        print("Gemini response:\n", answer)

        save_to_history(session_id=session_id, question=request.question, answer=answer)
        return QueryResponse(answer=answer)
    except Exception as e:
        print("ERROR:", str(e))
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/history", response_model=QueryHistoryResponse)
def fetch_history(session_id: str = Query("default")):
    history = get_history(session_id)
    return QueryHistoryResponse(history=history)
