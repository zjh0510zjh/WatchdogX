"""Diagnosis Agent"""
from watchdogx.core.agent import BaseAgent
class DiagnosisAgent(BaseAgent):
    async def run(self, context):
        alert = context.get("alert", {})
        similar = await self.retrieve_similar_cases(str(alert))
        return {"status": "diagnosed", "root_cause": "", "similar_cases": len(similar)}
