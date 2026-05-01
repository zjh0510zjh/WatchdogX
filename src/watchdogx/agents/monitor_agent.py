"""Monitor Agent"""
from watchdogx.core.agent import BaseAgent
class MonitorAgent(BaseAgent):
    async def run(self, context):
        return {"status": "collected", "metrics": {}, "alerts": []}
