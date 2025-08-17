import pytest

from src.models import User
from src.user_dao import UserDAO
from src.db import engine, Base

@pytest.fixture(scope="function", autouse=True)
def user_dao():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield UserDAO()

def test_user_creation(user_dao):
    user = User(name="Aung Aung", age="20")
    created_user = user_dao.create_user(user)
    assert created_user.id is not None
    assert created_user.name == "Aung Aung"
    assert created_user.age == 20

def test_get_user_not_found(user_dao):
    user = user_dao.get_user(999)
    assert user is None

def test_get_user(user_dao):
    user = User(name="Aung Aung", age="20")
    created_user = user_dao.create_user(user)
    retrieved_user = user_dao.get_user(created_user.id)
    assert retrieved_user is not None
    assert retrieved_user.id == created_user.id
    assert retrieved_user.name == "Aung Aung"
    assert retrieved_user.age == 20

def test_update_user(user_dao):
    user = User(name="Aung Aung", age="20")
    created_user = user_dao.create_user(user)
    created_user.name = "Aung Aung Updated"
    created_user.age = 21
    updated_user = user_dao.update_user(created_user)
    assert updated_user.id == created_user.id
    assert updated_user.name == "Aung Aung Updated"
    assert updated_user.age == 21

def test_delete_user(user_dao):
    user = User(name="Aung Aung", age="20")
    created_user = user_dao.create_user(user)
    assert user_dao.delete_user(created_user.id) is True
    assert user_dao.get_user(created_user.id) is None