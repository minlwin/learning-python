from typing import Any
from src.domain.db import SessionLocal
from src.domain.model.students import Student

class StudentDao:
    def __init__(self) -> None:
        self.session = SessionLocal()

    def create(self, student: Student) -> Student:
        self.session.add(student)
        self.session.commit()
        self.session.refresh(student)
        return student
    
    def find_one(self, student_id: int) -> Student | None:
        return self.session.get(Student, student_id)
    
    def search(self, params:dict[str, Any]) -> list[Student]:
        query = self.session.query(Student)
        for key, value in params.items():
            query = query.filter(getattr(Student, key) == value)
        return query.all()
    
    def update(self, student:Student) -> Student:
        self.session.merge(student)
        self.session.commit()
        return student
    
    def delete(self, student_id:int) -> bool:
        student = self.find_one(student_id)
        if student:
            self.session.delete(student)  
            self.session.commit()
            return True
        return False