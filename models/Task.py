from typing import Optional
from datetime import datetime
from .Base import Base

class Task(Base):
    task_id: str
    title: str
    description: Optional[str]
    due_date: Optional[datetime]
    completed: bool = False
    reward: int
