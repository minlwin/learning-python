from sqlmodel import Session, select
from app.model import Township

class TownshipService:
    def __init__(self, session:Session) -> None:
        self.session = session

    def get_all(self) -> list[Township]:
        return list(self.session.exec(select(Township)).all()   )

    def get_township(self, township_id: int) -> Township | None:
        return self.session.get(Township, township_id)

    def get_townships_by_region(self, region_id: int):
        statement = select(Township).where(Township.region_id == region_id)
        return self.session.exec(statement).all()

    def create_township(self, township: Township) -> Township:
        self.session.add(township)
        self.session.commit()
        self.session.refresh(township)
        return township

    def update_township(self, township_id: int, township: Township) -> Township | None:
        for_update = self.session.get(Township, township_id)
        if not for_update:
            return None
        for_update.name = township.name
        for_update.region_id = township.region_id
        self.session.commit()
        self.session.refresh(for_update)
        return for_update

    def delete_township(self, township_id: int) -> Township | None:
        for_delete = self.session.get(Township, township_id)
        if not for_delete:
            return None
        self.session.delete(for_delete)
        self.session.commit()
        return for_delete