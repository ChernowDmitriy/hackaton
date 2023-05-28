from datetime import timedelta, datetime

from fastapi import APIRouter, Depends

from core.domains.DTO.token import Token, UpdateTokensSchemaInput
from core.domains.DTO.user import AuthUserSchemaInput, CreateUserSchemaInput
from core.domains.models.user import User
from core.exceptions import InvalidCredentials
from core.services.auth_service import AuthService
from infrastructure.config.base import get_settings
from infrastructure.dependencies import get_auth_service
from infrastructure.utils import encode_token, get_current_user, verify_token

router = APIRouter()
settings = get_settings()


@router.post('/signin', response_model=Token)
async def auth(
        data: AuthUserSchemaInput,
        auth_service: AuthService = Depends(get_auth_service)
):
    user = await auth_service.authenticate_user(data)
    if user is None:
        raise InvalidCredentials

    now = datetime.utcnow()
    access_token_payload = {
        'sub': user.id,
        'iat': now,
        'nbf': now,
        'exp': now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    }
    refresh_token_payload = {
        'sub': user.id,
        'iat': now,
        'nbf': now,
        'exp': now + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES),
    }

    access_token = encode_token(access_token_payload)
    refresh_token = encode_token(refresh_token_payload)
    response = Token(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer"
    )
    return response


@router.post('/signup')
async def sign_up(
        data: CreateUserSchemaInput,
        auth_service: AuthService = Depends(get_auth_service)
):
    user = await auth_service.sign_up(data)

    now = datetime.utcnow()
    access_token_payload = {
        'sub': 'auth',
        'iat': now,
        'nbf': now,
        'exp': now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        'user': user.id
    }
    refresh_token_payload = {
        'sub': 'auth',
        'iat': now,
        'nbf': now,
        'exp': now + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES),
        'user': user.id
    }

    access_token = encode_token(access_token_payload)
    refresh_token = encode_token(refresh_token_payload)
    response = Token(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer"
    )
    return response


@router.post('/refresh_token', response_model=Token)
async def refresh_tokens(
        data: UpdateTokensSchemaInput,
        user: User = Depends(get_current_user)
):
    verify_token(data.refresh_token)
    now = datetime.utcnow()
    access_token_payload = {
        'sub': 'auth',
        'iat': now,
        'nbf': now,
        'exp': now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        'user': user.id
    }
    refresh_token_payload = {
        'sub': 'auth',
        'iat': now,
        'nbf': now,
        'exp': now + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES),
        'user': user.id
    }
    access_token = encode_token(access_token_payload)
    refresh_token = encode_token(refresh_token_payload)
    response = Token(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer"
    )
    return response
