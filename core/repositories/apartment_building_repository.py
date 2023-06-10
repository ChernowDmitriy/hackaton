from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from core.const import MAPPED_APARTMENT_FIELDS, code_decipher
from core.domains import ApartmentBuildingsWithTEC
from core.domains.DTO.unom_item import ItemUnomSchemaOutput, UpdateItemUnomSchemaOutput


class ApartmentBuildingRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_item(self, unom_id: int):
        query = select(ApartmentBuildingsWithTEC).where(ApartmentBuildingsWithTEC.COL_782 == unom_id)
        result = await self._session.execute(query)
        result = result.scalars().all()
        if not result:
            return {}

        response = ItemUnomSchemaOutput(
            statusMkd=code_decipher['Статус управления МКД'].get(result[0].COL_3243),
            floor_count=result[0].COL_759,
            year=result[0].COL_756,
            total_area=result[0].COL_762,
            project_series=code_decipher['Серия проекта'].get(result[0].COL_758),
            materialWall=code_decipher['Материал стен'].get(result[0].COL_769),
            count_passenger_elevators=result[0].COL_771,
            count_cargo_passenger_elevators=result[0].COL_772,
            total_area_of_residential_premises=result[0].COL_763,
            total_area_of_non_residential_premises=result[0].COL_764,
            number_of_entrances=result[0].COL_760,
            number_of_freight_elevators=result[0].COL_3363,
            type_of_housing_stock=code_decipher['Тип жилищного фонда'].get(result[0].COL_2463),
            a_sign_of_a_building_accident=code_decipher['Признак аварийности здания'].get(result[0].COL_770),
            apartments_number=result[0].COL_761,
            materialRoof=code_decipher['Материал кровли'].get(result[0].COL_781),
            mcd_management_status=result[0].COL_103506,
            appointment=result[0].COL_754,
            the_order_of_roof_cleaning=code_decipher['Очередность уборки кровли'].get(result[0].COL_775),
            construction_volume=result[0].COL_765,
            object_wear_and_tear=code_decipher['Категория МКД'].get(result[0].COL_766),
            reason_change_status=result[0].COL_3468,
            parent_id=result[0].PARENT_ID,
            year_reconstruction=result[0].COL_757,
            social_object_type=code_decipher['Вид социального объекта'].get(result[0].COL_2156),
            ownership_form=result[0].COL_755,
            energy_efficiency_class=result[0].COL_767,
        )
        return response

    async def update_item_by_unom_id(self, unom_id, item_update: UpdateItemUnomSchemaOutput):
        to_update = {}
        dict_item_update = item_update.dict(exclude_none=True)
        for key in dict_item_update:
            to_update[MAPPED_APARTMENT_FIELDS[key]] = dict_item_update[key]
        query = update(ApartmentBuildingsWithTEC).values(**to_update)
        await self._session.execute(query)
        await self._session.commit()
        updated_item = await self.get_item(unom_id)
        return updated_item
