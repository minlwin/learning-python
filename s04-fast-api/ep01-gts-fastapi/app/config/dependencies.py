from fastapi import Depends
from sqlmodel import Session

from app.config.database import get_session
from app.service.region_service import RegionService
from app.service.township_service import TownshipService

def get_region_service(session: Session = Depends(get_session)) -> RegionService:
    return RegionService(session=session)

def get_township_service(session: Session = Depends(get_session)) -> TownshipService:
    return TownshipService(session=session)
