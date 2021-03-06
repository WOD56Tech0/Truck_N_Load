"""palletContent table

Revision ID: 15421191625d
Revises: e188498408d1
Create Date: 2018-05-13 00:08:44.538617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15421191625d'
down_revision = 'e188498408d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('palletContent',
    sa.Column('Pallet ID', sa.Integer(), nullable=False),
    sa.Column('Content ID', sa.Integer(), nullable=False),
    sa.Column('Content Type', sa.String(length=64), nullable=True),
    sa.Column('Quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Content ID'], ['content.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['Pallet ID'], ['pallet.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('Pallet ID', 'Content ID')
    )
    op.create_index(op.f('ix_palletContent_Content Type'), 'palletContent', ['Content Type'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_palletContent_Content Type'), table_name='palletContent')
    op.drop_table('palletContent')
    # ### end Alembic commands ###
