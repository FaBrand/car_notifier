"""empty message

Revision ID: 081011088b0a
Revises: 
Create Date: 2018-10-15 23:09:42.162219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '081011088b0a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car_description',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shortDescr', sa.String(length=120), nullable=True),
    sa.Column('code', sa.String(length=120), nullable=True),
    sa.Column('wwwDescr', sa.String(length=120), nullable=True),
    sa.Column('ClassificationTypeId', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_car_description_code'), 'car_description', ['code'], unique=False)
    op.create_index(op.f('ix_car_description_shortDescr'), 'car_description', ['shortDescr'], unique=False)
    op.create_index(op.f('ix_car_description_wwwDescr'), 'car_description', ['wwwDescr'], unique=False)
    op.create_table('car_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('interieur', sa.String(length=1200), nullable=True),
    sa.Column('outside_large', sa.String(length=1200), nullable=True),
    sa.Column('outside_small', sa.String(length=1200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('car_entry',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('classificationId', sa.Integer(), nullable=True),
    sa.Column('carImageId', sa.Integer(), nullable=True),
    sa.Column('classificationGroupingId', sa.Integer(), nullable=True),
    sa.Column('Kilowatt', sa.Float(), nullable=True),
    sa.Column('stationId', sa.Integer(), nullable=True),
    sa.Column('classificationManufacturerTypeId', sa.Integer(), nullable=True),
    sa.Column('classificationManufacturerId', sa.Integer(), nullable=True),
    sa.Column('registrationNumber', sa.String(length=120), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('fuelType', sa.String(length=120), nullable=True),
    sa.Column('PS', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['carImageId'], ['car_image.id'], ),
    sa.ForeignKeyConstraint(['classificationId'], ['car_description.id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('booking',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('bufferCi', sa.DateTime(), nullable=True),
    sa.Column('ClassificationId', sa.Integer(), nullable=True),
    sa.Column('ResourceId', sa.Integer(), nullable=True),
    sa.Column('originCi', sa.DateTime(), nullable=True),
    sa.Column('CheckInStationId', sa.Integer(), nullable=True),
    sa.Column('bufferCo', sa.DateTime(), nullable=True),
    sa.Column('serviceCi', sa.DateTime(), nullable=True),
    sa.Column('serviceCo', sa.DateTime(), nullable=True),
    sa.Column('EndDate', sa.DateTime(), nullable=True),
    sa.Column('StartDate', sa.DateTime(), nullable=True),
    sa.Column('originCo', sa.DateTime(), nullable=True),
    sa.Column('IsOwn', sa.Boolean(), nullable=True),
    sa.Column('CheckInPositionId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ResourceId'], ['car_entry.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('booking')
    op.drop_table('car_entry')
    op.drop_table('car_image')
    op.drop_index(op.f('ix_car_description_wwwDescr'), table_name='car_description')
    op.drop_index(op.f('ix_car_description_shortDescr'), table_name='car_description')
    op.drop_index(op.f('ix_car_description_code'), table_name='car_description')
    op.drop_table('car_description')
    # ### end Alembic commands ###