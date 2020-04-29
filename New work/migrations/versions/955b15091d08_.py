"""empty message

Revision ID: 955b15091d08
Revises: 5d0aff1593fc
Create Date: 2020-04-29 12:03:18.570748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '955b15091d08'
down_revision = '5d0aff1593fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('parent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parent')
    op.drop_table('students')
    # ### end Alembic commands ###