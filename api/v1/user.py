from fastapi import APIRouter, Depends

from core.domains.DTO.user import UserForOutput
from core.domains.models.user import User
from infrastructure.utils import get_current_user

router = APIRouter()


@router.get("/users/me", response_model=UserForOutput)
async def get_current_authenticated_user(
        user: User = Depends(get_current_user)):
    return UserForOutput(**user.to_dict())
