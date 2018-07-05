from flask import Flask, jsonify, render_template, session, request, url_for, flash, redirect
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from flask import make_response

from functools import wraps
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()




app = Flask(__name__)

app.secret_key = "refuge wise"


registers = [
		{
				'user_id': 1,
    		'full_name':'refuge wise',
    		'username': 'refuge',
    		'email':  'wise@gmail.com',
    		'password': 'wise@1',
    		'confirm_password':'123456'

		},
		{
				'user_id':2,
    		'full_name':'opio wafula',
    		'username' : 'opio',
    		'email': 'wafula@gmail.com',
    		'password':'me1223',
    		'confirm_password':'me1223'
		}
]
comments = [
			{
			'user_id': 1,
			'post_id': 1,
			'post' : 'That is not True'
		}
]




# Validates logged in user with session
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('/api/auth/login'))
	return wrap


#home route
@app.route('/', methods=['GET'])
def index():
	return jsonify({'message': 'Welcome to our system'})

#User Register 
@app.route('/api/auth/register',  methods=['POST'])
def register():
	users={
	'user_id': registers[-1]['user_id'] + 1,
	'full_name' : request.form['full_name'],
	'username': request.form['username'],
	'email' :request.form['email'],
	'password': request.form['password'],
	'confirm_password' :request.form['confirm_password']	
	}
	registers.append(users)
	return jsonify({'message': 'Successfully Registered'}),201

#User login
@app.route('/api/auth/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':

		username = request.form['username']
		password = request.form['password']
		if username in registers:
			if password == registers[username["password"]]:
				session["logged_in"] = True
				return jsonify({"message": "Successfully Logged In"})
		return jsonify({"message": "Wrong Username and password"})

# Post comment
@app.route('/api/v1/post-comment', methods=['GET', 'POST'])
def post_comment():
	comm = {
		'post_id': comments[-1]['post_id'] + 1,
		'user_id': request.form['user_id'],
		'comment' : request.form['comment']
	}
	comments.append(comm)
	return jsonify({'comm': comm })

#deleting comments
@app.route('/api/v1/remove_post/<int:comments_id>', methods=['DELETE'])
def delete_comment():
	comm = [comm for comm in comments if comm['post_id']]
	if len(comm) == 0:
		abort(404)
	comments.remove(comm[0])
	return jsonify({'message': 'Comment successfully deleted'})



@app.route('/api/v1/view_comment', methods=['GET'])
def veiw_comment():
	return jsonify({'comments': comments })

# User Account
@app.route('/api/v1/account', methods=['GET'])
def user_account():
	return jsonify({'registers': registers })



#User Logout
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run()