from pydantic import BaseModel
from src.logic.models.task import TaskStatus
from datetime import datetime
class TaskResponse(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    status: TaskStatus
    created_at: datetime

class TaskCreate(BaseModel):
    user_id: int
    title: str
    description: str
    status: TaskStatus