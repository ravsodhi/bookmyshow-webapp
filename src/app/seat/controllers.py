from flask import Blueprint, request, session, jsonify, render_template
from app import db
from .models import Seat
from sqlalchemy import *

mod_seat = Blueprint('seat', __name__, url_prefix='/api')


@mod_seat.route('/seat', methods=['GET'])
def display_seat():
    seats = Seat.query.all()
    return jsonify(success=True),200

