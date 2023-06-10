import datetime

import sqlalchemy as sa

from infrastructure.database import ORMBaseModel


class IncidentsRegisteredAtMunicipalFacilities(ORMBaseModel):
    """
    Incidents registered at municipal facilities
    Инциденты зарегистрированные на объектах городского хозяйства
    """

    __tablename__ = 'IncidentsRegisteredAtMunicipalFacilities'

    ID = sa.Column(sa.Integer, primary_key=True, index=True, unique=True)

    name = sa.Column(sa.String)
    source = sa.Column(sa.String)
    created_at_in_the_external_system = sa.Column(sa.DateTime, default=datetime.datetime.now())
    closed_at = sa.Column(sa.DateTime)
    district = sa.Column(sa.String)
    address = sa.Column(sa.String)
    date_and_time_complete_event = sa.Column(sa.DateTime)
