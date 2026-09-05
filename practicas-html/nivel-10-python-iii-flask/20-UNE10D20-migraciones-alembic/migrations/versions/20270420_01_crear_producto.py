from alembic import op
import sqlalchemy as sa


revision = "20270420_01"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "producto",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nombre", sa.String(length=100), nullable=False),
        sa.Column("precio", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("nombre"),
    )


def downgrade():
    op.drop_table("producto")
