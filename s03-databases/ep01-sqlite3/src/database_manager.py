import sqlite3

class DatabaseManager:
    _instance = None
    _connection: sqlite3.Connection | None = None

    def __new__(cls, db_url = "default.db") -> "DatabaseManager":
        if not cls._instance:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            try:
                cls._instance._connection = sqlite3.connect(db_url)
            except sqlite3.Error as e:
                raise RuntimeError(f"Failed to connect to database: {e}")
        return cls._instance 

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if self._connection:
            self._connection.close()
            self._connection = None
            self._instance = None

    def create_table(self, table_name: str, columns: dict[str, str]):
        if not self._connection:
            raise RuntimeError("Database connection is not established.")

        columns_with_types = ", ".join([f"{col} {typ}" for col, typ in columns.items()])
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types});"

        try:
            cursor = self._connection.cursor()
            cursor.execute(create_table_sql)
            self._connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating table {table_name}: {e}")

    def execute_query(self, query: str, params: tuple = ()):
        if not self._connection:
            raise RuntimeError("Database connection is not established.")

        try:
            cursor = self._connection.cursor()
            cursor.execute(query, params)
            self._connection.commit()
            return cursor.fetchall()
        except sqlite3.Error as e:
            raise RuntimeError(f"Error executing query: {e}")
        
    def execute_update(self, query: str, params: tuple = ()):
        if not self._connection:
            raise RuntimeError("Database connection is not established.")

        try:
            cursor = self._connection.cursor()
            cursor.execute(query, params)
            self._connection.commit()
            return cursor.rowcount
        except sqlite3.Error as e:
            raise RuntimeError(f"Error executing update: {e}")