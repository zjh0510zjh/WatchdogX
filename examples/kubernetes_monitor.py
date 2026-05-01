"""K8s Monitor Example"""
from watchdogx.core.agent import BaseAgent

class K8sMonitorAgent(BaseAgent):
    async def run(self, context):
        return {"status": "scanned", "pods": 15}
