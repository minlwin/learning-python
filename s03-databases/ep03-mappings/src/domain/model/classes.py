from __future__ import annotations
from datetime import date
from typing import TYPE_CHECKING

from src.domain.db import Base
from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

if TYPE_CHECKING:
    from src.domain.model.courses import Course

class Class(Base):
    __tablename__ = "classes"

    id:Mapped[int]          = mapped_column(primary_key=True, autoincrement=True)
    start_at:Mapped[date]   = mapped_column(Date, nullable=False)
    months:Mapped[int]      = mapped_column(nullable=False)
    course_id:Mapped[int]   = mapped_column(ForeignKey("courses.id"), nullable=False)

    course:Mapped[Course]   = relationship(back_populates="classes")
