
from flask_sqlalchemy import SQLAlchemy
from app import db

import datetime
'''
from flask import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from flask_cors import CORS

#app=CORS(__name__)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
'''
class Screening (db.Model):
    __tablename__ = "screenings"
    id = db.Column('id', db.Integer, primary_key = True)
    movie_id = db.Column('movie_id', db.Integer)#, db.ForeignKey('movie.id'))
    auditorium_id = db.Column('auditorium_id', db.Integer)#, db.ForeignKey('auditorium.id'))
    screening_start_time = db.Column('screening_start_time', db.String)
    screening_date = db.Column('screening_date',db.String)

    def __init__(self,movie_id,auditorium_id,screening_start_time,screening_date):
        self.movie_id = movie_id
        self.auditorium_id = auditorium_id
        self.screening_start_time = screening_start_time
        self.screening_date = screening_date

    def to_dict(self):
        return {
            'id': self.id,
            'movie_id': self.movie_id,
            'auditorium_id': self.auditorium_id,
            'screening_start_time': self.screening_start_time,
            'screening_date': self.screening_date
        }

    def to_dict_dates(self):
        return {
            'date' : self.screening_date
        }
    def to_dict_shows(self):
        return {
            'screening_start_time' : self.screening_start_time
        }
    def __repr__(self):
        return "Screening { movie_id: %r auditorium_id: %r screening_start_time:%r screening_date: %r}"%(self.movie_id,self.auditorium_id,self.screening_start_time,self.screening_date)
'''
db.create_all()
#scr1  = Screening(1,1,"12:00","2016-12-04")
scr1  = Screening(1,1,datetime.time(12, 0,6), datetime.date(2017,4,2))
scr2  = Screening(1,1,datetime.time(9, 0,7), datetime.date(2017,4,2))

db.session.add(scr1)
db.session.add(scr2)

db.session.commit()
print('hello',scr1.screening_start_time)
print(Screening.query.filter_by(screening_start_time = datetime.time(12,0,6)).all())
print(scr1)
#Screening(1,1,"2016-12-04","12:00")
'''