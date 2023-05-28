from fastapi import APIRouter, Depends

from core.domains import User
from core.repositories.predict_event_repository import PredictEventRepository
from infrastructure.dependencies import get_predict_event_repository
from infrastructure.utils import get_current_user

router = APIRouter()


@router.get("/predict_events")
async def predict_events(
        user: User = Depends(get_current_user),
        predict_event_repo: PredictEventRepository = Depends(get_predict_event_repository)
):
    result = await predict_event_repo.get_list_events()
    return result

