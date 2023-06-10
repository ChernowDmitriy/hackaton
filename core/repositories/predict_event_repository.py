from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.domains import PredictedEvent as PredictedEventModel, ApartmentBuildingsWithTEC
from core.domains.DTO.predict_event import PredictEventSchemaOutput
from core.filtering.predict_event_filter import PredictEventFiltering


class PredictEventRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_list_events(self, filtering_fields: PredictEventFiltering):
        query = select(PredictedEventModel).options(selectinload(PredictedEventModel.unom)).join(
            ApartmentBuildingsWithTEC, PredictedEventModel.unom_id == ApartmentBuildingsWithTEC.unom)

        if filtering_fields.dict(exclude_none=True):
            if filtering_fields.unom:
                query = query.where(PredictedEventModel.unom_id == filtering_fields.unom)

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
            response = PredictEventSchemaOutput(
                unom=predict_record[0].unom_id,
                # type=predict_record
                date=predict_record[0].expected_date,
                duration=predict_record[0].expected_duration,
                organization=predict_record[0].organization,
                year=predict_record[0].unom.col_756,
                warn=predict_record[0].unom.col_770,
                materialRoof=predict_record[0].unom.col_781,
                materialWall=predict_record[0].unom.col_769,
                fond=predict_record[0].unom.col_2463,
                mkd=predict_record[0].unom.col_103506,
                statusMkd=predict_record[0].unom.col_3243,

            )
            return response

        return []

    async def get_item_predict_event_by_unom_id(self, unom_id: int):
        query = select(PredictedEventModel).options(selectinload(PredictedEventModel.unom)).join(
            ApartmentBuildingsWithTEC, PredictedEventModel.unom_id == ApartmentBuildingsWithTEC.unom)
        result = await self._session.execute(query)
        predict_record = result.scalars().all()
        if not predict_record:
            return []

        response = PredictEventSchemaOutput(
            unom=predict_record[0].unom_id,
            # type=predict_record
            date=predict_record[0].expected_date,
            duration=predict_record[0].expected_duration,
            organization=predict_record[0].organization,
            year=predict_record[0].unom.col_756,
            warn=predict_record[0].unom.col_770,
            materialRoof=predict_record[0].unom.col_781,
            materialWall=predict_record[0].unom.col_769,
            fond=predict_record[0].unom.col_2463,
            mkd=predict_record[0].unom.col_103506,
            statusMkd=predict_record[0].unom.col_3243,

        )
        return response
