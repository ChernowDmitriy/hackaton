from fastapi import APIRouter, Depends

from core.domains import User
from core.domains.DTO.predict_event import PredictEventSchemaOutput
from core.filtering.predict_event_filter import PredictEventFiltering
from core.repositories.predict_event_repository import PredictEventRepository
from infrastructure.dependencies import get_predict_event_repository
from infrastructure.utils import get_current_user

router = APIRouter()


@router.get("/predict_events")
async def predict_events(
        filtering_fields: PredictEventFiltering = Depends(),
        # user: User = Depends(get_current_user),
        predict_event_repo: PredictEventRepository = Depends(get_predict_event_repository),
):
    result = await predict_event_repo.get_list_events(filtering_fields)
    return result
