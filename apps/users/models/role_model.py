import sqlalchemy as sa
import sqlalchemy.orm

from db import Base
from apps.users.entities import RoleType


class Role(Base):
    __tablename__ = "roles"
    id = sa.Column(sa.Integer, primary_key=True, unique=True, autoincrement=True)
    type = sa.Column(sa.Enum(RoleType), nullable=False)

    profile_id = sa.Column(sa.ForeignKey("profiles.id"), nullable=False)
    profile = sa.orm.relationship("Profile", back_populates="roles", lazy="selectin")
