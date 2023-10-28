import sqlalchemy as sa
import sqlalchemy.orm

from db import Base


class InstitutionType(Base):
    __tablename__ = "institution_types"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, unique=True)
    type = sa.Column(sa.String(64), nullable=False)

    institution = sa.orm.relationship("Institution", back_populates="type")
