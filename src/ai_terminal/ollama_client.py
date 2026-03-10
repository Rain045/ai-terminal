import httpx
import json
from rich.console import Console

console = Console()

class OllamaClient:
    def __init__(self, base_url="http://localhost:11434", model="deepseek-coder:6.7b-instruct-q4_K_M"):
        self.base_url = base_url
        self.model = model

    async def generate_command(self, prompt, context=""):
        system_prompt = (
            "You are a specialized AI terminal assistant. "
            "Your goal is to translate natural language into precise shell commands. "
            "Only output the command itself, no explanation, no markdown backticks. "
            f"Current Context: {context}"
        )
        
        payload = {
            "model": self.model,
            "prompt": f"{system_prompt}\n\nUser Intent: {prompt}\nCommand:",
            "stream": False,
            "options": {
                "temperature": 0.1,
                "stop": ["\n"]
            }
        }

        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(f"{self.base_url}/api/generate", json=payload)
                response.raise_for_status()
                data = response.json()
                return data.get("response", "").strip()
        except Exception as e:
            return f"Error connecting to Ollama: {str(e)}"
