from sqlmodel import Session
from app.model import Task, TaskEdit, TaskRead

class TaskService:
    def __init__(self, session:Session) -> None:
        self.session = session

    def create_task(self, input:TaskEdit) -> TaskRead:
        task = Task(**dict(input))
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return TaskRead(**dict(task))

    def get_task(self, task_id:int) -> TaskRead | None:
        task = self.session.get(Task, task_id)
        if task:
            return TaskRead(**dict(task))
        return None

    def update_task(self, id:int, edit:TaskEdit) -> TaskRead | None:
        task = self.session.get(Task, id)
        if task:
            for key, value in dict(edit).items():
                setattr(task, key, value)
            self.session.commit()
            return TaskRead(**dict(task))
        return None

    def delete_task(self, id:int) -> bool:
        task = self.session.get(Task, id)
        if task:
            self.session.delete(task)
            self.session.commit()
            return True
        return False