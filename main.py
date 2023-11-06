from fastapi import Depends, FastAPI

from application.view_router import view_router
from application.profile_router import profile_router
from user_auth.auth import auth_backend
from domain.schemas.user import UserRead, UserCreate, UserUpdate
from user_auth.user_manager import get_user_manager, fastapi_users, us_rout, current_user

app = FastAPI(
    title="IntroWorld",
    docs_url="/docs"
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

app.include_router(
    us_rout,
    prefix="/users",
    tags=["users"],
)

app.include_router(
    profile_router,
    prefix="/profiles",
    tags=["Profile"]
)

app.include_router(view_router)