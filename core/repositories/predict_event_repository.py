from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.const import MAPPED_PREDICT_EVENT_FIELDS, code_decipher
from core.domains import PredictedEvent as PredictedEventModel, ApartmentBuildingsWithTEC
from core.domains.DTO.predict_event import PredictEventSchemaOutput, ItemEventSchemaOutput, UpdateItemSchemaOutput
from core.filtering.predict_event_filter import PredictEventFiltering


class PredictEventRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_list_events(self, filtering_fields: PredictEventFiltering):
        query = select(PredictedEventModel).options(selectinload(PredictedEventModel.unom)).join(
            ApartmentBuildingsWithTEC, PredictedEventModel.unom_id == ApartmentBuildingsWithTEC.COL_782)

        if filtering_fields.dict(exclude_none=True):
            if filtering_fields.unom:
                query = query.where(PredictedEventModel.unom_id == filtering_fields.unom)

            if filtering_fields.type:
                query = query.where()

            if filtering_fields.address:
                query = query.filter(ApartmentBuildingsWithTEC.name.ilike(f"%{filtering_fields.address}%"))

            if filtering_fields.project_series:
                query = query.where(ApartmentBuildingsWithTEC.COL_758 == int(filtering_fields.project_series))

            if filtering_fields.start_expected_duration and filtering_fields.end_expected_duration:
                cleft = int(filtering_fields.start_expected_duration)
                cright = int(filtering_fields.end_expected_duration)
                query = query.where(
                    (PredictedEventModel.expected_duration >= cleft) &
                    (PredictedEventModel.expected_duration <= cright)
                )

            if filtering_fields.area:
                query = query.where()

            if filtering_fields.district:
                query = query.where()

            if filtering_fields.start_construction_year and filtering_fields.end_construction_year:
                cleft = int(filtering_fields.start_construction_year)
                cright = int(filtering_fields.end_construction_year)
                query = query.where(
                    (ApartmentBuildingsWithTEC.COL_756 >= cleft) &
                    (ApartmentBuildingsWithTEC.COL_756 <= cright)
                )

            if filtering_fields.warn:
                query = query.where()

            if filtering_fields.mkd:
                query = query.where()

            if filtering_fields.statusMkd:
                query = query.where()

        result = await self._session.execute(query.limit(500))
        predict_record = result.scalars().all()
        if predict_record:
            response = [
                PredictEventSchemaOutput(
                    unom=record.unom_id,
                    type=record.name,
                    date=record.expected_date,
                    duration=record.expected_duration,
                    organization=record.organization,
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

    async def get_item_predict_event_by_unom_id(self, unom_id: int):
        query = select(PredictedEventModel).options(selectinload(PredictedEventModel.unom)).join(
            ApartmentBuildingsWithTEC, PredictedEventModel.unom_id == ApartmentBuildingsWithTEC.COL_782).where(
            PredictedEventModel.unom_id == unom_id
        )
        result = await self._session.execute(query)
        predict_record = result.scalars().all()

        if not predict_record:
            return []

        response = [
            ItemEventSchemaOutput(
                unom=record.unom_id,
                type=record.name,
                date=record.expected_date,
                duration=record.expected_duration,
                organization=record.organization,
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

    async def update_item_by_unom_id(self, unom_id: int, item_update: UpdateItemSchemaOutput):
        to_update = {}
        dict_item_update = item_update.dict(exclude_none=True)
        for key in dict_item_update:
            to_update[MAPPED_PREDICT_EVENT_FIELDS[key]] = dict_item_update[key]
        query = update(PredictedEventModel).values(**to_update)
        await self._session.execute(query)
        await self._session.commit()
        updated_item = await self.get_item_predict_event_by_unom_id(unom_id)
        return updated_item
