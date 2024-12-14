"""Add or remove verification_token column

Revision ID: e39a0497c7be
Revises: 75ea5018ad46
Create Date: 2024-12-14 11:15:26.454460

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e39a0497c7be'
down_revision: Union[str, None] = '75ea5018ad46'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('verification_token', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'verification_token')
    # ### end Alembic commands ###