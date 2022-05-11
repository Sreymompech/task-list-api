"""remove relationship between goal and task

Revision ID: 454c31399826
Revises: 0cbf89089d6d
Create Date: 2022-05-08 23:31:41.622911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '454c31399826'
down_revision = '0cbf89089d6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('task_goal_id_fkey', 'task', type_='foreignkey')
    op.drop_column('task', 'goal_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('goal_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('task_goal_id_fkey', 'task', 'goal', ['goal_id'], ['id'])
    # ### end Alembic commands ###