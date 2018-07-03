from flask import Flask, jsonify, render_template, session, request, url_for, flash, redirect
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from flask import make_response

from functools import wraps
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


from register import Registers
from comment import Post_comments

app = Flask(__name__)

app.secret_key = "refuge wise"

Registers = Registers()
Post_comments = Post_comments()

data = []
register_info = {}
comments = {}


# Validates logged in user with session
#def login_required(f):
	#@wraps(f)
	#def wrap(*args, **kwargs):
#		if 'logged_in' in session:
#			return f(*args, **kwargs)
#		else:
#			flash('You need to login first.')
#			return redirect(url_for('login'))
#	return wrap
@auth.get_password
def get_password(username):
    if username == 'refuge':
        return 'python'
    return None

@app.route('/', methods=['GET'])
@auth.login_required
def index():
	return jsonify({'message': 'Welcome to our system'})

@app.route('/api/auth/register', methods=['GET', 'POST'])
def register():
	user = {
		'user_id': registers[-1]['user_id'] + 1,
		'full_name': request.json['full_name'],
		'username' :request.json['username'],
		'email' : request.json['email'],
		'password' :request.json['password'],
		'confirm_password': request.json['confirm_password']
	}
	registers.append(user)
	return jsonify({'user': user}),201



	
@app.route('/logout')
#@login_required
def logout():
	session.pop('logged_in', None)
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run()