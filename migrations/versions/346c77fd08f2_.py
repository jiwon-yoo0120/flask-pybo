"""empty message

Revision ID: 346c77fd08f2
Revises: 05b4066b48c0
Create Date: 2022-01-19 14:00:40.064932

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '346c77fd08f2'
down_revision = '05b4066b48c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.drop_column('answer', 'content')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('content', sa.TEXT(), server_default=sa.text("'none'"), nullable=True))
    op.drop_table('user')
    # ### end Alembic commands ###