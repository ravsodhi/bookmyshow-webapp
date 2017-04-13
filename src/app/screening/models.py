
from flask_sqlalchemy import SQLAlchemy
from app import db
from app.auditorium.models import Auditorium
from datetime import datetime
from datetime import date
from datetime import time
from app.movie.models import Movie


class Screening (db.Model):
    __tablename__ = "screening"
    id = db.Column('id', db.Integer, primary_key = True)
    movie_id = db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'))
    auditorium_id = db.Column('auditorium_id', db.Integer, db.ForeignKey('auditorium.id'))
    screening_start_time = db.Column('screening_start_time', db.Time)
    screening_date = db.Column('screening_date',db.Date)

    db.relationship('Auditorium', foreign_keys='auditorium_id')
    db.relationship('Movie', foreign_keys='movie_id')

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
            'screening_start_time': str(self.screening_start_time),
            'screening_date': str(self.screening_date)
        }

    def to_dict_dates(self):
        return {
            'date' : str(self.screening_date)
        }

    def to_dict_shows(self):
        return {
            'screening_start_time' : str(self.screening_start_time)
        }
    def __repr__(self):
        return "Screening { 'movie_id': %r , 'auditorium_id': %r, 'screening_start_time':%r , 'screening_date': %r}"%(self.movie_id,self.auditorium_id,str(self.screening_start_time),str(self.screening_date))
