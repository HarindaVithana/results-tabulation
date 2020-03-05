"""empty message

Revision ID: 5f61093c9695
Revises: ab9d4f52637d
Create Date: 2020-03-03 21:29:02.871678

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5f61093c9695'
down_revision = 'ab9d4f52637d'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('election_invalidVoteCategory', sa.Column('invalidVoteCategoryType', sa.String(length=50), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('election_invalidVoteCategory', 'invalidVoteCategoryType')
    ### end Alembic commands ###
