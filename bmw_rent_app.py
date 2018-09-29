from app import app
from app.model import *


@app.shell_context_processor
def make_shell_context():
    return {
            'BmwRent': BmwRent,
            'Car': Car,
            'CarSelector': CarSelector,
            }

