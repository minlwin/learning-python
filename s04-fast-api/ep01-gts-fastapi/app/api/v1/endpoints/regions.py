from fastapi import APIRouter, Depends

from app.config.dependencies import get_region_service
from app.model import Region
from app.service.region_service import RegionService

router = APIRouter()

@router.get("/")
def read_regions(service: RegionService = Depends(get_region_service)):
    return service.get_all_regions()

@router.get("/{region_id}")
def read_region(region_id: int, service: RegionService = Depends(get_region_service)):
    return service.get_region_by_id(region_id)

@router.post("/")
def create_region(region_data: Region, service: RegionService = Depends(get_region_service)):
    return service.create_region(region_data)

@router.put("/{region_id}")
def update_region(region_id: int, region_data: Region, service: RegionService = Depends(get_region_service)):
    return service.update_region(region_id, region_data)

@router.delete("/{region_id}")
def delete_region(region_id: int, service: RegionService = Depends(get_region_service)):
    return service.delete_region(region_id)