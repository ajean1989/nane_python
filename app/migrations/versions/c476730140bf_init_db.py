"""init db

Revision ID: c476730140bf
Revises: 1a964fe5d54c
Create Date: 2023-07-24 11:00:22.720850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c476730140bf'
down_revision = '1a964fe5d54c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('birthday', sa.DateTime(), nullable=False),
    sa.Column('gender', sa.Integer(), nullable=False),
    sa.Column('diet', sa.Integer(), nullable=False),
    sa.Column('statut', sa.Integer(), nullable=False),
    sa.Column('view', sa.Integer(), nullable=False),
    sa.Column('creation_date_user', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id_user'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###