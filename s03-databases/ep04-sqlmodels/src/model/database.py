from sqlmodel import create_engine

DB_URL = "postgresql+psycopg2://testdb:testdb@localhost:5432/testdb"
engine = create_engine(DB_URL, echo=True)
