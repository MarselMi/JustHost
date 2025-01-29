from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, status

from core.models import db_helper
from api_v1.models.vps import crud


async def object_by_uuid(
    vps_uuid: str,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    vps = await crud.get_vps(session=session, vps_uuid=vps_uuid)
    if not vps:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"vps с uuid {vps_uuid} не найден",
        )
    return vps