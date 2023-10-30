import sqlalchemy as sa
import sqlalchemy.orm

from db import Base
from db.models import DateTimeMixin


class LoyaltyTicket(Base, DateTimeMixin):
    __tablename__ = "loyalty_tickets"

    id = sa.Column(sa.Integer, primary_key=True)

    profile_id = sa.Column(sa.ForeignKey("profiles.id"), nullable=False)
    profile = sa.orm.relationship("Profile", back_populates="tickets", lazy="selectin")

    institution_id = sa.Column(sa.ForeignKey("institutions.id"), nullable=False)
    institution = sa.orm.relationship(
        "Institution", back_populates="customer_tickets", lazy="selectin"
    )

    activated = sa.Column(sa.Boolean, default=False)

    scans = sa.orm.relationship("Scan", back_populates="loyalty_ticket", lazy="selectin")
