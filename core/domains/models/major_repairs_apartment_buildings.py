import sqlalchemy as sa

from infrastructure.database import ORMBaseModel
from sqlalchemy.orm import relationship


class MajorRepairsApartmentBuilding(ORMBaseModel):
    """
    major repairs carried out in apartment buildings
    работы по капитальному ремонту проведенные в многоквартирных домах
    """

    __tablename__ = 'MajorRepairsApartmentBuilding'

    ID = sa.Column(sa.Integer, primary_key=True, index=True, unique=True)

    global_id = sa.Column(sa.Integer)
    period = sa.Column(sa.SmallInteger)
    work_name = sa.Column(sa.String)
    num_entrance = sa.Column(sa.SmallInteger)
    elevator_number = sa.Column(sa.SmallInteger)
    plan_date_start = sa.Column(sa.Date)
    plan_date_end = sa.Column(sa.Date)
    fact_date_start = sa.Column(sa.Date)
    fact_date_end = sa.Column(sa.Date)
    adm_area = sa.Column(sa.String)
    district = sa.Column(sa.String)
    address = sa.Column(sa.String)
    unom_id = sa.Column(sa.Integer, sa.ForeignKey('ApartmentBuildingsWithTEC.COL_782'))
    unom = relationship('ApartmentBuildingsWithTEC', backref='MajorRepairsApartmentBuilding')
