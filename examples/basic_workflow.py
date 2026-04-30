"""Basic example demonstrating WatchdogX multi-agent workflow."""

import asyncio
from watchdogx import Orchestrator, MemoryStore
from watchdogx.core.agent import BaseAgent


# Custom agents inheriting from BaseAgent
class SimpleMonitorAgent(BaseAgent):
    async def run(self, context):
        print(f"[{self.name}] Checking metrics...")
        context["anomaly_detected"] = True
        context["alert"] = {
            "service": "api-gateway",
            "metric": "p99_latency",
            "value": 2500,
            "threshold": 2000,
        }
        return {"status": "alert", "data": context["alert"]}


class SimpleDiagnosisAgent(BaseAgent):
    async def run(self, context):
        alert = context.get("alert", {})
        print(f"[{self.name}] Analyzing alert: {alert}")

        similar = await self.retrieve_similar_cases(
            f"{alert.get('service')} {alert.get('metric')} high"
        )
        return {
            "status": "diagnosed",
            "root_cause": "Memory leak in connection pool",
            "similar_cases": len(similar),
        }


class SimpleExecutorAgent(BaseAgent):
    async def run(self, context):
        diagnosis = context.get("diagnosis", {})
        print(f"[{self.name}] Executing fix for: {diagnosis.get('root_cause')}")
        return {"status": "fixed", "action": "restart_api_gateway"}


class SimpleVerifyAgent(BaseAgent):
    async def run(self, context):
        print(f"[{self.name}] Verifying health...")
        return {"status": "healthy", "checks_passed": True}


async def main():
    memory = MemoryStore(storage_path="./example_memory")
    memory.add({
        "title": "API Gateway latency spike",
        "symptoms": ["high p99 latency", "connection timeout"],
        "root_cause": "Connection pool exhaustion",
        "fix": "Increased connection pool size and restarted gateway",
    })

    monitor = SimpleMonitorAgent("monitor", memory=memory)
    diagnosis = SimpleDiagnosisAgent("diagnosis", memory=memory)
    executor = SimpleExecutorAgent("executor")
    verify = SimpleVerifyAgent("verify")

    context = {}
    result = await monitor.run(context)
    print(f"Monitor result: {result}")

    context["diagnosis"] = await diagnosis.run(context)
    print(f"Diagnosis result: {context['diagnosis']}")

    context["execution"] = await executor.run(context)
    print(f"Executor result: {context['execution']}")

    context["verification"] = await verify.run(context)
    print(f"Verify result: {context['verification']}")

    print("\n[Workflow] Self-healing complete!")


if __name__ == "__main__":
    asyncio.run(main())
