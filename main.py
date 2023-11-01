import uuid

from fastapi import Depends, FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi_users import FastAPIUsers
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import create_db_and_tables
from dependencies import get_user_db, get_async_session
from user.auth import auth_backend
from user.models import User
from user.schemas import UserRead, UserCreate, UserUpdate
from user.user_manager import get_user_manager

app = FastAPI(
    title="IntroWorld",
    docs_url="/"
              )

# -------------------- Connection Users management ---------------------#


fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)
current_user = fastapi_users.current_user(optional=True)



app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

us_rout = fastapi_users.get_users_router(UserRead, UserUpdate)

app.include_router(
    us_rout,
    prefix="/users",
    tags=["users"],
)


# app.include_router(user_router, tags=["users"])


@app.get("/")
def m(user: User = Depends(current_user)):
    if not user:
        return "no access!"
    return f"Hello {user.hashed_password}! with email {user.email}"


# -------------------------------------------------------------------- #

@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()



