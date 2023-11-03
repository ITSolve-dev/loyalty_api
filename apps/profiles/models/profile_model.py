from typing import List, Optional, Sequence
from pprint import pformat

import sqlalchemy as sa
import sqlalchemy.orm

from db import Base
from db.models import DateTimeMixin
from apps.scans.models import LoyaltyTicket
from apps.institutions.models import Institution

from ..entities import RoleType
from ..exceptions import ProfilePermissionsDeniedException


class Profile(Base, DateTimeMixin):
    __tablename__ = "profiles"

    id = sa.Column(sa.Integer, primary_key=True, unique=True, autoincrement=True)

    user_id = sa.Column(sa.ForeignKey("users.id"), nullable=False)
    user = sa.orm.relationship("User", back_populates="profiles", lazy="selectin")

    role = sa.Column(sa.Enum(RoleType), default=RoleType.CUSTOMER, nullable=False)

    institutions = sa.orm.relationship(
        "ProfileToInstitution",
        back_populates="profile",
        lazy="selectin",
        order_by="desc(ProfileToInstitution.created_at)",
    )

    tickets = sa.orm.relationship("LoyaltyTicket", back_populates="profile", lazy="selectin")

    # scans = sa.orm.relationship(
    #     "Profile", secondary="Scan", lazy="joined", primaryjoin=(Scan.subject_profile_id == id)
    # )

    def __check_permission(self, roles: Sequence[RoleType], check_dev: bool = False):
        if self.role == RoleType.DEVELOPER and not check_dev:
            return
        if self.role not in roles:
            raise ProfilePermissionsDeniedException(
                ctx={"role": f"You role - {self.role} and allowed roles - {pformat(roles)}"}
            )

    @property
    def active_tickets(self) -> List[LoyaltyTicket]:
        self.__check_permission((RoleType.CUSTOMER, RoleType.OWNER))
        return list(filter(lambda ticket: not ticket.activated, self.tickets))

    @property
    def active_institution(self) -> Optional[Institution]:
        self.__check_permission((RoleType.EMPLOYEE,))
        return next((institution for institution in self.institutions if institution.active), None)

    def get_active_ticket_by_institution_id(self, institution_id: int) -> Optional[LoyaltyTicket]:
        self.__check_permission((RoleType.CUSTOMER, RoleType.OWNER))
        return next(
            (ticket for ticket in self.active_tickets if ticket.institution_id == institution_id),
            None,
        )
