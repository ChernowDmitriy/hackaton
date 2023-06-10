import sqlalchemy as sa
from sqlalchemy.orm import relationship

from infrastructure.database import ORMBaseModel


class ApartmentBuildingsWithTEC(ORMBaseModel):
    """
    Apartment buildings with technical and economic characteristics
    Многоквартирные дома с технико-экономическими характеристиками
    """

    __tablename__ = 'ApartmentBuildingsWithTEC'

    ID = sa.Column(sa.Integer, primary_key=True, index=True, unique=True)

    NAME = sa.Column(sa.String)
    PARENT_ID = sa.Column(sa.Integer, nullable=True)
    LOGIN = sa.Column(sa.String)

    COL_754 = sa.Column(sa.String, nullable=True)
    COL_755 = sa.Column(sa.String, nullable=True)
    COL_756 = sa.Column(sa.SmallInteger, nullable=True)
    COL_757 = sa.Column(sa.SmallInteger, nullable=True)
    COL_758 = sa.Column(sa.Integer, nullable=True)
    COL_759 = sa.Column(sa.SmallInteger, nullable=True)
    COL_760 = sa.Column(sa.SmallInteger, nullable=True)
    COL_761 = sa.Column(sa.SmallInteger, nullable=True)
    COL_762 = sa.Column(sa.Integer, nullable=True)
    COL_763 = sa.Column(sa.Integer, nullable=True)
    COL_764 = sa.Column(sa.Integer, nullable=True)
    COL_765 = sa.Column(sa.SmallInteger, nullable=True)
    COL_766 = sa.Column(sa.SmallInteger, nullable=True)
    COL_767 = sa.Column(sa.String, nullable=True)
    COL_769 = sa.Column(sa.Integer, nullable=True)
    COL_770 = sa.Column(sa.Integer, nullable=True)
    COL_771 = sa.Column(sa.SmallInteger, nullable=True)
    COL_772 = sa.Column(sa.SmallInteger, nullable=True)
    COL_775 = sa.Column(sa.Integer, nullable=True)
    COL_781 = sa.Column(sa.Integer, nullable=True)
    COL_782 = sa.Column(sa.Integer, primary_key=True, unique=True)
    COL_2156 = sa.Column(sa.String, nullable=True)
    COL_2463 = sa.Column(sa.Integer, nullable=True)
    COL_3163 = sa.Column(sa.Integer, nullable=True)
    COL_3243 = sa.Column(sa.Integer, nullable=True)
    COL_3363 = sa.Column(sa.SmallInteger, nullable=True)
    COL_3468 = sa.Column(sa.String)
    COL_103506 = sa.Column(sa.String)

    district_id = sa.Column(sa.Integer, sa.ForeignKey('districs.ID'), nullable=True)
    district = relationship('District', backref='ApartmentBuildingsWithTEC')
