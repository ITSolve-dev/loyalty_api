import sqlalchemy as sa
import sqlalchemy.orm

from db.models import DateTimeMixin
from db import Base


class Institution(Base, DateTimeMixin):
    __tablename__ = "institutions"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, unique=True)
    name = sa.Column(sa.String(255), nullable=False)

    type_id = sa.Column(sa.ForeignKey("institution_types.id"), nullable=False)
    type = sa.orm.relationship("InstitutionType", back_populates="institution", lazy="selectin")

    members = sa.orm.relationship(
        "ProfileToInstitution", back_populates="institution", lazy="joined"
    )

    customer_tickets = sa.orm.relationship("LoyaltyTicket", back_populates="institution", lazy="joined")
