from typing import List

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import Mapped, relationship

from db import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"
    children: Mapped[List["Profile"]] = relationship(back_populates="user")
