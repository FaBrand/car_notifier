"""empty message

Revision ID: 6206d96971f7
Revises: 081011088b0a
Create Date: 2018-10-16 00:23:26.345406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6206d96971f7'
down_revision = '081011088b0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('watch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('car_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['car_id'], ['car_entry.Id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('watch')
    # ### end Alembic commands ###
