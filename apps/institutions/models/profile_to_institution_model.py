import sqlalchemy as sa
import sqlalchemy.orm

from db import Base
from db.models import DateTimeMixin


class ProfileToInstitution(Base, DateTimeMixin):
    __tablename__ = "profiles_to_institutions"

    id = sa.Column(sa.Integer, primary_key=True, unique=True, autoincrement=True)

    institution_id = sa.Column(sa.ForeignKey("institutions.id"), nullable=False)
    institution = sa.orm.relationship("Institution", back_populates="members", lazy='joined')

    profile_id = sa.Column(sa.ForeignKey("profiles.id"), nullable=False)
    profile = sa.orm.relationship("Profile", back_populates="institutions", lazy='joined')

    active = sa.Column(sa.Boolean, default=True)
