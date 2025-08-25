from pydantic import ValidationError
import pytest
from src import Task


def test_create_task():
    task = Task(
        id=1,
        title="Test Task",
        description="This is a test task",
        completed=False
    )
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "This is a test task"
    assert task.completed is False

    dump = task.model_dump()
    assert dump == {
        "id": 1,
        "title": "Test Task",
        "description": "This is a test task",
        "completed": False
    }

@pytest.mark.parametrize("data", [
    {"id": "A", "title": "Title", "description" : "Description", "completed" : "True"},
    {"id": "1", "title": "", "description" : "Description", "completed" : "True"},
    {"id": "2", "title": "Title", "description" : "Description", "completed" : "Yes"},
])
def test_task_validation(data):
    with pytest.raises(ValidationError):
        Task(**data)