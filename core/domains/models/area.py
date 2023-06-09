import sqlalchemy as sa

from infrastructure.database import ORMBaseModel


class Area(ORMBaseModel):
    __tablename__ = 'areas'

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.String)
