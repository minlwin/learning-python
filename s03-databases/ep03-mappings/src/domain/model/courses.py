from sqlalchemy import Column, Integer, String
from src.domain.db import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    hourse = Column(Integer, nullable=False)
