"""empty message

Revision ID: 67d5e67352f3
Revises: 3553325d359b
Create Date: 2023-10-28 13:41:42.821559

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '67d5e67352f3'
down_revision: Union[str, None] = '3553325d359b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles')
    op.add_column('profiles', sa.Column('role', sa.Enum('DEVELOPER', 'EMPLOYEE', 'OWNER', 'CUSTOMER', name='roletype'), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profiles', 'role')
    op.create_table('roles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('type', postgresql.ENUM('DEVELOPER', 'EMPLOYEE', 'OWNER', 'CUSTOMER', name='roletype'), autoincrement=False, nullable=False),
    sa.Column('profile_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], name='roles_profile_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='roles_pkey'),
    sa.UniqueConstraint('id', name='roles_id_key')
    )
    # ### end Alembic commands ###