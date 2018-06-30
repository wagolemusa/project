from flask import Flask, jsonify, render_template, session, request, url_for, flash, redirect
from wtforms import Form, StringField, TextAreaField, passwordField, validators
from functools import wraps

from register import Registers
from comment import Post_comment

app = Flask(__name__)

app.secret_key = "my precious"

Registers = Registers()
Post_comment = Post_comment()


# Validates logged in user with session
def login_required(f):
	@wraps(f)
	def warp(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to Login first')
			return redirect(url_for('login'))
	return wrap

@app.route('/')
def home():
	return render_template('index.html', comments = Post_comment)

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
			return redirect(url_for('post'))
	return render_template('login.html', error=error)

#User Details    
@app.route('/user_details', )
def view_register():
	return render_template('user_details.html', registers = Registers)


#Post comment
@app.route('/post', methods=['GET', 'POST'])
def post():
	return render_template('post.html')
	

if __name__ == '__main__':
	app.run()