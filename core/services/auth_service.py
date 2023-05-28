from typing import Union

from passlib.context import CryptContext

from core.domains.DTO.user import AuthUserSchemaInput, CreateUserSchemaInput
from core.domains.models.user import User
from core.exceptions import UserEmailAlreadyExistsException
from core.repositories.user_repository import UserRepository
from infrastructure.config.base import get_settings


class AuthService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository
        self._password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self._settings = get_settings()

    def hash_password(self, password: str) -> str:
        return self._password_context.hash(password)

    async def authenticate_user(self, data: AuthUserSchemaInput) -> Union[User, None]:
        user = await self._user_repository.get_user_by_email(data.email)
        if user and self.verify_password(data.password, user.password):
            return user
        return None

    async def sign_up(self, data: CreateUserSchemaInput) -> User:
        existing_user = await self._user_repository.get_user_by_email(data.email)
        if existing_user:
            raise UserEmailAlreadyExistsException

        hashed_password = self.hash_password(data.password)
        data.password = hashed_password
        insert_data = User(**data.dict())
        created_user = await self._user_repository.create_user(insert_data)
        return created_user

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self._password_context.verify(plain_password, hashed_password)

