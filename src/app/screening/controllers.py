from flask import Blueprint, request, session, jsonify, render_template,redirect
from app import db
from .models import Screening
from sqlalchemy import *
from app.movie.models import Movie
from app.user.models import User

from app.auditorium.models import Auditorium
from app.forms.models import ScreeningForm
from datetime import *

mod_screening = Blueprint('screening', __name__)

@mod_screening.route('/api/screening/movies', methods=['POST'])
def get_all_dates():
    movie_id = request.form['movie_id']
    today = date.today()    
    dates = Screening.query.filter(and_(Screening.movie_id == movie_id,Screening.screening_date >= today)).order_by(str(Screening.screening_date))
    new_dates = []
    for i in dates:
        new_dates.append(i.to_dict_dates())
    if dates is None:
        return jsonify(success=False), 404
    else:
        return jsonify(success=True, dates=new_dates)

@mod_screening.route('/api/screening/date', methods=['POST'])
def get_all_screening():
    id1 = request.form['date_id']
    id2 = request.form['movie_id']
    id1 = id1.split("-")
    id1 = date(int(id1[0]),int(id1[1]),int(id1[2]))
    now = datetime.today().time()
    today = date.today()    
    if id1 == today:
        dates2 = db.session.query(Screening, Auditorium).join(Auditorium).filter(and_(Screening.screening_start_time >= now,Screening.auditorium_id == Auditorium.id,Screening.screening_date == id1,Screening.movie_id == id2)).order_by(Auditorium.name.asc(),(Screening.screening_start_time-datetime(1970,1,1)))
    else:
        dates2 = db.session.query(Screening, Auditorium).join(Auditorium).filter(and_(Screening.auditorium_id == Auditorium.id,Screening.screening_date == id1,Screening.movie_id == id2)).order_by(Auditorium.name.asc(),(Screening.screening_start_time-datetime(1970,1,1)))
    slots = []
    for i in dates2:
        slots.append({ 'screening_id' :i.Screening.id,'time' : str(i.Screening.screening_start_time) , 'hall_name' : i.Auditorium.name , 'hall_type' : i.Auditorium.audi_type })
    if dates2 is None:
        return jsonify(success=False), 404
    else:
        return jsonify(success=True, slots=slots)

# Given a screening, provide a audi_type:
@mod_screening.route('/api/screening/audi', methods=['POST'])
def get_aauditype():
    id1 = request.form['scr_id']
    m = db.session.query(Screening, Auditorium).join(Auditorium).filter(Screening.id == int(id1)).first()
    ans = m.Auditorium.audi_type
    return jsonify(success=True,ans=ans)

@mod_screening.route('/screening/add', methods=['GET', 'POST'])
def addscreening():
    if 'user_id' not in session:
        return render_template('401.html'),401
    else:
        print(session['user_id'])
        use = User.query.filter_by(id = session['user_id']).first()
        print(use.is_admin)
        ans = {'log':"Logout",'val': 'Hi! '+ use.name}
        if use.is_admin is False:
            return render_template('401.html'),401
        else:
            form = ScreeningForm()
            if form.validate_on_submit():
                print('Screening Form')
                tim = form .selecttime.data
                audi = form.selecthall.data
                mov = form.selectmovie.data
                audilen = len(audi)
                timlen = len(tim)
                dates = Movie.query.filter(Movie.id == mov).first()
                id1 = dates.release_date
                id2 = dates.off_theatre_date
                k = id2-id1
                k = str(k)
                k = k.split(",")
                k = k[0].split(" ")
                m = int(k[0])
                for i in range(0,m):
                    n = id1 + timedelta(days = i)
                    for j in range(0,audilen):
                        for g in range(0,timlen):
                            q = tim[g].split(":")
                            ti = time(int(q[0]),int(q[1]))
                            scr1  = Screening(mov,audi[j],ti,n)
                            db.session.add(scr1)
                db.session.commit()
                print('screening added')
                return redirect('http://127.0.0.1:5000/admin')
            else:
                return render_template('addscreening.html',form=form,log=ans),200
