from app import db
from datetime import datetime

def ToDateTime(raw):
    return datetime.strptime(raw, '%Y-%m-%d %H:%M:%S')

class CarDescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shortDescr = db.Column(db.String(120), index=True)
    code = db.Column(db.String(120), index=True)
    wwwDescr = db.Column(db.String(120), index=True)
    ClassificationTypeId = db.Column(db.Integer)

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    @classmethod
    def FromJson(cls, json):
        element = cls()
        element.id = int(json['id'])
        element.shortDescr = json['shortDescr']
        element.code = json['code']
        element.wwwDescr = json['wwwDescr']
        element.ClassificationTypeId = int(json['ClassificationTypeId'])
        return element

class CarEntry(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    classificationId = db.Column(db.Integer, db.ForeignKey('car_description.id'))
    description = db.relationship('CarDescription', uselist=False)
    classificationGroupingId = db.Column(db.Integer)
    Kilowatt = db.Column(db.Float)
    stationId = db.Column(db.Integer)
    classificationManufacturerTypeId = db.Column(db.Integer)
    classificationManufacturerId = db.Column(db.Integer)
    registrationNumber = db.Column(db.String(120))
    price = db.Column(db.Float)
    fuelType = db.Column(db.String(120))
    PS = db.Column(db.Float)
    bookings = db.relationship('Booking', backref='car')

    def __eq__(self, other):
        return self.Id == other.Id

    def __hash__(self):
        return hash(self.Id)

    @classmethod
    def FromJson(cls, json):
        element = cls()
        element.Id = int(json['Id'])
        element.classificationId = int(json['classificationId'])
        element.classificationGroupingId = int(json['classificationGroupingId'])
        element.Kilowatt = float(json['Kilowatt'])
        element.stationId = int(json['stationId'])
        element.classificationManufacturerTypeId = int(json['classificationManufacturerTypeId'])
        element.classificationManufacturerId = int(json['classificationManufacturerId'])
        element.registrationNumber = json['registrationNumber']
        element.price = float(json['price'])
        element.fuelType = json['fuelType']
        element.PS = float(json['PS'])
        return element

class Booking(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    bufferCi= db.Column(db.DateTime)
    ClassificationId = db.Column(db.Integer)
    ResourceId = db.Column(db.Integer, db.ForeignKey('car_entry.Id'))
    originCi= db.Column(db.DateTime)
    CheckInStationId = db.Column(db.Integer)
    bufferCo= db.Column(db.DateTime)
    serviceCi= db.Column(db.DateTime)
    serviceCo= db.Column(db.DateTime)
    EndDate= db.Column(db.DateTime)
    StartDate= db.Column(db.DateTime)
    originCo = db.Column(db.DateTime)
    IsOwn = db.Column(db.Boolean)
    CheckInPositionId = db.Column(db.Integer)

    def __eq__(self, other):
        return self.Id == other.Id

    def __hash__(self):
        return hash(self.Id)

    @classmethod
    def FromJson(cls, json):
        element = cls()
        element.Id = int(json['Id'])
        element.bufferCi = ToDateTime(json['bufferCi'])
        element.ClassificationId = json['ClassificationId']
        element.ResourceId = int(json['ResourceId'])
        element.originCi = ToDateTime(json['originCi'])
        element.CheckInStationId = int(json['CheckInStationId'])
        element.bufferCo = ToDateTime(json['bufferCo'])
        element.serviceCi = ToDateTime(json['serviceCi'])
        element.serviceCo = ToDateTime(json['serviceCo'])
        element.EndDate = ToDateTime(json['EndDate'])
        element.StartDate = ToDateTime(json['StartDate'])
        element.originCo = ToDateTime(json['originCo'])
        element.IsOwn = bool(json['IsOwn'])
        element.CheckInPositionId = int(json['CheckInPositionId'])
        return element

