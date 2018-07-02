"""Add routes table

Revision ID: bc8438517321
Revises: 
Create Date: 2018-07-02 21:44:33.759611

"""
from alembic import op
from geoalchemy2.types import Geometry
import sqlalchemy as sa
from sqlalchemy_utils import UUIDType

# revision identifiers, used by Alembic.
revision = 'bc8438517321'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "routes",
        sa.Column("id", UUIDType, primary_key=True),
        sa.Column("way_points", Geometry("LINESTRING")),
        sa.Column(
            "created_at",
            sa.DateTime,
            nullable=False,
            server_default=sa.func.now(),
        ),
    )


def downgrade():
    op.drop_table("routes")
