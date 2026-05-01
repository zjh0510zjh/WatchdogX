# Agent Development Guide

```python
from watchdogx.core.agent import BaseAgent
class MyAgent(BaseAgent):
    async def run(self, ctx):
        return {"status": "ok"}
```
