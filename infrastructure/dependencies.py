from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.repositories.user_repository import UserRepository
from core.services.auth_service import AuthService
from infrastructure.database import _async_scoped_session, async_session


# async def get_db():
#     return _async_scoped_session()

async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session


async def get_user_repository(db: AsyncSession = Depends(get_db)) -> UserRepository:
    return UserRepository(db)


async def get_auth_service(db: AsyncSession = Depends(get_db)) -> AuthService:
    return AuthService(UserRepository(db))
