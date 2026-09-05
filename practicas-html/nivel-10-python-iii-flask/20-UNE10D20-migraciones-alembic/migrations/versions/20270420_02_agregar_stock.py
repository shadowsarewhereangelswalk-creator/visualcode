from alembic import op
import sqlalchemy as sa


revision = "20270420_02"
down_revision = "20270420_01"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("producto") as lote:
        lote.add_column(sa.Column("stock", sa.Integer(), server_default="0", nullable=False))


def downgrade():
    with op.batch_alter_table("producto") as lote:
        lote.drop_column("stock")
