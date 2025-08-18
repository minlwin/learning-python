from __future__ import annotations
from typing import TYPE_CHECKING

from src.domain.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from src.domain.model.classes import Class  

class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int]             = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]           = mapped_column(index=True)
    description: Mapped[str]    = mapped_column(nullable=True)
    hours: Mapped[int]          = mapped_column(nullable=False)

    classes: Mapped[list[Class]] = relationship(back_populates="course")