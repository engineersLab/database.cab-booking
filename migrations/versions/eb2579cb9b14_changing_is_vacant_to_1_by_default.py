"""changing is_vacant to 1 by default

Revision ID: eb2579cb9b14
Revises: 929db15e1274
Create Date: 2022-03-08 11:41:14.566935

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


# revision identifiers, used by Alembic.
revision = 'eb2579cb9b14'
down_revision = '929db15e1274'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cab', 'is_vacant',
               existing_type=mysql.INTEGER,
               server_default='1')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
