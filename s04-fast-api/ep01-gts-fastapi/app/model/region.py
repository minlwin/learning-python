from sqlmodel import Field, SQLModel


class Region(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, index=True)
    region: str = Field(nullable=False)
