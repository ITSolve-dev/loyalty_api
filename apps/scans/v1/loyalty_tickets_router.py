from dependency_injector.wiring import inject, Provide
from fastapi import Depends

from core import VersionedAPIRouter, ErrorDetails

from ..cases import LoyaltyTicketsCases
from ..schemas import *

router = VersionedAPIRouter(
    v=1,
    prefix="/loyalty-tickets",
    tags=["loyalty tickets"],
    responses={404: {"model": ErrorDetails}},
)


@router.post("", response_model=RetrieveLoyaltyTicketSchema, operation_id="createLoyaltyTicket")
@inject
async def create_loyalty_ticket(
    data: CreateLoyaltyTicketSchema,
    loyalty_tickets_cases: LoyaltyTicketsCases = Depends(
        Provide["scans_app.loyalty_tickets_cases"]
    ),
):
    return await loyalty_tickets_cases.create(data=data)


@router.post(
    "/{ticket_id}", response_model=RetrieveLoyaltyTicketSchema, operation_id="getLoyaltyTicketById"
)
@inject
async def get_loyalty_ticket_by_id(
    ticket_id: int,
    loyalty_tickets_cases: LoyaltyTicketsCases = Depends(
        Provide["scans_app.loyalty_tickets_cases"]
    ),
):
    return await loyalty_tickets_cases.retrieve(id=ticket_id)


@router.post(
    "/{ticket_id}/activate",
    response_model=RetrieveLoyaltyTicketSchema,
    operation_id="activateLoyaltyTicket",
)
@inject
async def activate_loyalty_ticket(
    ticket_id: int,
    loyalty_tickets_cases: LoyaltyTicketsCases = Depends(
        Provide["scans_app.loyalty_tickets_cases"]
    ),
):
    return await loyalty_tickets_cases.activate_loyalty_ticket(id=ticket_id)
