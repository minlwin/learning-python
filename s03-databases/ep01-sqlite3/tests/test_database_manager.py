import pytest
from src.database_manager import DatabaseManager

@pytest.fixture
def db_manager():
    """Create a fresh in-memory DB for each test."""
    with DatabaseManager(":memory:") as db:
        # Create the users table
        db.create_table("users", {
            "id": "INTEGER PRIMARY KEY",
            "name": "TEXT",
            "age": "INTEGER"
        })
        yield db  # provide the db_manager to the test
        # automatic cleanup happens when context exits

def test_create_table(db_manager):
    result = db_manager.execute_query(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='users';"
    )
    assert result, "Table 'users' should exist"

def test_insert_and_select(db_manager):
    db_manager.execute_update(
        "INSERT INTO users (name) VALUES (?)", ("Alice",)
    )
    rows = db_manager.execute_query("SELECT * FROM users;")
    assert rows[0][1] == "Alice"

def test_update(db_manager):
    db_manager.execute_update(
        "INSERT INTO users (name) VALUES (?)", ("Bob",)
    )
    db_manager.execute_update(
        "UPDATE users SET name=? WHERE name=?", ("Robert", "Bob")
    )
    rows = db_manager.execute_query("SELECT * FROM users;")
    assert rows[0][1] == "Robert"

def test_delete(db_manager):
    db_manager.execute_update(
        "INSERT INTO users (name) VALUES (?)", ("Charlie",)
    )
    db_manager.execute_update(
        "DELETE FROM users WHERE name=?", ("Charlie",)
    )
    rows = db_manager.execute_query("SELECT * FROM users;")
    assert rows == []
