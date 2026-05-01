"""LLM client wrapper"""
import logging
logger = logging.getLogger(__name__)

class LLMClient:
    def __init__(self, api_key, model="gpt-4"):
        self.api_key = api_key
        self.model = model
    async def chat(self, messages, **kwargs):
        from openai import AsyncOpenAI
        client = AsyncOpenAI(api_key=self.api_key)
        resp = await client.chat.completions.create(model=self.model, messages=messages, **kwargs)
        return resp.choices[0].message.content
    async def analyze(self, prompt, context=""):
        msgs = [
            {"role": "system", "content": "You are an SRE expert."},
            {"role": "user", "content": f"Context: {context}\nTask: {prompt}"}
        ]
        return await self.chat(msgs, temperature=0.1)
