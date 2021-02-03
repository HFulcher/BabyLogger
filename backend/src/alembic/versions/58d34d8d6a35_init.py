"""init

Revision ID: 58d34d8d6a35
Revises: 
Create Date: 2021-02-03 20:08:55.360403

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = '58d34d8d6a35'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'entries',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('created_at', sa.DateTime,
                  default=datetime.utcnow(), index=True),
        sa.Column('notes', sa.String),
        sa.Column('dirty', sa.Boolean, default=False)
    )


def downgrade():
    pass
