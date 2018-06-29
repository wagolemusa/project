from flask import Flask, jsonify, render_template, session, request, url_for, flash

from functools import wraps

app = Flask(__name__)

app.secrect_key = "my precious"


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
	return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
	return render_template('post.html')
	

if __name__ == '__main__':
	app.run(debug=True)