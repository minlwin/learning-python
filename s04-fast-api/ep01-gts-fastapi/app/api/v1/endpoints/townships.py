from fastapi import APIRouter, Depends

from app.config.dependencies import get_township_service
from app.model import Township
from app.service import TownshipService

router = APIRouter()

@router.get("/")
def get_townships(service:TownshipService = Depends(get_township_service)):
    return service.get_all()

@router.get("/{township_id}")
def get_township(township_id: int, service:TownshipService = Depends(get_township_service)):
    return service.get_township(township_id)

@router.post("/")
def create(township:Township, service:TownshipService = Depends(get_township_service)):
    return service.create_township(township)

@router.put("/{township_id}")
def update(township_id: int, township: Township,  service:TownshipService = Depends(get_township_service)):
    return service.update_township(township_id, township)

@router.delete("/{township_id}")
def delete(township_id: int, service:TownshipService = Depends(get_township_service)):
    return service.delete_township(township_id)