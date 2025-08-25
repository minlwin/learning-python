from datetime import date
from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    milestone: date
    start_at: date | None = None
    description: str | None = None
    completed: bool = False

class TaskEdit(BaseModel):
    title: str | None = None
    milestone: date | None = None
    start_at: date | None = None
    description: str | None = None
    completed: bool | None = None

class TaskRead(Task):
    pass