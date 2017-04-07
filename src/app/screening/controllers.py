from flask import Blueprint, request, session, jsonify, render_template,redirect
from app import db
from .models import Screening
from sqlalchemy import *
from app.movie.models import Movie
from app.auditorium.models import Auditorium
from datetime import *

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
    movie_id = request.args.get('movie_id')
    #print(movie_id)
    #print("What the fuck")
    dates = Screening.query.filter(Screening.movie_id == movie_id).order_by(str(Screening.screening_date))
    #print(dates)
    #print(dates[0])
    new_dates = []

    for i in dates:
        #print(date)
        new_dates.append(i.to_dict_dates())
    if dates is None:
        return jsonify(success=False), 404
    else:
        return jsonify(success=True, dates=new_dates)

@mod_screening.route('/screening/date', methods=['GET'])
def get_all_screening():
    id1 = request.args.get('date_id')
    id2 = request.args.get('movie_id')
    id1 = id1.split("-")
    
 #   x = datetime.date(int(id[0]),int(id[1]),int(id[2]))
    id1 = date(int(id1[0]),int(id1[1]),int(id1[2]))
    t = time(8,0)
    print(t)
#   print(type(x))
    x = Screening.query.filter(Screening.screening_start_time == t).first()
    h = x.screening_start_time.hour
    print(h)
    print(type(h))
    def get_sec(time_str):
        h, m, s = time_str.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)


    dates2 = db.session.query(Screening, Auditorium).join(Auditorium).filter(and_(Screening.auditorium_id == Auditorium.id,Screening.screening_date == id1,Screening.movie_id == id2)).order_by(Auditorium.name.asc(),(Screening.screening_start_time-datetime(1970,1,1)))
    slots = []
    for i in dates2:
        slots.append({ 'screening_id' :i.Screening.id,'time' : str(i.Screening.screening_start_time) , 'hall_name' : i.Auditorium.name , 'hall_type' : i.Auditorium.audi_type })
#    print(type(slots))
#    for date in dates:
#        new_dates.append(date.to_dict_shows())
    if dates2 is None:
        return jsonify(success=False), 404
    else:
        return jsonify(success=True, slots=slots)


@mod_screening.route('/screening/add', methods=['GET'])
def add_screening():
    #date = (request.form.get('day'),request.form
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
