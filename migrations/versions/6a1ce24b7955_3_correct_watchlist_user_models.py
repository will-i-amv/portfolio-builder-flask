"""3_correct_watchlist_user_models

Revision ID: 6a1ce24b7955
Revises: fe0e176c3581
Create Date: 2023-09-08 12:43:40.302743

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6a1ce24b7955'
down_revision = 'fe0e176c3581'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('watchlist_items', schema=None) as batch_op:
        batch_op.drop_constraint('watchlist_items_ibfk_1', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('watchlist_items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('watchlist_items_ibfk_1', 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###
