"""panCoordinator table

Revision ID: 0f1b344edc14
Revises: acc202c34e9e
Create Date: 2018-05-30 11:18:35.904576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f1b344edc14'
down_revision = 'acc202c34e9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pan_coordinator', sa.Column('delivery_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'pan_coordinator', 'delivery', ['delivery_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pan_coordinator', type_='foreignkey')
    op.drop_column('pan_coordinator', 'delivery_id')
    # ### end Alembic commands ###