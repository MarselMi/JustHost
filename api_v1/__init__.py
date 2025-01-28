from fastapi import APIRouter

from api_v1.models.vps.views import router as vps_router


router = APIRouter()
router.include_router(router=vps_router, prefix="/vps")