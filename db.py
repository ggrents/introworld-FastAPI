from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base


Base: DeclarativeMeta = declarative_base()
DATABASE_URL = "postgresql+asyncpg://postgres:2996@localhost:5432/INTROWORLD_DB"
engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
