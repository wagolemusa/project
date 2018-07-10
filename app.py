from flask import Flask, request,flash,redirect, url_for, session, logging, jsonify
from datetime import datetime
from flask_marshmallow import Marshmallow
from passlib.hash import sha256_crypt
from flask_bcrypt import Bcrypt
import json
import os
#from flask.ext.bcrypt import Bcrypt

from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:refuge@localhost/wies'
app.secret_key = "refuge"

db = SQLAlchemy(app)
ma = Marshmallow(app)


#Cheack if user loggged_in
def is_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		#toke = request.args.get('token')
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('Unauthorized, Please login', 'danger')
			return redirect(url_for('login'))
	return wrap


class Comments(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	comment = db.Column(db.String(500))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

	def __init__(self,comment):
		self.comment = comment
		#self.user_id = user_id


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

class UserSchema(ma.Schema):
	class Meta:
		fields = ('full_name', 'username', 'email', 'password')

user_schema = UserSchema()
user_schema = UserSchema(many=True)



@app.route('/')
def home():
	return jsonify({'message':'Welcome to the System'}) 
#register routes
@app.route('/api/v1/register', methods=['POST'])
def register():
	user = Users(
		request.form['full_name'],
		request.form['username'],
		request.form['email'],
		request.form['password'],
		request.form['confirm_password']
	)
	try:
		db.session.add(user)
		db.session.commit()
		status = 'Succes'
	except:
		status = 'This useis already registerd'

	db.session.close()
	return jsonify({'result': status})


#loggin routes
@app.route('/api/v1/login', methods=['GET', 'POST'])
def login():
	json_data = request.json
	user = Users.query.filter_by(email=json_data['email']).first()
	user.password, json_data['password']
	session['logged_in'] = True
	status = True
	return jsonify({'result': status})

#post comments
@app.route('/api/v1/post_comment', methods=['POST'])
def post():
	comm = Comments(
		request.form['comment']
		)
	try:
		db.session.add(comm)
		db.session.commit()
		status = 'Success'
	except:
		status = "This it con not be black"
	db.session.close()
	return jsonify({'result': status})

#View comments
@app.route('/api/v1/view_post', methods=['GET'])
def veiw_post(id):
	comment = Comments.query.all(id)
	return comment

#view Users details 
@app.route("/api/v1/get_all_user", methods=["GET"])
def get_all_user():
	all_users = Users.query.all()
	result = all_users
	return jsonify(result.data)




if __name__ =="__main__":
	app.run()