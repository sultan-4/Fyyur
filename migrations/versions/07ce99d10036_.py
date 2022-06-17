"""empty message

Revision ID: 07ce99d10036
Revises: ff033119ae2c
Create Date: 2022-06-16 18:25:45.436150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07ce99d10036'
down_revision = 'ff033119ae2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Shows', sa.Column('show_id', sa.Integer(), nullable=True))
    op.drop_constraint('Shows_show_id_fkey', 'Shows', type_='foreignkey')
    op.create_foreign_key(None, 'Shows', 'Artist', ['show_id'], ['id'])
    op.drop_column('Shows', 'artist_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Shows', sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'Shows', type_='foreignkey')
    op.create_foreign_key('Shows_show_id_fkey', 'Shows', 'Artist', ['artist_id'], ['id'])
    op.drop_column('Shows', 'show_id')
    # ### end Alembic commands ###
