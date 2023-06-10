import sqlalchemy as sa

from infrastructure.database import ORMBaseModel


class EventsTypesRegisteredByTheObject(ORMBaseModel):
    """
    Типы событий регистрируемых по типу объекта многоквартирный дом
    """

    __tablename__ = 'EventsTypesRegisteredByTheObject'

    ID = sa.Column(sa.Integer, primary_key=True, index=True, unique=True)

    name = sa.Column(sa.String)
    system = sa.Column(sa.String)
