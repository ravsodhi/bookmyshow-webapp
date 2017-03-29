from flask import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import * #for and_ && or_
from flask_cors import CORS
#app=CORS(__name__)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


shows = db.Table("shows",
        db.Column('movie_id', db.Integer, db.ForeignKey('movie.movie_id')),
        db.Column('date_id', db.Integer, db.ForeignKey('date.date_id')),
        #db.Column('time_id', db.Integer, db.ForeignKey('time.time_id'))
    )

times = db.Table('times',
        db.Column('time_id', db.Integer, db.ForeignKey('time.time_id')),
        db.Column('movie_id', db.Integer, db.ForeignKey('movie.movie_id'))
        )

dates = db.Table('dates',
        db.Column('time_id', db.Integer, db.ForeignKey('time.time_id')),
        db.Column('date_id', db.Integer, db.ForeignKey('date.date_id'))
        )
class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    showing = db.relationship('Date', secondary=shows, backref = db.backref('movies', lazy='dynamic'))
    timing  = db.relationship('Time', secondary=times, backref = db.backref('current_movies', lazy='dynamic'))

class Date(db.Model):
    date_id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.String(20))
    date_timing  = db.relationship('Time', secondary=dates, backref = db.backref('current_dates', lazy='dynamic'))

class Time(db.Model):
    time_id = db.Column(db.Integer, primary_key = True)
    time = db.Column(db.String(20))
    #k = db.relationship('Date', secondary=shows, backref = db.backref('movies', lazy='dynamic'))

movie1 = Movie(name = 'batman')
movie2 = Movie(name = 'superman')
date1  = Date(date = '01/05/2017')
date2  = Date(date = '02/05/2017')
time1  = Time(time = '10:00 am')
time2  = Time(time = '08:30 pm')
db.create_all()
db.session.add(movie1)
db.session.add(movie2)
db.session.add(date1)
db.session.add(date2)
db.session.add(time1)
db.session.add(time2)
date1.movies.append(movie1)
date1.movies.append(movie2)
time1.current_dates.append(date1)
time1.current_dates.append(date2)
time1.current_movies.append(movie1)
time2.current_movies.append(movie1)
db.session.commit()

