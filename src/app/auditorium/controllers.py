from flask import Blueprint, request, session, jsonify, render_template
from app import db
from .models import Auditorium
from sqlalchemy import *

mod_auditorium = Blueprint('auditorium', __name__, url_prefix='/api')


@mod_auditorium.route('/auditorium', methods=['GET'])
def display_audi():
	print("display_audi")
	audi = Auditorium.query.all()
	print(audi)
	audi_array = []
	for i in audi:
		audi_array.append(i.to_dict_audi())
	return jsonify(success=True, audi=audi_array),200

@mod_auditorium.route('/auditorium/add', methods=['POST'])
def add_audi():
	name = request.form['name']
	audi_type = request.form['audi_type']
	new_audi = Auditorium(name,audi_type)
	db.session.add(new_audi)
	db.session.commit()
	return jsonify(success=True),200
