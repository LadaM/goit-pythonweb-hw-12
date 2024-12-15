"""Add avatar column to User model

Revision ID: 88af5919d373
Revises: dea08fd90d1c
Create Date: 2024-12-15 18:11:02.495424

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88af5919d373'
down_revision: Union[str, None] = 'dea08fd90d1c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar')
    # ### end Alembic commands ###
