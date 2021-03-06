"""empty message

Revision ID: 5cb54e413f00
Revises: 08e0a120640a
Create Date: 2020-04-29 20:55:30.133295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5cb54e413f00'
down_revision = '08e0a120640a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###

    op.execute('UPDATE todos SET completed = False WHERE completed IS NULL;')
    op.alter_column('todos', 'completed', nullable=False)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
