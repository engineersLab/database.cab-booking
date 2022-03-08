"""Initial migration.

Revision ID: 69d333559748
Revises: 
Create Date: 2022-03-04 15:20:44.199215

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '69d333559748'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('admin_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('admin_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('cab_type',
    sa.Column('type_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('type_id')
    )
    op.create_table('developer_type',
    sa.Column('type_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('type_id')
    )
    op.create_table('cab',
    sa.Column('cab_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('reg_no', sa.String(length=40), nullable=False),
    sa.Column('is_vacant', sa.Integer(), nullable=False),
    sa.Column('reserved_for', sa.String(length=10), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('date_created', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['type_id'], ['cab_type.type_id'], ),
    sa.PrimaryKeyConstraint('cab_id')
    )
    op.create_table('developer',
    sa.Column('developer_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('date_created', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['type_id'], ['developer_type.type_id'], ),
    sa.PrimaryKeyConstraint('developer_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('booking',
    sa.Column('booking_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cab_id', sa.Integer(), nullable=False),
    sa.Column('developer_id', sa.Integer(), nullable=False),
    sa.Column('date_created', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['cab_id'], ['cab.cab_id'], ),
    sa.ForeignKeyConstraint(['developer_id'], ['developer.developer_id'], ),
    sa.PrimaryKeyConstraint('booking_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('booking')
    op.drop_table('developer')
    op.drop_table('cab')
    op.drop_table('developer_type')
    op.drop_table('cab_type')
    op.drop_table('admin')
    # ### end Alembic commands ###