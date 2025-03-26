from sqlalchemy import Column, String, Enum, DateTime

from models.mysqldb import Base
from models.status import StatusEnum

from datetime import datetime, timezone
import uuid

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(String(255), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    title = Column(String(255), nullable=False)
    status = Column(Enum(StatusEnum), nullable=False, default=StatusEnum.PENDING)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))