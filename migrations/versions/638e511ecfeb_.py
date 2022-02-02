"""empty message

Revision ID: 638e511ecfeb
Revises: 346c77fd08f2
Create Date: 2022-01-26 13:35:00.319935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '638e511ecfeb'
down_revision = '346c77fd08f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.drop_column('content')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_email'), ['email'])
        batch_op.create_unique_constraint(batch_op.f('uq_user_username'), ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_username'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_user_email'), type_='unique')

    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('content', sa.TEXT(), server_default=sa.text("'none'"), nullable=True))

    # ### end Alembic commands ###
