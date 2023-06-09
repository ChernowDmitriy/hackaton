from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.domains import ApartmentBuildingsWithTEC
from core.domains.DTO.unom_item import ItemUnomSchemaOutput


class ApartmentBuildingRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_item(self, unom_id: int):
        query = select(ApartmentBuildingsWithTEC).where(ApartmentBuildingsWithTEC.unom == unom_id)
        result = await self._session.execute(query)
        result = result.scalars().all()
        if not result:
            return {}
        response = ItemUnomSchemaOutput(
            statusMkd=result[0].col_3163,
            floor_count=result[0].col_759,
            year=result[0].col_756,
            total_area=result[0].col_762,
            project_series=result[0].col_758,
            materialWall=result[0].col_769,
            count_passenger_elevators=result[0].col_771,
            count_cargo_passenger_elevators=result[0].col_772,
            total_area_of_residential_premises=result[0].col_763,
            total_area_of_non_residential_premises=result[0].col_764,
            number_of_entrances=result[0].col_760,
            number_of_freight_elevators=result[0].col_3363,
            type_of_housing_stock=result[0].col_2463,
            a_sign_of_a_building_accident=result[0].col_770,
            apartments_number=result[0].col_761,
            materialRoof=result[0].col_781,
            mcd_management_status=result[0].col_103506,
            appointment=result[0].col_754,
            the_order_of_roof_cleaning=result[0].col_775,
            construction_volume=result[0].col_765,
            object_wear_and_tear=result[0].col_766,
            reason_change_status=result[0].col_3468,
            parent_id=result[0].parent_id,
            year_reconstruction=result[0].col_757,
            social_object_type=result[0].col_2156,
            ownership_form=result[0].col_755,
            energy_efficiency_class=result[0].col_767,
        )
        return response
