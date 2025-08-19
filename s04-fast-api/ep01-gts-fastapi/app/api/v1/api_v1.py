from fastapi import APIRouter
from app.api.v1.endpoints import regions_router, townships_router

router = APIRouter(
    prefix="/api/v1",
    tags=["v1"]
)

router.include_router(regions_router, prefix="/regions", tags=["regions"])
router.include_router(townships_router, prefix="/townships", tags=["townships"])
