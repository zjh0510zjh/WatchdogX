"""Shell executor tool"""
import subprocess
from watchdogx.core.tools import BaseTool
class ShellExecutor(BaseTool):
    def __init__(self): super().__init__("shell_executor", "Execute shell commands")
    async def execute(self, **kwargs):
        cmd = kwargs.get("command", "")
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        return {"stdout": r.stdout, "returncode": r.returncode}
