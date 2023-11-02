from datetime import datetime
from typing import Optional

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass


class Profile(Base):
    __tablename__ = "Profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    first_name: Mapped[str] = mapped_column(String(64), index=True)
    last_name: Mapped[str] = mapped_column(String(64), index=True)
    gender: Mapped[bool] = mapped_column(Boolean, nullable=False)
    about: Mapped[Optional[str]] = mapped_column(String(140))
    image_path: Mapped[Optional[str]] = mapped_column(String(140))
