import uuid

from fastapi import Depends, FastAPI
from fastapi_users import FastAPIUsers

from user.auth import auth_backend
from user.models import User
from user.schemas import UserRead, UserCreate
from user.user_manager import get_user_manager

from user.api import user_router

app = FastAPI(title="IntroWorld")

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

app.include_router(user_router, tags=["users"])


@app.get("/")
def m(user: User = Depends(current_user)) :
    if not user :
        return "no access!"
    return f"Hello {user.username}! with email {user.email}"

# -------------------------------------------------------------------- #

# @app.on_event("startup")
# async def on_startup():
#     await create_db_and_tables()
