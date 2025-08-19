from sqlmodel import Relationship, SQLModel, Field

from app.model.region import Region

class Township(SQLModel, table= True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, index=True)
    region_id: int = Field(foreign_key="region.id", nullable=False)

    region: Region = Relationship()
