from pydantic import BaseModel


class Settings(BaseModel):
    # Project information
    PROJECT_TITLE: str = 'Hackaton'
    PROJECT_VERSION: str = '1.0'

    # Postgres DB
    POSTGRES_URL: str = 'postgresql+asyncpg://postgres:postgres@db/hackaton'

    # Security
    SECRET_KEY: str = '123456'
    HASHING_ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 5  # 5 min
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 90  # 90 days
    JWT_SECRET: str = '123456'

    # Validation
    EMAIL_REGEX: str = (
        r"^([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$"
    )
    PASSWORD_MIN_LENGTH: int = 8

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


def get_settings() -> Settings:
    return Settings()
