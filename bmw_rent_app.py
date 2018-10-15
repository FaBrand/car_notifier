from app import app, db
from app.model import CarEntry, Booking, CarDescription, CarImage
from app.car_model import *
from pprint import pprint


@app.shell_context_processor
def make_shell_context():
    connector = BmwRent()
    connector.login()
    return {
            'pprint': pprint,
            'con': connector,
            'Car': Car,
            'CarSelector': CarSelector,
            'CarDescription': CarDescription,
            'CarEntry': CarEntry,
            'CarImage': CarImage,
            'Booking': Booking,
            'db' : db,
           }


