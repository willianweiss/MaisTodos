import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "7be94db97e67"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "credit_card",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("exp_date", sa.DateTime(), nullable=False),
        sa.Column("holder", sa.String(), nullable=False),
        sa.Column("number", sa.String(), nullable=False, unique=True),
        sa.Column("cvv", sa.String(), nullable=True),
        sa.Column("brand", sa.String(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
        ),
    )


def downgrade() -> None:
    op.drop_table("credit_card")
