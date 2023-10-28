import sqlalchemy as sa
import sqlalchemy.orm

from db import Base
from db.models import DateTimeMixin


class User(Base, DateTimeMixin):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, unique=True)
    telegram_id = sa.Column(sa.Integer, unique=True, nullable=False)
    username = sa.Column(sa.String(64), nullable=True, default=None)
    first_name = sa.Column(sa.String(64), nullable=False)

    profiles = sa.orm.relationship("Profile", back_populates="user")
