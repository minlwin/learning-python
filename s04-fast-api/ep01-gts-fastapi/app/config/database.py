from sqlmodel import Session, create_engine

DB_URL = "sqlite:///database.db"
engine = create_engine(DB_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session