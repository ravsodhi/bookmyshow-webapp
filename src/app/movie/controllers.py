from flask import Blueprint, request, session, jsonify, render_template
from app import db
from .models import Movie
from sqlalchemy import *

mod_movie = Blueprint('movie', __name__, url_prefix='/api')


@mod_movie.route('/movies', methods=['GET'])
def display_movies():
    movies = Movie.query.all()
    movie_array = []

    for i in movies:
        movie_array.append(i.to_dict_movies())
    return jsonify(success=True, movies=movie_array),200
