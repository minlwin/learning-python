from typing import Any
from src.domain.db import SessionLocal
from src.domain.model.regostration import Registration


class RegistrationDao:
    def __init__(self) -> None:
        self.session = SessionLocal()

    def create(self, registration: Registration) -> 'Registration':
        self.session.add(registration)
        self.session.commit()
        self.session.refresh(registration)
        return registration

    def find_one(self, registration_id: int) -> 'Registration | None':
        return self.session.get(Registration, registration_id)

    def search(self, params: dict[str, Any]) -> list[Registration]:
        query = self.session.query(Registration)
        for key, value in params.items():
            query = query.filter(getattr(Registration, key) == value)
        return query.all()

    def update(self, registration: Registration) -> 'Registration':
        self.session.merge(registration)
        self.session.commit()
        return registration

    def delete(self, registration_id: int) -> bool:
        registration = self.find_one(registration_id)
        if registration:
            self.session.delete(registration)
            self.session.commit()
            return True
        return False