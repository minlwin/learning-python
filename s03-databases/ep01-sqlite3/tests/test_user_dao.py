import pytest

from src.database_manager import DatabaseManager
from src.user_dao import UserDao


@pytest.fixture
def user_dao():
    with DatabaseManager(":memory:") as db:
        dao = UserDao(db)
        yield dao

def test_add_user(user_dao):
    user_id = user_dao.add_user("Aung Aung", 20)
    assert user_id == 1
    user_id = user_dao.add_user("Thidar", 25)
    assert user_id == 2

def test_get_user_by_id(user_dao):
    user_dao.add_user("Aung Aung", 20)
    aung_aung = user_dao.get_user_by_id(1)
    assert aung_aung == {"id": 1, "name": "Aung Aung", "age" : 20}

    user_dao.add_user("Thidar", 25)
    thidar = user_dao.get_user_by_id(2)
    assert thidar == {"id": 2, "name": "Thidar", "age": 25}

def test_update_user(user_dao):
    user_dao.add_user("Aung Aung", 20)
    assert user_dao.update_user(1, "Aung Aung", 21) > 0
    updated_user = user_dao.get_user_by_id(1)
    assert updated_user == {"id": 1, "name": "Aung Aung", "age": 21}

def test_get_all_users(user_dao):
    user_dao.add_user("Aung Aung", 20)
    user_dao.add_user("Thidar", 25)
    all_users = user_dao.get_all_users()
    assert all_users == [
        {"id": 1, "name": "Aung Aung", "age": 20},
        {"id": 2, "name": "Thidar", "age": 25},
    ]

def test_delete_user(user_dao):
    user_dao.add_user("Aung Aung", 20)
    assert user_dao.delete_user(1) > 0
    deleted_user = user_dao.get_user_by_id(1)
    assert deleted_user is None
