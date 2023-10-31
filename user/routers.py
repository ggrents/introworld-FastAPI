from fastapi_users import FastAPIUsers
from sqlalchemy import UUID

from main import app
from user.auth import auth_backend
from user.models import User
from user.schemas import UserRead, UserCreate
from user.user_manager import get_user_manager

fastapi_users = FastAPIUsers[User, UUID](
    get_user_manager,
    [auth_backend],
)

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

current_user = fastapi_users.current_user(optional=True)
