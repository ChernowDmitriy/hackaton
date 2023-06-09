from typing import List

from fastapi import APIRouter, Depends

from core.domains import User
from core.domains.DTO.predict_event import PredictEventSchemaOutput
from core.domains.DTO.predicted_major_repairs import PredictedMajorRepairs
from core.filtering.predict_event_filter import PredictEventFiltering, PredictMajorRepairsFiltering
from core.repositories.major_repairs_repository import PredictedMajorRepairsRepository
from core.repositories.predict_event_repository import PredictEventRepository
from infrastructure.dependencies import get_predict_event_repository, get_major_repairs_repository
from infrastructure.utils import get_current_user

router = APIRouter()


@router.get("/predict_events", response_model=List[PredictEventSchemaOutput])
async def predict_events(
        filtering_fields: PredictEventFiltering = Depends(),
        # user: User = Depends(get_current_user),
        predict_event_repo: PredictEventRepository = Depends(get_predict_event_repository),
):
    result = await predict_event_repo.get_list_events(filtering_fields)
    return result


@router.get("/major_repairs", response_model=List[PredictedMajorRepairs])
async def major_repairs(
        filtering_fields: PredictMajorRepairsFiltering = Depends(),
        # user: User = Depends(get_current_user),
        major_repairs_repo: PredictedMajorRepairsRepository = Depends(get_major_repairs_repository)
):
    return await major_repairs_repo.get_list_major_repairs(filtering_fields)
