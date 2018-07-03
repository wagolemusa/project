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

comments = {
				
			'user_id': 1,
			'post_id': 1,
			'post' : 'That is not True'	
}




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

#home route
@app.route('/', methods=['GET'])
@auth.login_required
def index():
	return jsonify({'message': 'Welcome to our system'})

#User Register 
@app.route('/api/auth/register', methods=['GET', 'POST'])
def register():
	user = {
		#'user_id': registers[-1]['user_id'] + 1,
		'full_name': request.json['full_name'],
		'username' :request.json['username'],
		'email' : request.json['email'],
		'password' :request.json['password'],
		'confirm_password': request.json['confirm_password']
	}
	registers.append(user)
	return jsonify({'user': user}),201

# Post comment
@app.route('/api/v1/post-comment', methods=['GET', 'POST'])
def post_comment():
	comm = {
		'post_id': comm[-1]['post_id'] + 1,
		'user_id': request.json.get['user_id'],
		'comment' : request.json['comment']
	}
	comments.append(comm)
	return jsonify({'comm': comm })

@app.route('/api/v1/view_comment', methods=['GET'])
def veiw_comment():
	return jsonify({'comments': comments })

# User Account
@app.route('/api/v1/account', methods=['GET'])
def user_account():
	return jsonify({'registers': registers })

#User Logout
@app.route('/logout')
#@login_required
def logout():
	session.pop('logged_in', None)
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run()