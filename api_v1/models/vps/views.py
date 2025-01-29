from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from core.models import db_helper, Vps
from .schemas import VpsUpdateSchemas, VpsSchemas, VpsCreateSchemas
from api_v1.models.dependencies import object_by_uuid
from . import crud


router = APIRouter(tags=["Vps"])


@router.get("/", response_model=List[VpsSchemas])
async def get_vpses(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_vpses(session=session)


@router.post("/", response_model=VpsSchemas, status_code=status.HTTP_201_CREATED)
async def create_error(
    vps_in: VpsCreateSchemas,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    vps = await crud.create_vps(session=session, vps_in=vps_in)
    return vps


@router.get("/{vps_uuid}/", response_model=VpsSchemas)
async def get_vps(vps: VpsSchemas = Depends(object_by_uuid)):
    return vps


@router.patch("/{vps_uuid}/", response_model=VpsSchemas)
async def update_vps(
    vps_update: VpsUpdateSchemas,
    vps: Vps = Depends(object_by_uuid),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_vps(
        session=session,
        vps=vps,
        vps_update=vps_update,
    )