# app/core/llm_client.py
import httpx
from app.core.config import settings

async def query_gemini(prompt: str) -> str:
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=f"{settings.GEMINI_API_URL}?key={settings.GEMINI_API_KEY}",
            headers=headers,
            json=payload
        )
        
        if response.status_code != 200:
            print("🚨 Gemini error:", response.text)
            return "❌ Gemini API error: check logs"

        data = response.json()
        try:
            return data['candidates'][0]['content']['parts'][0]['text']
        except (KeyError, IndexError):
            return "⚠️ Gemini returned an unexpected response format."
