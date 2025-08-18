from typing import Any
from src.domain.db import SessionLocal
from src.domain.model.classes import Class


class ClassDao:
    def __init__(self) -> None:
        self.session = SessionLocal()

    def create(self, class_: Class) -> Class:
        self.session.add(class_)
        self.session.commit()
        self.session.refresh(class_)
        return class_

    def find_one(self, class_id: int) -> Class | None:
        return self.session.get(Class, class_id)

    def search(self, params: dict[str, Any]) -> list[Class]:
        query = self.session.query(Class)
        for key, value in params.items():
            query = query.filter(getattr(Class, key) == value)
        return query.all()

    def update(self, class_: Class) -> Class:
        self.session.merge(class_)
        self.session.commit()
        return class_

    def delete(self, class_id: int) -> bool:
        class_ = self.session.get(Class, class_id)
        if class_:
            self.session.delete(class_)
            self.session.commit()
            return True
        return False
