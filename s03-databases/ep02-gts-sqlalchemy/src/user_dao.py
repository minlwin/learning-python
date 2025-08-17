from src.db import SessionLocal
from src.models import User

class UserDAO:
    def __init__(self):
        self.session = SessionLocal()

    def create_user(self, user:User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_user(self, user_id:int) -> User | None:
        return self.session.query(User).filter(User.id == user_id).first()

    def update_user(self, user) -> User:
        self.session.commit()
        self.session.refresh(user)
        return user

    def delete_user(self, user_id:int) -> bool:
        user = self.get_user(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False