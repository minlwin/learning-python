from asyncio import Task
from unittest.mock import Mock

import pytest
from sqlmodel import Session

from app.model.task import TaskEdit
from app.service.task_service import TaskService


class TestTaskService:

    @pytest.fixture
    def mock_session(self) -> Session:
        return Mock(spec=Session)

    @pytest.fixture
    def task_service(self, mock_session) -> TaskService:
        return TaskService(mock_session)

    def test_create_task(self, task_service: TaskService, mock_session: Session):
        # Arrange
        task_data = TaskEdit(title="Test Task", description="This is a test task.")
        
        # Act
        task = task_service.create_task(task_data)
        
        # Assert
        assert task.title == "Test Task"
        assert task.description == "This is a test task."
        mock_session.add.assert_called_once_with(task)
        mock_session.commit.assert_called_once()
        mock_session.refresh.assert_called_once_with(task)