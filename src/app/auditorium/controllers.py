from flask import Blueprint, request, session, jsonify, render_template,redirect
from app import db
from .models import Auditorium
from sqlalchemy import *
from app.user.models import User
from app.forms.models import HallForm
mod_auditorium = Blueprint('auditorium', __name__)


@mod_auditorium.route('/api/auditorium', methods=['GET'])
def display_audi():
	print("display_audi")
	audi = Auditorium.query.order_by(Auditorium.audi_type)
	print(audi)
	audi_array = []
	for i in audi:
		audi_array.append(i.to_dict_audi())
	return jsonify(success=True, audi=audi_array),200

@mod_auditorium.route('/hall/add', methods=['GET', 'POST'])
def addhall():
	if 'user_id' not in session:
		return render_template('401.html'),401
	else:
		print(session['user_id'])
		use = User.query.filter_by(id = session['user_id']).first()
		print(use.is_admin)
		if use.is_admin is True:
			form = HallForm()
			ans = {'log':"Logout",'val':use.name}	
			if form.validate_on_submit():
				print('Hall Form')
				name = form.hall_name.data
				audi_type = form.hall_type.data
				new_audi = Auditorium(name,audi_type)
				db.session.add(new_audi)
				db.session.commit()
				print('Hall Added')
				return redirect("http://127.0.0.1:5000/admin")
			return render_template('addhall.html', form=form,log=ans	),200
		else:
			return render_template('401.html'),401
