import sqlalchemy as sa
from typing import Optional

from db.orm import start_session

from ..schemas import CreateInstitutionTypeSchema, RetrieveInstitutionTypeSchema
from .interface_institution_type_repo import IInstitutionTypeRepo


class DefaultInstitutionTypeRepo(IInstitutionTypeRepo):
    async def create(
        self, data: CreateInstitutionTypeSchema
    ) -> Optional[RetrieveInstitutionTypeSchema]:
        async with start_session(self.db_session) as session:
            query = sa.insert(self.table).values(**data.model_dump()).returning(self.table)

            institution = await session.scalar(query)
            return RetrieveInstitutionTypeSchema.model_validate(institution)
