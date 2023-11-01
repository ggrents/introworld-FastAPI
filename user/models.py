from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, String, DateTime

from db import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass

