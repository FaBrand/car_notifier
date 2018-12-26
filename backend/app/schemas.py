from app.model import *
from app import ma


class CarEntrySchema(ma.ModelSchema):
    class Meta:
        model = CarEntry

car_entry_schemas = CarEntrySchema(many=True)
car_entry_schema  = CarEntrySchema(many=False)


