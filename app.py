from app import app, bmw_rent_app


@app.shell_context_processor
def make_shell_context():
    return {
            'BmwRent': BmwRent,
            'Car': Car,
            'CarSelector': CarSelector,
            }

