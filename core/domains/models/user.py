import sqlalchemy as sa

from infrastructure.database import ORMBaseModel


class User(ORMBaseModel):

    __tablename__ = 'users'

    email = sa.Column(sa.String)
    password = sa.Column(sa.String)

    first_name = sa.Column(sa.String)
    last_name = sa.Column(sa.String)
    middle_name = sa.Column(sa.String, nullable=True)

    is_active = sa.Column(sa.Boolean, default=True)
