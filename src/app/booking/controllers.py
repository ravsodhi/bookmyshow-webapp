from flask import Blueprint, request, session, jsonify, render_template,redirect
from app import db
from .models import Booking
from app.user.models import User
from app.seat.models import Seat
from app.auditorium.models import Auditorium
from app.screening.models import Screening
from app.movie.models import Movie

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
    	seats.append({ 'screening_id' :i.Booking.screening_id,'seat_row':i.Seat.row,'seat_column':i.Seat.column,'seat_id':i.Seat.id, 'seat_cost': i.Seat.cost, 'audi_type': m.Auditorium.audi_type})
    if bookings is None:
    	return jsonify(success=False), 404
    else:
    	return jsonify(success=True, seats=seats)
@mod_booking.route('/booking/user', methods=['GET'])
def book_user():
	# Change url to get user id from here only (if usr_id in session) return user id#
	if 'user_id' in session:
		user_id = session['user_id']
		print(user_id)
	else:
		return jsonify(success=False), 404
	
	booking_data = db.session.query(Booking,Screening,Seat).join(Screening,Seat).filter(Booking.user_id == user_id).order_by(Screening.id,Seat.row)
	print('booking_data', booking_data)
	bookings = []
	screening_id = 0
	screening_data = []
	for i in booking_data:
		if(screening_id != i.Screening.id):
			screening_aud_data = db.session.query(Screening,Auditorium).join(Auditorium).filter(Screening.id == i.Screening.id).first()
			screening_mov_data = db.session.query(Screening,Movie).join(Movie).filter(Screening.id == i.Screening.id).first()
			screening_id = i.Screening.id
		print(screening_mov_data)
		bookings.append({'screening_time':str(i.Screening.screening_start_time),'screening_date':str(i.Screening.screening_date),'screening_id':i.Screening.id,'movie_title':screening_mov_data.Movie.title,'audi_name':screening_aud_data.Auditorium.name,'audi_type':screening_aud_data.Auditorium.audi_type,'seat_row':i.Seat.row,'seat_column':i.Seat.column, 'seat_cost': i.Seat.cost})
	
	screening_id = 0
	booking_info = []
	if bookings is None:
		return jsonify(success=False), 404
	else:
		for i in bookings:
			#print(i)
			if screening_id != i['screening_id']:
				if i != bookings[0]:
					booking_info.append({'cost':seat_cost,'screening_time':screening_time,'screening_date':screening_date,'movie_title':movie_title,'audi_name':audi_name,'audi_type':audi_type,'seats':seats})
				screening_id = i['screening_id']
				screening_date = i['screening_date']
				screening_time = i['screening_time']
				movie_title = i['movie_title']
				audi_name = i['audi_name']
				audi_type = i['audi_type']
				
				seats = []
				seat_str = ""
				seat_cost = 0
						
			seat_str = i['seat_row'] + str(i['seat_column'])
			seats.append(seat_str)
			seat_cost += i['seat_cost']
			print(seats)
			print(booking_info)
		booking_info.append({'cost':seat_cost,'screening_time':screening_time,'screening_date':screening_date,'movie_title':movie_title,'audi_name':audi_name,'audi_type':audi_type,'seats':seats})
				#print(seat_str)
		#print(bookings[0])
		#print(bookings[0]['screening_id'])
		return jsonify(success=True, booking_data=booking_info)

@mod_booking.route('/booking/add', methods=['GET'])
def add_booking():
	if 'user_id' in session:
		use = session['user_id']
	else:
		return jsonify(success=False)
	print(use)
	scr_id =  int(request.args.get('scr_id'))
	k = request.args.get('seats')
	k = k.split(",")
	print(k)
	screening_touple = Screening.query.filter(Screening.id == scr_id).first()
	start_time = screening_touple.screening_start_time
	start_date = screening_touple.screening_date
	hall_id = screening_touple.auditorium_id
	hall_touple = Auditorium.query.filter(Auditorium.id == hall_id).first()
	hall_name = hall_touple.name
	hall_type = hall_touple.audi_type
	movie_touple = Movie.query.filter(Movie.id == screening_touple.movie_id).first()
	movie_name = movie_touple.title
	print(start_time)
	print(scr_id)
	p =[]
	cost = 0
	for i in k:
		m = i[1:]
		screens = Seat.query.filter(and_(Seat.row == i[0],Seat.column == int(m))).first()
		p.append(screens.id)
		cost += screens.cost
	for t in p:
		sy = Booking(use,scr_id,t)
		db.session.add(sy)
	print(p)
	db.session.commit()
	#	seat_id = int(request.args.get('seat_id'))
#	Book = Booking(user_id,scr_id,seat_id)
#	db.session.add(Book)
#	db.session.commit()
	print(type(str(start_time)))
	ticket = { 'seats' : k , 'screening_start_time' : str(start_time) , 'total_cost' : cost , 'hall_name' : hall_name , 'hall_type' : hall_type , 'date' : start_date , 'movie_name' : movie_name}
	session['myticket'] = ticket
	print('reached at end of booking controllers')
	return jsonify(success=True),200

