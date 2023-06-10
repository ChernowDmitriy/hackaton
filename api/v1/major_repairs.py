from typing import List

from fastapi import APIRouter, Depends

from core.domains.DTO.predicted_major_repairs import PredictedMajorRepairsSchemaOutput
from core.filtering.predict_event_filter import PredictMajorRepairsFiltering
from core.repositories.major_repairs_repository import PredictedMajorRepairsRepository
from infrastructure.dependencies import get_major_repairs_repository

router = APIRouter()


@router.get("/major_repairs", response_model=List[PredictedMajorRepairsSchemaOutput])
async def major_repairs(
        filtering_fields: PredictMajorRepairsFiltering = Depends(),
        # user: User = Depends(get_current_user),
        major_repairs_repo: PredictedMajorRepairsRepository = Depends(get_major_repairs_repository)
):
    return await major_repairs_repo.get_list_major_repairs(filtering_fields)
