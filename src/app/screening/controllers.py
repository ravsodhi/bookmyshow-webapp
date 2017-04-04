from flask import Blueprint, request, session, jsonify, render_template,redirect
from app import db
from .models import Screening
from sqlalchemy import *
from app.movie.models import Movie

mod_screening = Blueprint('screening', __name__, url_prefix='/api')
'''
@mod_screening.route('/screening', methods=['GET'])
def page_displayer():
    movie_id = request.args.get('movie_id')
    return redirect("http://127.0.0.1:5000/movie/" + movie_id)
#    return render_template('screening.html', movie=movie)
'''

@mod_screening.route('/screening/movies', methods=['GET'])
def get_all_dates():
    id = request.args.get('movie_id')
    dates = Screening.query.filter(Screening.movie_id == id).all()
    new_dates = []

    for date in dates:
        new_dates.append(date.to_dict_dates())
    if dates is None:
        return jsonify(success=False), 404
    else:
        return jsonify(success=True, dates=new_dates)

@mod_screening.route('/screening/date', methods=['GET'])
def get_all_screening():
    id1 = request.args.get('date_id')
    id2 = request.args.get('movie_id')

#    dates = Screening.query.filter(and_(Screening.screening_date == id1,Screening.movie_id == id2)).all()
    dates2 = db.session.query(Screening, Auditorium).join(Auditorium).filter(Screening.auditorium_id == Auditorium.id).order_by('Auditorium.name','Screening.screening_start_time')
    slots = []
    for date in dates2:
        slots.append({ 'time' : date.Screening.screening_start_time , 'hall_name' : date.Auditorium.name , 'hall_type' : date.Auditorium.audi_type })

#    for date in dates:
#        new_dates.append(date.to_dict_shows())
    if dates2 is None:
        return jsonify(success=False), 404
    else:
        return jsonify(success=True, slots=slots)


@mod_screening.route('/screening/add', methods=['GET'])
def add_screening():
    date = request.args.get('date')
    time = request.args.get('time')
    auditorium_id = request.args.get('audi_id')
    movie_id = request.args.get('movie_id')
    scr1  = Screening(movie_id,auditorium_id,time,date)
    db.session.add(scr1)
    db.session.commit()
    print(scr1)
    return jsonify(success=True)
        #return jsonify(success=True, dates=new_dates)

#@mod_screening.route('/screening/delete', methods=['GET'])
