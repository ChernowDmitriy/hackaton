import datetime
import typing

from pydantic import BaseModel


class PredictedMajorRepairs(BaseModel):
    unom: typing.Optional[int]
    # type: typing.Optional[str]
    date: typing.Optional[datetime.datetime]  # Ожидаемая дата починки
    duration: typing.Optional[str]  # Ожидаемая продолжительность выполнения
    year: typing.Optional[int]
    warn: typing.Optional[str]  # Признак аварийности
    materialRoof: typing.Optional[str]
    materialWall: typing.Optional[str]
    fond: typing.Optional[str]
    mkd: typing.Optional[str]
    statusMkd: typing.Optional[str]
