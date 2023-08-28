from typing import Generator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_NAME, BASE_DIR
from sqlalchemy.ext.asyncio import create_async_engine

Base = declarative_base()

DATABASE_URL = f"sqlite+aiosqlite:///{BASE_DIR}/{DB_NAME}.db"
engine = create_async_engine(DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> Generator:
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()
