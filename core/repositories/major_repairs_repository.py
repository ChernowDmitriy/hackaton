from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.const import code_decipher
from core.domains import MajorRepairsApartmentBuilding as MajorRepairsApartmentBuildingModel, ApartmentBuildingsWithTEC
from core.domains.DTO.predicted_major_repairs import PredictedMajorRepairs
from core.filtering.predict_event_filter import PredictMajorRepairsFiltering


class PredictedMajorRepairsRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_list_major_repairs(self, filtering_fields: PredictMajorRepairsFiltering):
        query = select(
            MajorRepairsApartmentBuildingModel
        ).options(selectinload(MajorRepairsApartmentBuildingModel.unom)).join(
            ApartmentBuildingsWithTEC, MajorRepairsApartmentBuildingModel.unom_id == ApartmentBuildingsWithTEC.COL_782)

        if filtering_fields.dict(exclude_none=True):
            if filtering_fields.unom:
                query = query.where(MajorRepairsApartmentBuildingModel.unom_id == filtering_fields.unom)

            if filtering_fields.type:
                query = query.where()

            if filtering_fields.address:
                query = query.filter(ApartmentBuildingsWithTEC.name.ilike(f"%{filtering_fields.address}%"))

            if filtering_fields.project_series:
                query = query.where(ApartmentBuildingsWithTEC.col_758 == int(filtering_fields.project_series))

            if filtering_fields.start_expected_duration and filtering_fields.end_expected_duration:
                cleft = int(filtering_fields.start_expected_duration)
                cright = int(filtering_fields.end_expected_duration)
                query = query.where(
                    (MajorRepairsApartmentBuildingModel.expected_duration >= cleft) &
                    (MajorRepairsApartmentBuildingModel.expected_duration <= cright)
                )

            if filtering_fields.area:
                query = query.where()

            if filtering_fields.district:
                query = query.where()

            if filtering_fields.start_construction_year and filtering_fields.end_construction_year:
                cleft = int(filtering_fields.start_construction_year)
                cright = int(filtering_fields.end_construction_year)
                query = query.where(
                    (ApartmentBuildingsWithTEC.col_756 >= cleft) &
                    (ApartmentBuildingsWithTEC.col_756 <= cright)
                )

            if filtering_fields.warn:
                query = query.where()

            if filtering_fields.mkd:
                query = query.where()

            if filtering_fields.statusMkd:
                query = query.where()

        result = await self._session.execute(query)
        predict_record = result.scalars().all()
        if predict_record:
            response = [
                PredictedMajorRepairs(
                    unom=record.unom_id,
                    type=record.name,
                    date=record.expected_date,
                    duration=record.expected_duration,
                    year=record.unom.COL_756,
                    warn=code_decipher['Признак аварийности здания'].get(record.unom.COL_770),
                    materialRoof=code_decipher['Материал кровли'].get(record.unom.COL_781),
                    materialWall=code_decipher['Материал стен'].get(record.unom.COL_769),
                    fond=code_decipher['Тип жилищного фонда'].get(record.unom.COL_2463),
                    mkd=code_decipher['Статус МКД'].get(record.unom.COL_103506),
                    statusMkd=code_decipher['Статус управления МКД'].get(record.unom.COL_3243)
                ) for record in predict_record
            ]
            return response

        return []
