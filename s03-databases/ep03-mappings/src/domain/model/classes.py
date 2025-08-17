from src.domain.db import Base
from sqlalchemy import Column, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    course = relationship("Course", back_populates="classes")
    start_at = Column(Date, nullable=False)
    months = Column(Integer, nullable=False)
