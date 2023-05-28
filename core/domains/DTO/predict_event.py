import datetime

from pydantic import BaseModel


class PredictEventSchemaOutput(BaseModel):
    class _ApartmentBuildingsWithTEC(BaseModel):
        id: int
        unom: int
        name: str
        parent_id: int
        login: str

        col_754: str
        col_755: str
        col_756: int
        col_757: int
        col_758: int
        col_759: int
        col_760: int
        col_761: int
        col_762: int
        col_763: int
        col_764: int
        col_765: int
        col_766: int
        col_767: str
        col_769: int
        col_770: int
        col_771: int
        col_772: int
        col_775: int
        col_781: int
        col_782: int

        col_2156: str
        col_2463: int
        col_3163: int
        col_3243: int
        col_3363: int
        col_3468: str
        col_103506: str

    id: int
    unom_id: int

    name: str
    expected_date: datetime.datetime
    expected_duration: int
    organization: str
    unom: _ApartmentBuildingsWithTEC
