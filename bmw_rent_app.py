from app import app, db
from app.model import CarEntry, Booking, CarDescription
from app.car_model import *


@app.shell_context_processor
def make_shell_context():
    connector = BmwRent()
    connector.login()
    return {
            'con': connector,
            'Car': Car,
            'CarSelector': CarSelector,
            'CarDescription': CarDescription,
            'CarEntry': CarEntry,
            'Booking': Booking,
            'db' : db,
           }


