from flask import Blueprint, request, session, jsonify, render_template
from app import db
from sqlalchemy import *
class Booking (db.Model):
    __tablename__ = "booking"
    id = db.Column('id',db.Integer,primary_key = True)
    user_id = db.Column('user_id',db.Integer,db.ForeignKey('user.id'))
    screening_id = db.Column('screening_id',db.Integer,db.ForeignKey('screening.id'))
    seat_id = db.Column('seat_id',db.Integer,db.ForeignKey('seat.id'))

    def __init__(self,user_id,screening_id,seat_id):
        self.user_id = user_id
        self.screening_id = screening_id
        self.seat_id = seat_id

    def to_dict_booking(self):
        return{
		'id' : self.id ,
		'user_id' : self.user_id,
		'screening_id': self.screening_id,
		'seat_id': self.seat_id
		}

    def __repr__(self):
        return "Booking { user_id: %r screening_id: %r seat_id: %r}"%(self.user_id,self.screening_id,self.seat_id)
