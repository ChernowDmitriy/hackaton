import sqlalchemy as sa
from sqlalchemy.orm import relationship

from infrastructure.database import ORMBaseModel


class District(ORMBaseModel):
    __tablename__ = 'districs'

    ID = sa.Column(sa.Integer, primary_key=True, index=True, unique=True)
    name = sa.Column(sa.String)

    area_id = sa.Column(sa.Integer, sa.ForeignKey('areas.ID'))
    area = relationship('Area', backref='districs')
