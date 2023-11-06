from typing import List, TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import Mapped, relationship, mapped_column

from db import Base

if TYPE_CHECKING:
    from .profile import Profile


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    profiles: Mapped[List["Profile"]] = relationship(back_populates="user_auth")
