"""add columns to crew members

Revision ID: 6241b7dd2230
Revises: b89128ce0be6
Create Date: 2023-07-07 13:14:12.353950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6241b7dd2230'
down_revision = 'b89128ce0be6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('crew_members', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('role', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('crew_members', schema=None) as batch_op:
        batch_op.drop_column('role')
        batch_op.drop_column('name')

    # ### end Alembic commands ###