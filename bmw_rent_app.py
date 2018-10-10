from app import app, db
from app.model import CarEntry, Booking, CarDescription
from app.car_model import *


@app.shell_context_processor
def make_shell_context():
    return {
            'js_desc' : { "id": "51277", "parentId": "3", "shortDescr": "BMW X6", "code": "BMW X6", "wwwDescr": "BMW X6", "ClassificationTypeId": "4" },
            'js_booking': { "bufferCi": "2018-10-01 11:00:00", "ClassificationId": "50721", "ResourceId": "196417", "originCi": "2018-10-01 10:00:00", "CheckInStationId": "50585", "bufferCo": "2018-09-03 09:00:00", "serviceCi": "2018-10-01 11:00:00", "serviceCo": "2018-09-03 10:00:00", "EndDate": "2018-10-01 11:00:00", "StartDate": "2018-09-03 09:00:00", "Id": "1623620", "originCo": "2018-09-03 10:00:00", "IsOwn": False, "CheckInPositionId": "0" },
            'js_car': { "classificationId": "51194", "classificationGroupingId": "50421", "specialType": "", "Kilowatt": "250.00", "specialPrice": "", "specialPeriod": "", "stationId": "50585", "maxDistanceValue": "0", "classificationManufacturerTypeId": "51193", "classificationManufacturerId": "723", "registrationNumber": "M-DT 3672", "price": "59.0000", "orderNo": "0", "specialwwwDescr": "", "objPositionId": None, "fuelType": "UP", "poolType": "", "PS": "340.00", "Id": "196580", "CO2Emission": "", "distanceGroupId": "" },
            'BmwRent': BmwRent,
            'Car': Car,
            'CarSelector': CarSelector,
            'CarDescription': CarDescription,
            'CarEntry': CarEntry,
            'Booking': Booking,
           }


