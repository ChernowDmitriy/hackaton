import datetime

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from infrastructure.database import ORMBaseModel


class PredictedEvent(ORMBaseModel):
    """
    Предсказанные события
    """

    __tablename__ = 'PredictedEvent'

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    unom_id = sa.Column(sa.Integer, sa.ForeignKey('ApartmentBuildingsWithTEC.unom'))
    unom = relationship('ApartmentBuildingsWithTEC', backref='PredictedEvent')

    name = sa.Column(sa.String)
    expected_date = sa.Column(sa.DateTime, default=datetime.datetime.now())
    expected_duration = sa.Column(sa.Integer)
    organization = sa.Column(sa.String)
