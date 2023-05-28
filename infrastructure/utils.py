from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError, ExpiredSignatureError
from jwt import InvalidTokenError
from passlib.context import CryptContext

from core.domains.models.user import User
from core.exceptions import SignatureVerificationFailed
from core.repositories.user_repository import UserRepository
from infrastructure.config.base import get_settings
from infrastructure.dependencies import get_user_repository

settings = get_settings()
security_scheme = HTTPBearer()


def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, settings.HASHING_ALGORITHM)
        return payload
    except (InvalidTokenError, ExpiredSignatureError, JWTError):
        raise SignatureVerificationFailed


def encode_token(payload: dict) -> str:
    encoded_jwt = jwt.encode(payload,
                             settings.JWT_SECRET,
                             algorithm=settings.HASHING_ALGORITHM)
    return encoded_jwt


async def get_current_user(
        auth_credentials: HTTPAuthorizationCredentials = Depends(security_scheme),
        user_repository: UserRepository = Depends(get_user_repository)
) -> User:
    payload = verify_token(auth_credentials.credentials)
    user_id = payload.get("sub")
    user = await user_repository.get_user_by_id(user_id)
    return user
