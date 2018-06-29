from flask import Flask, jsonify, render_template, session, request, url_for, flash

from register import Registers
from comment import Post_comment

app = Flask(__name__)

app.secrect_key = "my precious"

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
	return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'refuge' or request.form['password'] != 'wise':
			error  = 'Invalid credentials please try agian.'
		else:
			session['logged_in'] = True
			flask('You are just logged in')
			return redirect(url_for('post'))
			return render_template('login.html', error=error)
    
@app.route('/user_details')
def view_register():
	return render_template('user_details.html', registers = Registers)


@app.route('/post', methods=['GET', 'POST'])
def post():
	return render_template('post.html')
	

if __name__ == '__main__':
	app.run(debug=True)