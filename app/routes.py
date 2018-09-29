from app import app, model
from flask import render_template, redirect, url_for, flash

@app.route('/')
@app.route('/index')
def index():
    return render_template('car_overview.html', selector=model.car_selector)


@app.route('/reload')
def reload():
    try:
        connector = model.BmwRent()
        connector.login()
        connector.load_data()
        connector.write_to_file()
        model.car_selector.load_from_file()
        model.car_selector.read_cars()
    except Exception as e:
        flash('Error during reload: {}'.format(e))
    return render_template('car_overview.html', selector=model.car_selector)

