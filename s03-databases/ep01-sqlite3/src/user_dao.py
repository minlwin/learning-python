from src.database_manager import DatabaseManager


class UserDao:
    def __init__(self, dbm:DatabaseManager):
        self.dbm = dbm
        dbm.create_table("users", {
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "name": "TEXT",
            "age": "INTEGER"
        })

    def add_user(self, name: str, age: int) -> int:
        self.dbm.execute_update(
            "INSERT INTO users (name, age) VALUES (?, ?)", (name, age)
        )
        result = self.dbm.execute_query("SELECT last_insert_rowid();")
        if not result:
            raise RuntimeError("Failed to retrieve last inserted user ID.")

        return result[0][0]
    
    def get_user_by_id(self, id:int) -> dict | None:
        result = self.dbm.execute_query("SELECT * FROM users WHERE id = ?", (id,))
        if not result:
            return None
        user = result[0]
        return {
            "id": user[0],
            "name": user[1],
            "age": user[2]
        }
    
    def update_user(self, id: int, name: str, age: int) -> bool:
        result = self.dbm.execute_update(
            "UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, id)
        )
        return result is not None and result > 0

    def delete_user(self, id: int) -> bool:
        result = self.dbm.execute_update(
            "DELETE FROM users WHERE id = ?", (id,)
        )
        return result is not None and result > 0
    
    def get_all_users(self) -> list[dict]:
        result = self.dbm.execute_query("SELECT * FROM users")
        if not result:
            return []
        users = []
        for user in result:
            users.append({
                "id": user[0],
                "name": user[1],
                "age": user[2]
            })
        return users