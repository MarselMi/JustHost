from core.models import Vps
from sqlalchemy.engine import Result
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from fastapi import status, HTTPException

from .schemas import VpsCreateSchemas, VpsUpdateSchemas


async def get_vpses(session: AsyncSession,) -> List[Vps]:
    query = select(Vps).order_by(Vps.id)
    result: Result = await session.execute(query)
    res = result.scalars().all()
    return list(res)


async def get_vps(
    session: AsyncSession,
    vps_uuid: str,
) -> Vps | None:
    return await session.get(Vps, vps_uuid)


async def create_vps(
    session: AsyncSession,
    vps_in: VpsCreateSchemas,
) -> Vps:
    try:
        obj = Vps(**vps_in.model_dump())
        session.add(obj)
        await session.commit()
        return obj
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid data"
        )


async def update_vps(
    session: AsyncSession,
    vps: Vps,
    vps_update: VpsUpdateSchemas,
) -> Vps:
    for name, value in vps_update.model_dump(exclude_unset=True).items():
        setattr(vps, name, value)

    await session.commit()
    return vps