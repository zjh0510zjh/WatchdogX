"""Slack Integration Example"""
from watchdogx.core.agent import BaseAgent

class SlackNotifierAgent(BaseAgent):
    async def run(self, context):
        return {"status": "sent"}
