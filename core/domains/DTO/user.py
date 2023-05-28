import datetime
import uuid
from typing import Optional, Union

from pydantic import BaseModel, Field

from infrastructure.config.base import get_settings


class AuthUserSchemaInput(BaseModel):
    __settings__ = get_settings()

    email: str = Field(..., regex=__settings__.EMAIL_REGEX)
    password: str = Field(..., min_length=__settings__.PASSWORD_MIN_LENGTH)


class CreateUserSchemaInput(BaseModel):
    __settings__ = get_settings()

    email: str = Field(..., regex=__settings__.EMAIL_REGEX)
    password: str = Field(..., min_length=__settings__.PASSWORD_MIN_LENGTH)

    first_name: str
    last_name: str
    middle_name: Optional[str]


class UserForOutput(BaseModel):
    id: uuid.UUID
    email: str
    password: str
    first_name: str
    last_name: str
    middle_name: Optional[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_active: bool
