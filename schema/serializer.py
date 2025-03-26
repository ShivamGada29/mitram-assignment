from pydantic import BaseModel

from models.status import StatusEnum

from datetime import datetime
from typing import Optional
from uuid import UUID

class TaskId(BaseModel):
    id: UUID

class TaskBase(BaseModel):
    title: str
    status: StatusEnum = StatusEnum.PENDING

class TaskCreate(TaskBase):
    pass

class TaskSerializer(TaskBase, TaskId):
    created_at: datetime

    class Config:
        from_orm = True

class TaskUpdate(TaskId):
    title: str