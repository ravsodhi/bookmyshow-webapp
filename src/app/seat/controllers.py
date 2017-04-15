from flask import Blueprint, request, session, jsonify, render_template,redirect
from app import db
from .models import Seat
from app.user.models import User

from sqlalchemy import *
from app.forms.models import CostForm

mod_seat = Blueprint('seat', __name__)


@mod_seat.route('/seat/cost', methods=['GET', 'POST'])
def setcost():
	if 'user_id' not in session:
		return render_template('401.html'),401
	else:
		print(session['user_id'])
		use = User.query.filter_by(id = session['user_id']).first()
		print(use.is_admin)
		if use.is_admin is True:
			form = CostForm()
			ans = {'log':"Logout",'val':use.name}	
			if form.validate_on_submit():
				print('Cost Form')
				platinum = form.platinum.data
				gold = form.gold.data
				silver = form.silver.data
				k = Seat.query.all()
				for i in k:
					db.session.delete(i)
				db.session.commit()
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
				print('Seat Cost')
				return redirect("http://127.0.0.1:5000/admin")
			return render_template('seatcost.html', form=form,log=ans),200
		else:
			return render_template('401.html'),401


@mod_seat.route('/api/seat/get', methods=['GET'])
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


