from app.model import *
from app import ma

class CarDescriptionSchema(ma.ModelSchema):
    class Meta:
        model = CarDescription

class CarEntrySchema(ma.ModelSchema):
    class Meta:
        model = CarEntry
    description = ma.Nested(CarDescriptionSchema)

car_entry_schemas = CarEntrySchema(many=True)
car_entry_schema  = CarEntrySchema(many=False)


