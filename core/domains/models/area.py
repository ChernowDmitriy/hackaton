import sqlalchemy as sa

from infrastructure.database import ORMBaseModel


class Area(ORMBaseModel):
    __tablename__ = 'areas'

    ID = sa.Column(sa.Integer, primary_key=True, index=True, unique=True)
    name = sa.Column(sa.String)
