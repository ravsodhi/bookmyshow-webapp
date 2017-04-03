from flask import Blueprint, request, session, jsonify, render_template
from app import db
from sqlalchemy import *

class Movie (db.Model):
 #Model
    __tablename__ = "movie"
    id = db.Column('id', db.Integer, primary_key = True)
    title = db.Column('title', db.String)
    director = db.Column('director', db.String)
    description = db.Column('description', db.String)
    duration_min = db.Column('duration_min', db.Integer)
    rating = db.Column('rating', db.Float)
    def __init__(self,title,director,description,duration_min,rating):
    #def __init__(self,title):
        self.title = title
        self.director = director
        self.description = description
        self.duration_min = duration_min
        self.rating = rating

    def __repr__(self):
        #return "Movie { name: %r }"%(self.title)
        return "Movie {'name': %r, 'director' : %r, 'description' :%r ,'duration_min' : %r, 'rating' : %r}"%(self.title,self.director,self.description,self.duration_min,self.rating)

    def to_dict_movies(self):
        return {
        'title': self.title, 
        'director' : self.director,
        'description' :self.description, 
        'id' : self.id
        }

