from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.domains import PredictedEvent as PredictedEventModel, ApartmentBuildingsWithTEC


class PredictEventRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_list_events(self):
        query = select(PredictedEventModel).options(selectinload(PredictedEventModel.unom)).join(
            ApartmentBuildingsWithTEC, PredictedEventModel.unom_id == ApartmentBuildingsWithTEC.unom)
        result = await self._session.execute(query)
        predict_record = result.scalars().all()
        return predict_record
