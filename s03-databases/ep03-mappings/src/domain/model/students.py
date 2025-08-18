from __future__ import annotations
from typing import TYPE_CHECKING

from src.domain.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from src.domain.model.regostration import Registration

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int]         = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]       = mapped_column(nullable=False)
    email: Mapped[str]      = mapped_column(nullable=False)
    
    registrations: Mapped[list[Registration]] = relationship(back_populates="student")
