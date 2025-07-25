# app/utils/gemini.py

from app.core.config import settings
import httpx


GEMINI_API_URL = (
    f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    f"?key={settings.GEMINI_API_KEY}"
)


async def query_gemini(prompt: str) -> str:
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(GEMINI_API_URL, json=payload)
        response.raise_for_status()
        data = response.json()

        return data["candidates"][0]["content"]["parts"][0]["text"]
