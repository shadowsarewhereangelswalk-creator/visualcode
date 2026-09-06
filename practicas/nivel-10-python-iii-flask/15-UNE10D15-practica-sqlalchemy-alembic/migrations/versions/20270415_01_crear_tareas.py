from alembic import op
import sqlalchemy as sa


revision = "20270415_01"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "tarea",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("titulo", sa.String(length=120), nullable=False),
        sa.Column("estado", sa.String(length=20), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("tarea")
