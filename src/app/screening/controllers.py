from flask import Blueprint, request, session, jsonify, render_template,redirect
from app import db
from .models import Screening
from sqlalchemy import *
from app.movie.models import Movie
from app.auditorium.models import Auditorium
from datetime import *

mod_screening = Blueprint('screening', __name__, url_prefix='/api')

@mod_screening.route('/screening/movies', methods=['POST'])
def get_all_dates():
    movie_id = request.form['movie_id']
    dates = Screening.query.filter(Screening.movie_id == movie_id).order_by(str(Screening.screening_date))
    new_dates = []
    for i in dates:
        new_dates.append(i.to_dict_dates())
    if dates is None:
        return jsonify(success=False), 404
    else:
        return jsonify(success=True, dates=new_dates)

@mod_screening.route('/screening/date', methods=['POST'])
def get_all_screening():
    id1 = request.form['date_id']
    id2 = request.form['movie_id']
    id1 = id1.split("-")
    id1 = date(int(id1[0]),int(id1[1]),int(id1[2]))

    dates2 = db.session.query(Screening, Auditorium).join(Auditorium).filter(and_(Screening.auditorium_id == Auditorium.id,Screening.screening_date == id1,Screening.movie_id == id2)).order_by(Auditorium.name.asc(),(Screening.screening_start_time-datetime(1970,1,1)))
    slots = []
    for i in dates2:
        slots.append({ 'screening_id' :i.Screening.id,'time' : str(i.Screening.screening_start_time) , 'hall_name' : i.Auditorium.name , 'hall_type' : i.Auditorium.audi_type })
    if dates2 is None:
        return jsonify(success=False), 404
    else:
        return jsonify(success=True, slots=slots)

# Given a screening, provide a audi_type:
@mod_screening.route('/screening/audi', methods=['POST'])
def get_aauditype():
    id1 = request.form['scr_id']
    m = db.session.query(Screening, Auditorium).join(Auditorium).filter(Screening.id == int(id1)).first()
    ans = m.Auditorium.audi_type
    return jsonify(success=True,ans=ans)


@mod_screening.route('/screening/add', methods=['POST'])
def add_screening():
    id1 = request.form['rel_date']
    id1 = id1.split("-")
    id1 = date(int(id1[0]),int(id1[1]),int(id1[2]))
    
    id2 = request.form['off_date']
    id2 = id2.split("-")
    id2 = date(int(id2[0]),int(id2[1]),int(id2[2]))

    k = id2-id1
    k = str(k)
    k = k.split(",")
    k = k[0].split(" ")
    m = int(k[0])   #no of days for which movie is to be screened 
        
    id3 = request.form['movie_id']
    audi = request.form['audi_id']
    audi = audi.split(",")
    audilen = len(audi);

    tim = request.form['time']
    tim = tim.split(",")
    timlen = len(tim);
    '''
    print("all things needed")
    print(id1) #relese date
    print(id2)  # i=off date
    print(id3) # movieid
    print(audi) # audi_id
    print(m)    #no of days movie is to be screened
    '''
    for i in range(0,m):
        n = id1 + timedelta(days = i)
        print(n)
        for j in range(0,audilen):
            for g in range(0,timlen):
                q = tim[g].split(":")
                ti = time(int(q[0]),int(q[1]))
                scr1  = Screening(id3,audi[j],ti,n)
                db.session.add(scr1)
    db.session.commit()
    return jsonify(success=True)
