from fastapi import APIRouter, Depends

from core.domains.DTO.unom_item import UpdateItemUnomSchemaOutput
from core.repositories.apartment_building_repository import ApartmentBuildingRepository
from infrastructure.dependencies import get_apartment_building_repository

router = APIRouter()


@router.get('/apartment_buildings-with_tec/{unom_id}')
async def get_item_from_unom(
        unom_id: int,
        # user: User = Depends(get_current_user),
        get_predict_event_repo: ApartmentBuildingRepository = Depends(get_apartment_building_repository)
):
    return await get_predict_event_repo.get_item(unom_id)


@router.put('/apartment_buildings-with_tec/{unom_id}')
async def update_unom_by_id(
        unom_id: int,
        item_update: UpdateItemUnomSchemaOutput,
        # user: User = Depends(get_current_user),
        get_predict_event_repo: ApartmentBuildingRepository = Depends(get_apartment_building_repository)
):
    return await get_predict_event_repo.update_item_by_unom_id(unom_id, item_update)
