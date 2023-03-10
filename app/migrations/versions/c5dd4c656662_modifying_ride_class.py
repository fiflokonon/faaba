"""Modifying Ride Class

Revision ID: c5dd4c656662
Revises: 5580d1d4afa8
Create Date: 2023-03-02 13:30:39.691113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5dd4c656662'
down_revision = '5580d1d4afa8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rides', schema=None) as batch_op:
        batch_op.add_column(sa.Column('boardingLocation', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rides', schema=None) as batch_op:
        batch_op.drop_column('boardingLocation')

    # ### end Alembic commands ###
