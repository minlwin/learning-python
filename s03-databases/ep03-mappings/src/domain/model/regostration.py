from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from src.domain.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from src.domain.model.students import Student
    from src.domain.model.classes import Class

class Registration(Base):
    __tablename__ = "registrations"

    id: Mapped[int]             = mapped_column(primary_key=True, autoincrement=True)
    student_id: Mapped[int]     = mapped_column(ForeignKey("students.id"), nullable=False)
    class_id: Mapped[int]       = mapped_column(ForeignKey("classes.id"), nullable=False)

    student: Mapped[Student]    = relationship("Student", back_populates="registrations")
    class_: Mapped[Class]       = relationship("Class")