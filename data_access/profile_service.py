from typing import List, Sequence
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from domain.models.profile import Profile


async def get_all_profiles(db: AsyncSession) -> Sequence[Profile]:
    query = select(Profile)
    result = await db.execute(query)
    return result.scalars().all()


async def get_all_profiles_by_user(db: AsyncSession, user_id: int) -> Sequence[Profile]:
    query = select(Profile).where(Profile.user_id == user_id)
    result = await db.execute(query)
    return result.scalars().all()


async def get_profile(db: AsyncSession, profile_id: int) -> Profile | None:
    return await db.get(Profile, profile_id)


async def create_profile(db: AsyncSession, profile: ProfileCreate) -> Profile:
    profile = Profile()
    db.add(profile)
    await db.commit()
    return profile


async def update_profile(db: AsyncSession, profile_id: int, profile: UpdateCreate) -> Profile:
    stmt = (
        update(Profile)
        .where(Profile.id == profile_id)
        .values(**profile.dict())
    )
    result = await db.execute(stmt)
    return profile


async def delete_product(session: AsyncSession, profile: Profile) -> None:
    await session.delete(profile)
    await session.commit()
