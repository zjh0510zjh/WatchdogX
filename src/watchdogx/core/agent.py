"""Base Agent class for multi-agent collaboration."""

import logging
from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
from watchdogx.core.memory import MemoryStore

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
    """Abstract base class for all WatchdogX agents.
    
    Each agent can access the shared memory store for historical case retrieval
    and tool registry for executing actions.
    """

    def __init__(
        self,
        name: str,
        memory: Optional[MemoryStore] = None,
        config: Optional[Dict[str, Any]] = None,
    ):
        self.name = name
        self.memory = memory
        self.config = config or {}
        logger.info(f"[{self.name}] Agent initialized")

    @abstractmethod
    async def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the agent's main logic.
        
        Args:
            context: Input context containing alert info, logs, metrics, etc.
            
        Returns:
            Result dict with status and output data
        """
        ...

    async def retrieve_similar_cases(self, query: str, top_k: int = 5) -> list:
        """Query the memory store for similar historical incidents."""
        if not self.memory:
            return []
        return self.memory.search(query, top_k=top_k)

    def __repr__(self):
        return f"<{self.__class__.__name__}(name={self.name})>"
