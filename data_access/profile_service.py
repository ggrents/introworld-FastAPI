from typing import List, Sequence
from sqlalchemy import select, update, insert
from sqlalchemy.ext.asyncio import AsyncSession
from domain.models.profile import Profile
from domain.models.user import User
from domain.schemas.profile import ProfileCreateUpdateSchema


async def get_all_profiles(db: AsyncSession) :
    query = select(Profile)
    result = await db.execute(query)
    return result.scalars().all()


async def get_all_profiles_by_user(db: AsyncSession, user_id: int) -> Sequence[Profile]:
    query = select(Profile).where(Profile.user_id == user_id)
    result = await db.execute(query)
    return result.scalars().all()


async def get_profile(db: AsyncSession, profile_id: int) -> Profile | None:
    return await db.get(Profile, profile_id)


async def create_profile(db: AsyncSession, user: User, profile: ProfileCreateUpdateSchema):
    query = insert(Profile).values(username=profile.username,
                                   first_name=profile.first_name,
                                   last_name=profile.last_name,
                                   gender=profile.gender,
                                   user_id=user.id)

    await db.execute(query)
    await db.commit()

    return profile


async def update_profile(db: AsyncSession, profile_id: int, profile: ProfileCreateUpdateSchema) -> Profile:
    stmt = (
        update(Profile)
        .where(Profile.id == profile_id)
        .values(**profile.model_dump())
    )
    result = await db.execute(stmt)
    await db.commit()
    return profile


async def delete_product(session: AsyncSession, profile: Profile) -> None:
    await session.delete(profile)
    await session.commit()
