"""empty message

Revision ID: 6c132b2e74c0
Revises: 67d5e67352f3
Create Date: 2023-10-29 20:30:43.607428

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '6c132b2e74c0'
down_revision: Union[str, None] = '67d5e67352f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('loyalty_tickets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=False),
    sa.Column('institution_id', sa.Integer(), nullable=False),
    sa.Column('activated', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['institution_id'], ['institutions.id'], ),
    sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('profiles', 'role',
               existing_type=postgresql.ENUM('DEVELOPER', 'EMPLOYEE', 'OWNER', 'CUSTOMER', name='roletype'),
               nullable=False)
    op.add_column('scans', sa.Column('loyalty_ticket_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'scans', 'loyalty_tickets', ['loyalty_ticket_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'scans', type_='foreignkey')
    op.drop_column('scans', 'loyalty_ticket_id')
    op.alter_column('profiles', 'role',
               existing_type=postgresql.ENUM('DEVELOPER', 'EMPLOYEE', 'OWNER', 'CUSTOMER', name='roletype'),
               nullable=True)
    op.drop_table('loyalty_tickets')
    # ### end Alembic commands ###
