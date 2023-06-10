from fastapi import APIRouter, Depends

from core.domains.DTO.predict_event import UpdateItemSchemaOutput
from core.filtering.predict_event_filter import PredictEventFiltering
from core.repositories.predict_event_repository import PredictEventRepository
from infrastructure.dependencies import get_predict_event_repository

router = APIRouter()


@router.get("/predict_events")
async def predict_events(
        filtering_fields: PredictEventFiltering = Depends(),
        # user: User = Depends(get_current_user),
        predict_event_repo: PredictEventRepository = Depends(get_predict_event_repository),
):
    result = await predict_event_repo.get_list_events(filtering_fields)
    return result


@router.get("/predict_events/{unom_id}")
async def item_predict_events(
        unom_id: int,
        # user: User = Depends(get_current_user),
        predict_event_repo: PredictEventRepository = Depends(get_predict_event_repository),
):
    return await predict_event_repo.get_item_predict_event_by_unom_id(unom_id)


@router.put("/predict_events/{unom_id}")
async def item_predict_events(
        unom_id: int,
        update_data: UpdateItemSchemaOutput,
        # user: User = Depends(get_current_user),
        predict_event_repo: PredictEventRepository = Depends(get_predict_event_repository),
):
    return await predict_event_repo.update_item_by_unom_id(unom_id, update_data)
