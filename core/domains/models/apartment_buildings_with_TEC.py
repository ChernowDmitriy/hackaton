import sqlalchemy as sa

from infrastructure.database import ORMBaseModel


class ApartmentBuildingsWithTEC(ORMBaseModel):
    """
    Apartment buildings with technical and economic characteristics
    Многоквартирные дома с технико-экономическими характеристиками
    """

    __tablename__ = 'ApartmentBuildingsWithTEC'

    id = sa.Column(sa.Integer, primary_key=True, index=True, unique=True)
    unom = sa.Column(sa.Integer, primary_key=True, unique=True)

    name = sa.Column(sa.String)
    parent_id = sa.Column(sa.Integer, nullable=True)
    login = sa.Column(sa.String)

    col_754 = sa.Column(sa.String, nullable=True)
    col_755 = sa.Column(sa.String, nullable=True)
    col_756 = sa.Column(sa.SmallInteger, nullable=True)
    col_757 = sa.Column(sa.SmallInteger, nullable=True)
    col_758 = sa.Column(sa.Integer, nullable=True)
    col_759 = sa.Column(sa.SmallInteger, nullable=True)
    col_760 = sa.Column(sa.SmallInteger, nullable=True)
    col_761 = sa.Column(sa.SmallInteger, nullable=True)
    col_762 = sa.Column(sa.Integer, nullable=True)
    col_763 = sa.Column(sa.Integer, nullable=True)
    col_764 = sa.Column(sa.Integer, nullable=True)
    col_765 = sa.Column(sa.SmallInteger, nullable=True)
    col_766 = sa.Column(sa.SmallInteger, nullable=True)
    col_767 = sa.Column(sa.String, nullable=True)
    col_769 = sa.Column(sa.Integer, nullable=True)
    col_770 = sa.Column(sa.Integer, nullable=True)
    col_771 = sa.Column(sa.SmallInteger, nullable=True)
    col_772 = sa.Column(sa.SmallInteger, nullable=True)
    col_775 = sa.Column(sa.Integer, nullable=True)
    col_781 = sa.Column(sa.Integer, nullable=True)
    col_782 = sa.Column(sa.Integer, nullable=True)
    col_2156 = sa.Column(sa.String, nullable=True)
    col_2463 = sa.Column(sa.Integer, nullable=True)
    col_3163 = sa.Column(sa.Integer, nullable=True)
    col_3243 = sa.Column(sa.Integer, nullable=True)
    col_3363 = sa.Column(sa.SmallInteger, nullable=True)
    col_3468 = sa.Column(sa.String)
    col_103506 = sa.Column(sa.String)
