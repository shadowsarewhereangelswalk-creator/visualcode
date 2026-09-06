from alembic import op
import sqlalchemy as sa


revision = "20270430_01"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "solicitud",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nombre", sa.String(length=80), nullable=False),
        sa.Column("correo", sa.String(length=120), nullable=False),
        sa.Column("servicio", sa.String(length=40), nullable=False),
        sa.Column("mensaje", sa.Text(), nullable=False),
        sa.Column("estado", sa.String(length=20), nullable=False),
        sa.Column("creada_en", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_solicitud_correo"), "solicitud", ["correo"], unique=False)
    op.create_index(op.f("ix_solicitud_estado"), "solicitud", ["estado"], unique=False)
    op.create_index(op.f("ix_solicitud_servicio"), "solicitud", ["servicio"], unique=False)


def downgrade():
    op.drop_index(op.f("ix_solicitud_servicio"), table_name="solicitud")
    op.drop_index(op.f("ix_solicitud_estado"), table_name="solicitud")
    op.drop_index(op.f("ix_solicitud_correo"), table_name="solicitud")
    op.drop_table("solicitud")
