from flask import Blueprint, request, session, jsonify, render_template
from app import db
from .models import Seat
from sqlalchemy import *

mod_seat = Blueprint('seat', __name__, url_prefix='/api')


@mod_seat.route('/seat/set', methods=['POST'])
def set_seat_cost():
	platinum =  int(request.form['platinum'])
	gold = int(request.form['gold'])
	silver = int(request.form['silver'])
	for i in range(65,72):
		for j in range(1,16):
			s = Seat(chr(i),j,silver)
			db.session.add(s)
	for i in range(72,77):
		for j in range(1,16):
			s = Seat(chr(i),j,gold)
			db.session.add(s)

	for i in range(77,80):
		for j in range(1,16):
			s = Seat(chr(i),j,platinum)
			db.session.add(s)
	db.session.commit()
	return jsonify(success=True),200


@mod_seat.route('/seat/get', methods=['GET'])
def get_seat_cost():
	cost =[]
	c1 = Seat.query.filter(Seat.id == 1).first()
	c2 = Seat.query.filter(Seat.id == 121).first()
	c3 = Seat.query.filter(Seat.id == 211).first()
	cost.append(c1.cost)
	cost.append(c2.cost)
	cost.append(c3.cost)
	print(cost)
	return jsonify(success=True,cost=cost)


