from flask import Flask, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:refuge@localhost/andela'

db = SQLAlchemy(app)


class Comments(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, primary_key=True)
	comment = db.Column(db.String(500), nullable=True)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

	def __init__(self,comment, user_id):
		self.comment = comment
		self.user_id = user_id


	def __repr_(self):
		return '<Comments {}>'.format(self.comment)


class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	full_name = db.Column(db.String(30), unique=True)
	username = db.Column(db.String(30), unique=True)
	email = db.Column(db.String(120), unique=True)
	password = db.Column(db.String(120))
	active = db.Column(db.Boolean())
	confirm_password = db.Column(db.String(120))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	


	def __init__(self, full_name, username, email, password, confirm_password):
		self.full_name = full_name
		self.username = username
		self.email = email
		self.password = password
		self.confirm_password = confirm_password


		def __repr__(self):
			return '<Users {}'.format(self.username)



@app.route('/')
def home():
	return "<h1>Welcome to the System<h1>"

@app.route('/api/v1/register', methods=['POST'])
def register():
	user = Users(request.form['full_name'], request.form['username'], request.form['email'], request.form['password'], request.form['confirm_password'])
	db.session.add(user)
	db.session.commit()
	return "True"








if __name__ =="__main__":
	app.run()