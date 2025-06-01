from sqlalchemy.ext.asyncio import AsyncSession

from database import async_session_factory


async def get_db() -> AsyncSession:
    db = async_session_factory()

    try:
        yield db
    finally:
        await db.close()
