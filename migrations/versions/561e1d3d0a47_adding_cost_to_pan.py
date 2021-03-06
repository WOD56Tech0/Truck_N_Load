"""adding cost to Pan

Revision ID: 561e1d3d0a47
Revises: 3718e72dbfe7
Create Date: 2018-06-04 11:01:37.059569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '561e1d3d0a47'
down_revision = '3718e72dbfe7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pan', sa.Column('Cost', sa.Numeric(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pan', 'Cost')
    # ### end Alembic commands ###
