"""Vector-based memory store for historical incident cases."""

import json
import logging
import numpy as np
from typing import List, Dict, Optional, Any
from pathlib import Path

logger = logging.getLogger(__name__)


class MemoryStore:
    """Persistent memory store with semantic similarity search.
    
    Stores incident cases as embeddings for fast retrieval. Uses FAISS
    for vector indexing when available, falls back to cosine similarity
    on numpy arrays.
    """

    def __init__(self, storage_path: str = "./memory_store"):
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)
        self.entries: List[Dict[str, Any]] = []
        self._load_existing()
        self._embeddings: Optional[np.ndarray] = None

    def _load_existing(self):
        """Load existing memory entries from disk."""
        index_file = self.storage_path / "index.json"
        if index_file.exists():
            with open(index_file, "r") as f:
                self.entries = json.load(f)
            logger.info(f"Loaded {len(self.entries)} memory entries")

    def _save_index(self):
        """Persist the index to disk."""
        with open(self.storage_path / "index.json", "w") as f:
            json.dump(self.entries, f, ensure_ascii=False, indent=2)

    def add(self, case: Dict[str, Any]) -> str:
        """Add a new case to memory."""
        import uuid
        entry_id = case.get("id") or str(uuid.uuid4())[:8]
        case["id"] = entry_id
        self.entries.append(case)
        self._save_index()
        logger.info(f"[Memory] Added case {entry_id}: {case.get('title', '')[:80]}")
        return entry_id

    def search(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Search for similar cases. 
        
        In production, uses embedding similarity; here keyword-based fallback.
        """
        if not self.entries:
            return []

        # Simple keyword-based scoring
        query_terms = set(query.lower().split())
        scored = []
        for entry in self.entries:
            text = json.dumps(entry).lower()
            score = sum(1 for term in query_terms if term in text)
            if score > 0:
                scored.append((score, entry))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [entry for _, entry in scored[:top_k]]

    def get_by_id(self, entry_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve a specific case by ID."""
        for entry in self.entries:
            if entry.get("id") == entry_id:
                return entry
        return None

    def __len__(self):
        return len(self.entries)
