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

@mod_movie.route('/movie/add', methods=['POST'])
def add_movie():
	print("hdwdjw")
	title = request.form['title']
	print(title)
	director = request.form['director']
	discription = request.form['discription']
	duration = request.form['duration']
	url = request.form['url']
	new_movie = Movie(title,director,discription,duration,url)
	db.session.add(new_movie)
	db.session.commit()
	return jsonify(success=True),200
