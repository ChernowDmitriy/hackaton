from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.const import MAPPED_PREDICT_EVENT_FIELDS, code_decipher
from core.domains import PredictedEvent as PredictedEventModel, ApartmentBuildingsWithTEC
from core.domains.DTO.predict_event import PredictEventSchemaOutput, ItemEventSchemaOutput
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

        result = await self._session.execute(query)
        predict_record = result.scalars().all()
        if predict_record:
            material_roof_id = predict_record[0].unom.COL_781
            response = [
                PredictEventSchemaOutput(
                    unom=record.unom_id,
                    # type=predict_record
                    date=record.expected_date,
                    duration=record.expected_duration,
                    organization=record.organization,
                    year=record.unom.COL_756,
                    warn=record.unom.COL_770,
                    materialRoof=code_decipher['Материал кровли'][material_roof_id],
                    materialWall=record.unom.COL_769,
                    fond=record.unom.COL_2463,
                    mkd=record.unom.COL_103506,
                    statusMkd=record.unom.COL_3243
                ) for record in predict_record
            ]
            return response
        return []

    async def get_item_predict_event_by_unom_id(self, unom_id: int):
        query = select(PredictedEventModel).options(selectinload(PredictedEventModel.unom)).join(
            ApartmentBuildingsWithTEC, PredictedEventModel.unom_id == ApartmentBuildingsWithTEC.COL_782)
        result = await self._session.execute(query)
        predict_record = result.scalars().all()
        if not predict_record:
            return []

        response = ItemEventSchemaOutput(
            unom=predict_record[0].unom_id,
            # type=predict_record
            date=predict_record[0].expected_date,
            duration=predict_record[0].expected_duration,
            organization=predict_record[0].organization,
            year=predict_record[0].unom.COL_756,
            warn=predict_record[0].unom.COL_770,
            materialRoof=predict_record[0].unom.COL_781,
            materialWall=predict_record[0].unom.COL_769,
            fond=predict_record[0].unom.COL_2463,
            mkd=predict_record[0].unom.COL_103506,
            statusMkd=predict_record[0].unom.COL_3243,

        )
        return response

    async def update_item_by_unom_id(self, unom_id: int, item_update):
        to_update = {}
        dict_item_update = item_update.dict(exclude_none=True)
        for key in dict_item_update:
            to_update[MAPPED_PREDICT_EVENT_FIELDS[key]] = dict_item_update[key]
        query = update(PredictedEventModel).values(**to_update)
        await self._session.execute(query)
        await self._session.commit()
        updated_item = await self.get_item_predict_event_by_unom_id(unom_id)
        return updated_item
