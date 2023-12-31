"""empty message

Revision ID: 55d0e157d588
Revises: a2340884a7c7
Create Date: 2023-10-28 01:20:48.198783

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision: str = '55d0e157d588'
down_revision: Union[str, None] = 'a2340884a7c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles_to_institutions', sa.Column('active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profiles_to_institutions', 'active')
    # ### end Alembic commands ###
