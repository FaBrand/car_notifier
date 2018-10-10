from app import app, car_model, db
from flask import render_template, redirect, url_for, flash
from app.model import CarDescription, CarEntry, Booking

@app.route('/')
@app.route('/index')
def index():
    cars = CarEntry.query.all()
    return render_template('car_overview.html', cars=cars)

def updateDatabase(Entry, new_list):
    current_entries = {Entry.FromJson(js) for js in new_list}
    entries_in_db = set(Entry.query.all())

    new_entries = current_entries - entries_in_db
    deleted_entries = entries_in_db - current_entries

    db.session.add_all(new_entries)
    for e in deleted_entries:
        db.session.delete(e)

    return (new_entries, deleted_entries)

@app.route('/reload')
def reload():
    try:
        connector = car_model.BmwRent()
        connector.login()
        connector.load_data()

        new_cars, deleted_cars = updateDatabase(CarEntry, connector.car_list['rentObjects'])
        new_descriptions, deleted_descriptions = updateDatabase(CarDescription, connector.car_description)
        new_bookings, deleted_bookins = updateDatabase(Booking, connector.car_list['rentObjTransacts'])

        db.session.commit()

        if new_descriptions:
            flash('Added {} new descriptions'.format(len(new_descriptions)))
        else:
            flash('Now new descriptions found')

        if new_cars:
            flash('Added {} new car objects'.format(len(new_cars)))
        else:
            flash('No new cars found')

        if new_bookings:
            flash('Added {} new bookings'.format(len(new_bookings)))
        else:
            flash('No new bookings found')

    except Exception as e:
        raise e
        flash('Error during reload: {}'.format(e))
    return redirect(url_for('index'))

