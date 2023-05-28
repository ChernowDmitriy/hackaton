import sqlalchemy as sa

from infrastructure.database import ORMBaseModel


class EventsTypesRegisteredByTheObject(ORMBaseModel):
    """
    Типы событий регистрируемых по типу объекта многоквартирный дом
    """

    __tablename__ = 'EventsTypesRegisteredByTheObject'

    name = sa.Column(sa.String)
    system = sa.Column(sa.String)
