from src.logic.models.base import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import String,Integer,DateTime,Text,Enum,ForeignKey
from datetime import datetime
import enum
class TaskStatus(str,enum.Enum):
        ACTIVE = "ACTIVE",
        IN_PROGRESS= "IN PROGRESS",
        ENDED= "ENDED",
        DECLINED= "DECLINED"
        DELETED= "DELETED"

class Task(Base):
    id: Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    title: Mapped[str] = mapped_column(String(200),nullable=False)
    description: Mapped[str] = mapped_column(Text,nullable=True)
    status: Mapped[TaskStatus] = mapped_column(Enum(TaskStatus))
    created_at: Mapped[datetime] = mapped_column(DateTime,default=datetime.now(),nullable=False)
