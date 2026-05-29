"""input table column

Revision ID: 4251007e58b8
Revises: 2a5a42542aaa
Create Date: 2026-05-29 16:50:30.215106

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4251007e58b8'
down_revision: Union[str, Sequence[str], None] = '2a5a42542aaa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
