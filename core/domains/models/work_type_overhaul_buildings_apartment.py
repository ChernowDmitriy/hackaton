import sqlalchemy as sa

from infrastructure.database import ORMBaseModel


class WorkTypeOverhaulBuildingApartment(ORMBaseModel):
    """
    Types of work on the overhaul of apartment buildings
    Виды работ по капитальному ремонту многоквартирных домов
    """

    __tablename__ = 'WorkTypeOverhaulBuildApart'

    ID = sa.Column(sa.Integer, primary_key=True, index=True, unique=True)

    code = sa.Column(sa.SmallInteger)
    name = sa.Column(sa.String)
    common_property_name = sa.Column(sa.String)
    work_type = sa.Column(sa.String)
    work_group = sa.Column(sa.String)
    work_alias = sa.Column(sa.String)
