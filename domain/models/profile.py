import uuid
from typing import Optional, TYPE_CHECKING

from fastapi_users_db_sqlalchemy import GUID
from sqlalchemy import String, Boolean, ForeignKey, Column, Integer, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base

if TYPE_CHECKING:
    from .user import User


class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(64), index=True)
    first_name: Mapped[str] = mapped_column(String(64), index=True)
    last_name: Mapped[str] = mapped_column(String(64), index=True)
    gender: Mapped[bool] = mapped_column(Boolean, nullable=False)
    about: Mapped[Optional[str]] = mapped_column(String(140))
    image_path: Mapped[Optional[str]] = mapped_column(String(140))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="profiles")
