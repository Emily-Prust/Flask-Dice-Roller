"""empty message

Revision ID: cd4a3c5489a0
Revises: 7912ed27784a
Create Date: 2025-03-08 23:35:59.974866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd4a3c5489a0'
down_revision = '7912ed27784a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roll', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timestamp', sa.DateTime(), nullable=False))
        batch_op.drop_index('ix_roll_note')
        batch_op.create_index(batch_op.f('ix_roll_note'), ['note'], unique=False)
        batch_op.create_index(batch_op.f('ix_roll_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roll', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_roll_timestamp'))
        batch_op.drop_index(batch_op.f('ix_roll_note'))
        batch_op.create_index('ix_roll_note', ['note'], unique=1)
        batch_op.drop_column('timestamp')

    # ### end Alembic commands ###
