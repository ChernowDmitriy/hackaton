from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.repositories.predict_event_repository import PredictEventRepository
from core.repositories.user_repository import UserRepository
from core.services.auth_service import AuthService
from infrastructure.database import async_session


async def get_db() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
        finally:
            await session.close()


async def get_user_repository(db: AsyncSession = Depends(get_db)) -> UserRepository:
    return UserRepository(db)


async def get_auth_service(db: AsyncSession = Depends(get_db)) -> AuthService:
    return AuthService(UserRepository(db))


async def get_predict_event_repository(db: AsyncSession = Depends(get_db)) -> PredictEventRepository:
    return PredictEventRepository(db)
