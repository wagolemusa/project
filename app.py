from flask import Flask, jsonify, render_template, session, request, url_for, flash, redirect
from wtforms import Form, StringField, TextAreaField, PasswordField, validators

from functools import wraps

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
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('login'))
	return wrap


@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		comment['user_id'] = len(users)+1
		comment['comment'] = request.post('comment')
	return render_template('index.html', comments = Post_comments)

# registration validation form
class RegisterForm(Form):
	full_name = StringField('full_name', [validators.Length(min=1, max=50)])
	username = StringField('username', [validators.Length(min=4, max=25)])
	email = StringField('email', [validators.Length(min=6, max=50)])
	password = PasswordField('Password',[
		validators.DataRequired(),
		validators.EqualTo('confirm', message='Password does not match')

		])
	confirm = PasswordField('Confirm Password')

#User Regisetr
@app.route('/register', methods=['GET', 'POST'])
def register():
	#form = RegisterForm(request.form)
	#if request.methods == 'POST' and form.validete():

		#register_info['full_name'] = request.form.post('full_name')
		#register_info['username'] = request.form.post('username')
		#register_info['email'] = request.form.post('email')
		#register_info['password'] = request.form.post('password')
		#register_info['confirm_password'] = request.form.post('confirm_password')
		#data.append(register_info)
		#flash ('successfully Registerd')
		#print('data')
  	return render_template('register.html')


#User login
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'refuge' or request.form['password'] != 'wise@1':
			error = 'Invalid credentials. Please try agian.'
		else:
			session['logged_in'] = True
			flash('You were just logged in!')
			return redirect(url_for('comment'))
	return render_template('login.html', error=error)


 
@app.route('/user_details', )
@login_required
def view_register():
	return render_template('user_details.html', registers = Registers)



@app.route('/comment',  methods=['GET', 'POST'])
@login_required
def comment():
	if request.method == 'POST':
		comment['user_id'] = len(users)+1
		comment['comment'] = request.post('comment')
	return render_template('comment.html')



@app.route('/query_comment', )
@login_required
def show_comment():
	return render_template('query_comment.html', comments = Post_comments)



	
@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run()