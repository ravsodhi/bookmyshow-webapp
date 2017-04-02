from flask import Blueprint, request, session, jsonify
from app import db, requires_auth
from .models import Screening
from sqlalchemy import *
    
mod_screening = Blueprint('screening', __name__, url_prefix='/api')
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

    dates = Screening.query.filter(and_(Screening.screening_date == id1,Screening.movie_id == id2)).all()
    new_dates = []
    for date in dates:
        new_dates.append(date.to_dict_shows())
    if dates is None:
        return jsonify(success=False), 404
    else:
        return jsonify(success=True, dates=new_dates)


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
