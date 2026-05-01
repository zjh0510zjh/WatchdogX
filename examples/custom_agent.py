"""Custom Agent Example"""
from watchdogx.core.agent import BaseAgent

class DatabaseMonitorAgent(BaseAgent):
    async def run(self, context):
        return {"status": "ok", "connections": 42}
