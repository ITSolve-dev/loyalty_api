from typing import Optional

import sqlalchemy as sa
from sqlalchemy.orm import joinedload

from db.orm import start_session

from ..schemas import CreateMemberSchema, RetrieveMemberSchema
from .intreface_members_repo import IMembersRepo


class DefaultMemberRepo(IMembersRepo):
    async def create(self, data: CreateMemberSchema) -> Optional[RetrieveMemberSchema]:
        async with start_session(self.db_session) as session:
            query = sa.insert(self.table).values(**data.model_dump()).returning(self.table.id)
            member_id: int = await session.scalar(query)
        return await self.retrieve(member_id)

    async def retrieve(self, id: int) -> Optional[RetrieveMemberSchema]:
        async with start_session(self.db_session) as session:
            query = (
                sa.select(self.table)
                .options(joinedload(self.table.profile))
                # .options(joinedload(self.table.institution))
            )
            member = await session.scalar(query)
            return RetrieveMemberSchema.model_validate(member)
