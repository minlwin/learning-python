from typing import Any
from src.domain.db import SessionLocal
from src.domain.model.courses import Course


class CourseDao:
    def __init__(self):
        self.session = SessionLocal()

    def create(self, course: Course) -> Course:
        self.session.add(course)
        self.session.commit()
        self.session.refresh(course)
        return course

    def find_one(self, course_id: int) -> Course | None:
        return self.session.get(Course, course_id)

    def search(self, params: dict[str, Any]) -> list[Course]:
        query = self.session.query(Course)
        for key, value in params.items():
            query = query.filter(getattr(Course, key) == value)
        return query.all()

    def update(self, course: Course) -> Course:
        self.session.merge(course)
        self.session.commit()
        return course

    def delete(self, course_id: int) -> bool:
        course = self.session.get(Course, course_id)
        if course:
            self.session.delete(course)
            self.session.commit()
            return True
        return False
