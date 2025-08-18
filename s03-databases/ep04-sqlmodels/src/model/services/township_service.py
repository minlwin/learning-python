from sqlalchemy import Engine
from sqlmodel import Session, select

from src.model.entity.region import Region
from src.model.entity.township import Township

class TownshipService:
    def __init__(self, engine:Engine) -> None:
        self.engine = engine

    def create(self, entity:Township) -> Township:
        with Session(self.engine) as session:
            session.add(entity)
            session.commit()
            session.refresh(entity)
            return entity
            
    def update(self, entity:Township) -> Township:
        if entity.id is None:
            raise ValueError("Entity must have an ID to update.")
        with Session(self.engine) as session:
            session.merge(entity)
            session.commit()
            return entity

    def find_by_region(self, region_id:int) -> list[Township]:
        with Session(self.engine) as session:
            statement = select(Township).where(Township.region_id == region_id)
            return list(session.exec(statement))
        
    def find_one(self, township_id:int) -> Township | None:
        with Session(self.engine) as session:
            statement = select(Township).where(Township.id == township_id)
            township = session.exec(statement).one_or_none()

            if township is None:
                return None

            statement = select(Region).where(Region.id == township.region_id)
            region = session.exec(statement).one()
            township.region = region

            return township
        
    def delete(self, township_id:int) -> bool:
        with Session(self.engine) as session:
            entity = self.find_one(township_id)
            if entity:
                session.delete(entity)
                session.commit()
                return True
            return False
