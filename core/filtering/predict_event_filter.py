from typing import Optional

from pydantic import BaseModel


class PredictEventFiltering(BaseModel):
    unom: Optional[int]
    type: Optional[str]
    address: Optional[str]
    project_series: Optional[str]
    area: Optional[str]
    district: Optional[str]
    start_construction_year: Optional[str]
    end_construction_year: Optional[str]
    start_expected_duration: Optional[int]
    end_expected_duration:  Optional[int]
    warn: Optional[str]  # Признак аварийности
    mkd: Optional[str]
    statusMkd: Optional[str]
