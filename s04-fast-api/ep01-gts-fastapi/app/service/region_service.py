from sqlmodel import Session, select

from app.model import region

class RegionService:
    def __init__(self, session:Session):
        self.session = session

    def get_region_by_id(self, region_id: int):
        statement = select(region.Region).where(region.Region.id == region_id)
        result = self.session.exec(statement)
        return result.first()
    
    def get_all_regions(self):
        statement = select(region.Region)
        result = self.session.exec(statement)
        return result.all()
    
    def create_region(self, region_data: region.Region):
        self.session.add(region_data)
        self.session.commit()
        self.session.refresh(region_data)
        return region_data
    
    def update_region(self, region_id: int, region_data: region.Region):
        existing_region = self.get_region_by_id(region_id)
        if existing_region:
            existing_region.name = region_data.name
            existing_region.region = region_data.region
            self.session.commit()
            self.session.refresh(existing_region)
            return existing_region
        return None

    def delete_region(self, region_id: int):
        existing_region = self.get_region_by_id(region_id)
        if existing_region:
            self.session.delete(existing_region)
            self.session.commit()
            return existing_region
        return None