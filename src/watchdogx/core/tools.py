"""Tool registry and base tool for WatchdogX agents."""

import logging
from typing import Callable, Dict, Any, Optional

logger = logging.getLogger(__name__)


class BaseTool:
    """Base class for all tools that agents can invoke."""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    async def execute(self, **kwargs) -> Any:
        """Execute the tool with given parameters."""
        raise NotImplementedError


class ToolRegistry:
    """Central registry for agent-accessible tools."""

    _instance: Optional["ToolRegistry"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._tools = {}
        return cls._instance

    def register(self, tool: BaseTool):
        """Register a tool."""
        self._tools[tool.name] = tool
        logger.info(f"[ToolRegistry] Registered tool: {tool.name}")

    def get(self, name: str) -> Optional[BaseTool]:
        """Get a tool by name."""
        return self._tools.get(name)

    def list_tools(self) -> Dict[str, str]:
        """List all registered tools with descriptions."""
        return {name: tool.description for name, tool in self._tools.items()}

    def get_tool_definitions(self) -> list:
        """Get tool definitions for LLM function calling."""
        return [
            {"name": t.name, "description": t.description}
            for t in self._tools.values()
        ]
