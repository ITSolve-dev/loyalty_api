import sqlalchemy as sa
from dependency_injector.wiring import Provide, inject

from db.orm import start_session

from ..schemas import *
from .interface_scans_repo import IScansRepo
from .interface_loyalty_tickets_repo import ILoyaltyTicketsRepo
from ..exceptions import LoyaltyTicketsNotFoundException


class DefaultLoyaltyTicketsRepo(ILoyaltyTicketsRepo):
    @inject
    async def create(
        self,
        data: CreateLoyaltyTicketSchema,
        scans_repo: IScansRepo = Provide["scans_app.scans_repo"],
    ) -> RetrieveLoyaltyTicketSchema:
        async with start_session(self.db_session) as session:
            query = (
                sa.insert(self.table)
                .values(**data.model_dump(exclude={"scans"}))
                .returning(self.table.id)
            )
            ticket_id: int = await session.scalar(query)

        for scan in data.scans:
            await scans_repo.create(
                CreateScanSchema(**scan.model_dump(), loyalty_ticket_id=ticket_id)
            )
        return await self.retrieve(ticket_id)

    async def retrieve(self, id: int) -> RetrieveLoyaltyTicketSchema:
        async with start_session(self.db_session) as session:
            query = sa.select(self.table).where(self.table.id == id)
            ticket = await session.scalar(query)
            if not ticket:
                raise LoyaltyTicketsNotFoundException
        return RetrieveLoyaltyTicketSchema.model_validate(ticket)

    async def activate_ticket(self, id: int) -> RetrieveLoyaltyTicketSchema:
        async with start_session(self.db_session) as session:
            query = (
                sa.update(self.table)
                .where(self.table.id == id)
                .values(activated=True)
                .returning(self.table)
            )
            ticket = await session.scalar(query)
        return RetrieveLoyaltyTicketSchema.model_validate(ticket)
