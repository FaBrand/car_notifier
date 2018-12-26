from app import app, car_model, db
from flask import render_template, redirect, url_for, flash, jsonify, request
from app.model import CarDescription, CarEntry, Booking, CarImage, Watch
from app.schemas import *


@app.route('/')
@app.route('/index')
def index():
    cars = CarEntry.query.order_by(CarEntry.PS.desc()).all()
    return render_template('car_overview.html', cars=cars, watches=Watch.query.all())

def updateDatabase(Entry, new_list):
    current_entries = {Entry.FromJson(js) for js in new_list}
    entries_in_db = set(Entry.query.all())

    new_entries = current_entries - entries_in_db
    deleted_entries = entries_in_db - current_entries

    db.session.add_all(new_entries)
    for e in deleted_entries:
        db.session.delete(e)

    return (new_entries, deleted_entries)

@app.route('/view/<car_id>')
def view(car_id):
    car = CarEntry.query.filter(CarEntry.Id==car_id).first()
    if car:
        return render_template('car_view.html',car=car, watches=Watch.query.all())
    else:
        flash('Link is invalid')
        return redirect(url_for('index'))

@app.route('/watch/<car_id>')
def watch(car_id):
    car = CarEntry.query.filter(CarEntry.Id==car_id).first()
    if car:
        watch = Watch.query.filter(Watch.car_id==car.Id).first()
        if not watch:
            new_watch = Watch(car=car)
            db.session.add(new_watch)
            db.session.commit()
            flash('Now watching {}'.format(car.description.shortDescr))
        else:
            flash('Already watching {}'.format(car.description.shortDescr))
        return redirect(url_for('view', car_id=car.Id))
    else:
        flash('Link is invalid')
        return redirect(url_for('index'))

@app.route('/unwatch/<car_id>')
def unwatch(car_id):
    car = CarEntry.query.filter(CarEntry.Id==car_id).first()
    if car:
        watches = car.watches
        if watches:
            db.session.delete(watches[0])
            db.session.commit()
            flash('Not watching {} anymore'.format(car.description.shortDescr))
        else:
            flash('Not watching {} already'.format(car.description.shortDescr))

        return redirect(url_for('view', car_id=car.Id))
    else:
        flash('Link is invalid')
        return redirect(url_for('index'))

@app.route('/watchlist')
def watchlist():
    cars = [w.car for w in Watch.query.all()]
    return render_template('car_overview.html', cars=cars, watches=Watch.query.all())

@app.route('/check')
def check():
    try:
        connector = car_model.BmwRent()
        connector.login()
        connector.load_data()

        updateDatabase(CarImage,connector.vehicle_detail_data)
        new_descriptions, deleted_descriptions = updateDatabase(CarDescription, connector.car_description)
        new_cars, deleted_cars = updateDatabase(CarEntry, connector.car_list)
        existing_car_ids = {c.Id for c in CarEntry.query.all()}
        new_bookings, deleted_bookings = updateDatabase(Booking, connector.bookings)

        # Remove bookings that refer to an invalid car id
        for inconsistent in {bkg for bkg in new_bookings if bkg.ResourceId not in existing_car_ids}:
            db.session.expunge(inconsistent)

        for dc in deleted_cars:
            if dc.watches:
                db.session.delete(dc.watches[0])
        db.session.commit()

        if new_descriptions:
            flash('Added {} new descriptions'.format(len(new_descriptions)))

        if new_cars:
            flash('Added {} new car objects'.format(len(new_cars)))

        if new_bookings:
            flash('Added {} new bookings'.format(len(new_bookings)))

    except Exception as e:
        raise e
        flash('Error during reload: {}'.format(e))
    return redirect(url_for('index'))

@app.route('/api')
def api():
    return redirect(url_for('api_v1'))

@app.route('/api/v1')
def api_v1():
    return jsonify({'status': True})

@app.route('/api/v1/cars')
def cars_api():
    id = request.args.get('id')
    if id is None:
        all_cars = CarEntry.query.all()
        return car_entry_schemas.jsonify(all_cars)
    else:
        car = CarEntry.query.filter(CarEntry.Id==id).first()
        return car_entry_schema.jsonify(car)
