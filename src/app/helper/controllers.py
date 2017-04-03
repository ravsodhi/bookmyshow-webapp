from flask import Blueprint, request, session, jsonify
from app import db,requires_auth
from functools import wraps
from flask import render_template
mod_todo = Blueprint('todo', __name__, url_prefix='/api')


@mod_todo.route('/todo', methods=['POST'])
def form_auth():
      #@wraps(f)
      #def decorated(*args, **kwargs):
      if 'user_id' not in session:
           return jsonify(success=False)
      #return f(*args, **kwargs)
      return jsonify(success=True)

