"""empty message

Revision ID: a052e36d088f
Revises: 7168c0059d93
Create Date: 2020-01-16 17:12:42.452595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a052e36d088f'
down_revision = '7168c0059d93'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tallySheet_map',
    sa.Column('tallySheetMapId', sa.Integer(), nullable=False),
    sa.Column('pre_41_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('pre_34_co_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('ce_201_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('ce_201_pv_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('pre_30_pd_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('pre_34_i_ro_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('pre_34_pd_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('pre_30_ed_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('pre_34_ii_ro_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('pre_34_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('pre_34_ed_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('pre_all_island_ed_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('pre_all_island_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('pre_34_ai_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('pe_27_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('pe_4_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('pe_ce_ro_v1_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('pe_r1_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('pe_ce_ro_pr_1_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('pe_ce_ro_v2_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('pe_r2_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('pe_ce_ro_pr_2_tallySheetId', sa.Integer(), nullable=True),
    sa.Column('pe_ce_ro_pr_3_tallySheetId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ce_201_pv_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['ce_201_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pe_27_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pe_4_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pe_ce_ro_pr_1_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pe_ce_ro_pr_2_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pe_ce_ro_pr_3_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pe_ce_ro_v1_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pe_ce_ro_v2_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pe_r1_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pe_r2_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pre_30_ed_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pre_30_pd_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pre_34_ai_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pre_34_co_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pre_34_ed_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pre_34_i_ro_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pre_34_ii_ro_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pre_34_pd_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pre_34_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pre_41_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pre_all_island_ed_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.ForeignKeyConstraint(['pre_all_island_tallySheetId'], ['tallySheet.tallySheetId'], ),
    sa.PrimaryKeyConstraint('tallySheetMapId')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tallySheet_map')
    ### end Alembic commands ###