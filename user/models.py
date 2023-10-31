from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, String, DateTime

from db import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    registration_date = Column(DateTime, default=datetime.utcnow)

