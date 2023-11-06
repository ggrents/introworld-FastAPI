from typing import Annotated

from fastapi import APIRouter, Depends, Body, Path
from sqlalchemy.ext.asyncio import AsyncSession

from data_access import profile_service
from dependencies import get_async_session
from domain.models.user import User
from domain.schemas.profile import ProfileCreateUpdateSchema
from user_auth.user_manager import current_user, current_superuser

profile_router = APIRouter()


@profile_router.post("")
async def create_profile(profile: Annotated[ProfileCreateUpdateSchema, Body()],
                         db: AsyncSession = Depends(get_async_session),
                         user: User = Depends(current_user),
                         ):
    return await profile_service.create_profile(db, user, profile)


@profile_router.get("")
async def list_profiles(db: AsyncSession = Depends(get_async_session),
                        super_user: User = Depends(current_superuser),
                        ):
    return await profile_service.get_all_profiles(db)


@profile_router.get("/me")
async def list_my_profiles(
        db: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    return await profile_service.get_all_profiles_by_user(db, user.id)


@profile_router.patch("/me/{profile_id}")
async def list_my_profiles(
        profile_id: Annotated[int, Path(gt=0)],
        profile: Annotated[ProfileCreateUpdateSchema, Body()],
        db: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    return await profile_service.update_profile(db, profile_id, profile)
