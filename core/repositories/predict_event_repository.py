from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.domains import PredictedEvent as PredictedEventModel


class PredictEventRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_list_events(self) -> List[PredictedEventModel]:
        result = await self._session.execute(select(PredictedEventModel))
        predict_record = result.scalars().all()
        return predict_record
