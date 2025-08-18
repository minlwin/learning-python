from sqlalchemy import Engine
from sqlmodel import Session, select

from src.model.entity.region import Region

class RegionService:
    def __init__(self, engine:Engine) -> None:
        self.engine = engine

    def create(self, entity:Region) -> Region:
        with Session(self.engine) as session:
            session.add(entity)
            session.commit()
            session.refresh(entity)
            return entity
    
    def find_one(self, id:int) -> Region | None:
        with Session(self.engine) as session:
            statement = select(Region).where(Region.id == id)
            return session.exec(statement).first()
        
    def find_all(self) -> list[Region]:
        with Session(self.engine) as session:
            statement = select(Region)
            return list(session.exec(statement).all())
        
    def update(self, entity:Region) -> Region:
        with Session(self.engine) as session:
            session.merge(entity)
            session.commit()
            return entity 
        
    def delete(self, id:int) -> bool:
        with Session(self.engine) as session:
            entity = self.find_one(id)
            if entity:
                session.delete(entity)
                session.commit()
                return True
            return False