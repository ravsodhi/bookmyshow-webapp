from flask import Blueprint, request, session, jsonify, render_template
from app import db
from sqlalchemy import *
class Auditorium (db.Model):
    __tablename__ = "auditorium"
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column('name', db.String)
    audi_type = db.Column('audi_type',db.String)

    def __init__(self,name,audi_type):
        self.name = name
        self.audi_type = audi_type
    def __repr__(self):
        return "Auditorium { 'name': %r, 'audi_type': %r}"%(self.name,self.audi_type)

