from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Task:
    """
    Represents a single todo item.
    """
    id: int
    title: str
    description: str
    created_at: datetime
    completed: bool = False
    completed_at: Optional[datetime] = None
