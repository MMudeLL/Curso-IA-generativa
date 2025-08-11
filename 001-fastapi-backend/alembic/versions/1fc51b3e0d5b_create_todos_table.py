"""create todos table

Revision ID: 1fc51b3e0d5b
Revises: ad1c380734f8
Create Date: 2025-08-09 13:19:33.629506

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1fc51b3e0d5b'
down_revision: Union[str, None] = 'ad1c380734f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
