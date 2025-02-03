import httpx
import os

async def get_ai_response(prompt: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            os.getenv("DEEPSEEK_ENDPOINT"),
            headers={"Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}"},
            json={
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": prompt}]
            }
        )
    return response.json()["choices"][0]["message"]["content"]
