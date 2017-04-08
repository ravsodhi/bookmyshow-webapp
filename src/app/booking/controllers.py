from flask import Blueprint, request, session, jsonify, render_template,redirect
from app import db
from .models import Booking
from app.user.models import User
from app.seat.models import Seat
from app.auditorium.models import Auditorium
from app.screening.models import Screening

from sqlalchemy import *

mod_booking = Blueprint('booking', __name__, url_prefix='/api')


@mod_booking.route('/booking', methods=['GET'])
def display_booking():
    bookings = Booking.query.all()
    return jsonify(success=True),200

@mod_booking.route('/booking/<scr_id>', methods=['GET'])
def book_screening(scr_id):
    bookings = db.session.query(Booking,Seat).join(Seat).filter(Booking.screening_id == scr_id)
    m = db.session.query(Screening, Auditorium).join(Auditorium).filter(Screening.id == scr_id).first()

    seats=[]
    for i in bookings:
    	#print(i)
    	i.Seat
    	seats.append({ 'screening_id' :i.Booking.screening_id,'seat_row':i.Seat.row,'seat_column':i.Seat.column,'seat_id':i.Seat.id,'audi_type': m.Auditorium.audi_type})
    if bookings is None:
    	return jsonify(success=False), 404
    else:
    	return jsonify(success=True, seats=seats)

@mod_booking.route('/booking/add', methods=['GET'])
def add_booking():
	if 'user_id' in session:
		use = session['user_id']
	else:
		return redirect("http://127.0.0.1:5000/login")
	print(use)
	scr_id =  int(request.args.get('scr_id'))
	k = request.args.get('seats')
	k = k.split(",")
	print(k)
	print(scr_id)
	p =[]
	for i in k:
		m = i[1:]
		print(m)
		p.append(Seat.query.filter(and_(Seat.row == i[0],Seat.column == int(m))).first().id)
		print(p)
	for t in p:
		sy = Booking(use,scr_id,t)
		db.session.add(sy)
	print(p)
	db.session.commit()
	#	seat_id = int(request.args.get('seat_id'))
#	Book = Booking(user_id,scr_id,seat_id)
#	db.session.add(Book)
#	db.session.commit()
	return jsonify(success=True),200

