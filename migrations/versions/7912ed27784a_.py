"""empty message

Revision ID: 7912ed27784a
Revises: 
Create Date: 2025-03-06 22:49:00.947932

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7912ed27784a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roll',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('note', sa.String(length=64), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('dice_number', sa.Integer(), nullable=False),
    sa.Column('roll_result', sa.String(length=999), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('roll', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_roll_note'), ['note'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roll', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_roll_note'))

    op.drop_table('roll')
    # ### end Alembic commands ###
