from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_async_session
from main import us_rout
from user.models import User
from user.schemas import UserRead


@us_rout.get("/me", response_model=list[UserRead])
async def ma(db: AsyncSession = Depends(get_async_session)):
    users = await db.execute(select(User).limit(10))
    users = users.scalars().all()
    return users
