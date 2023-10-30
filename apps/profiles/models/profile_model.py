import sqlalchemy as sa
import sqlalchemy.orm

from db import Base
from db.models import DateTimeMixin

from apps.scans.models import Scan

from ..entities import RoleType


class Profile(Base, DateTimeMixin):
    __tablename__ = "profiles"

    id = sa.Column(sa.Integer, primary_key=True, unique=True, autoincrement=True)

    user_id = sa.Column(sa.ForeignKey("users.id"), nullable=False)
    user = sa.orm.relationship("User", back_populates="profiles", lazy="selectin")

    role = sa.Column(sa.Enum(RoleType), default=RoleType.CUSTOMER, nullable=False)

    institutions = sa.orm.relationship(
        "ProfileToInstitution", back_populates="profile", lazy="joined"
    )

    tickets = sa.orm.relationship("LoyaltyTicket", back_populates="profile", lazy="selectin")

    # scans = sa.orm.relationship(
    #     "Profile", secondary="Scan", lazy="joined", primaryjoin=(Scan.subject_profile_id == id)
    # )
