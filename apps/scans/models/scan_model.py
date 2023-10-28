import sqlalchemy as sa
import sqlalchemy.orm

from db import Base


class Scan(Base):
    __tablename__ = "scans"

    id = sa.Column(sa.Integer, primary_key=True, unique=True, autoincrement=True)

    amount = sa.Column(
        sa.Integer, sa.CheckConstraint("amount > 0"), server_default="1", nullable=True
    )

    object_profile_id = sa.Column(sa.ForeignKey("profiles.id"), nullable=False)
    object_profile = sa.orm.relationship(
        "Profile", lazy="joined", primaryjoin="Profile.id == Scan.object_profile_id"
    )

    subject_profile_id = sa.Column(sa.ForeignKey("profiles.id"), nullable=False)
    subject_profile = sa.orm.relationship(
        "Profile", lazy="joined", primaryjoin="Profile.id == Scan.subject_profile_id"
    )

    created_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.sql.func.now())

    @sa.orm.validates("amount")
    def validate_age(self, key, value):
        if value <= 0:
            raise ValueError(f"Invalid amount {value}")
        return value
