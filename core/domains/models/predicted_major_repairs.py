import datetime

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from infrastructure.database import ORMBaseModel


class PredictedMajorRepairs(ORMBaseModel):
    """
    Предсказанния для кап. ремонтов
    """

    __tablename__ = 'PredictedMajorRepairs'

    ID = sa.Column(sa.Integer, primary_key=True, index=True, unique=True)
    unom_id = sa.Column(sa.Integer, sa.ForeignKey('ApartmentBuildingsWithTEC.COL_782'))
    unom = relationship('ApartmentBuildingsWithTEC', backref='PredictedMajorRepairs')

    name = sa.Column(sa.String)
    expected_date = sa.Column(sa.DateTime, default=datetime.datetime.now())
    expected_duration = sa.Column(sa.Integer)
