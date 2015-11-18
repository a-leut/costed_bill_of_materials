"""empty message

Revision ID: 4e4bcdc6efd
Revises: 492ff776cdf
Create Date: 2015-11-17 21:35:25.445996

"""

# revision identifiers, used by Alembic.
revision = '4e4bcdc6efd'
down_revision = '492ff776cdf'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cbom_row', schema=None) as batch_op:
        batch_op.add_column(sa.Column('MOQ', sa.Integer(), nullable=True))

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cbom_row', schema=None) as batch_op:
        batch_op.drop_column('MOQ')

    ### end Alembic commands ###