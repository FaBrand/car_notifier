from app import app, car_model
from flask import render_template, redirect, url_for, flash

@app.route('/')
@app.route('/index')
def index():
    return render_template('car_overview.html', selector=car_model.car_selector)


@app.route('/reload')
def reload():
    try:
        connector = car_model.BmwRent()
        connector.login()
        connector.load_data()
        connector.write_to_file()
        car_model.car_selector.load_from_file()
        car_model.car_selector.read_cars()
    except Exception as e:
        flash('Error during reload: {}'.format(e))
    return render_template('car_overview.html', selector=car_model.car_selector)

