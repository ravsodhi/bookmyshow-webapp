from flask import Blueprint, request, session, jsonify, render_template
from app import db
from .models import Booking
from sqlalchemy import *

mod_booking = Blueprint('booking', __name__, url_prefix='/api')


@mod_booking.route('/booking', methods=['GET'])
def display_booking():
    bookings = Booking.query.all()
    return jsonify(success=True),200

