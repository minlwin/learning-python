from typing import Optional
from sqlmodel import Relationship, SQLModel, Field
from sqlalchemy.orm import QueryableAttribute

from src.model.entity.region import Region

class Township(SQLModel, table = True):
    id: Optional[int] = Field(primary_key=True, default=None)
    name: str
    region_id: int = Field(
        foreign_key="region.id", 
        nullable=False
    )
    region: Region = Relationship()