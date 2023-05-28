from typing import Union
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.domains.models.user import User as UserModel


class UserRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_user_by_id(self, user_id: Union[UUID, str]) -> UserModel:
        result = await self._session.execute(select(UserModel).where(UserModel.id == user_id))
        user_record = result.scalars().first()
        return UserModel(**user_record.to_dict()) if user_record else None

    async def get_user_by_email(self, email: str) -> UserModel:
        result = await self._session.execute(select(UserModel).where(UserModel.email == email))
        user_record = result.scalars().first()
        return UserModel(**user_record.to_dict()) if user_record else None

    async def create_user(self, user: UserModel) -> UserModel:
        self._session.add(user)
        await self._session.commit()
        await self._session.refresh(user)
        await self._session.close()

        return UserModel(**user.to_dict())
