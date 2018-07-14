from flask import Flask, request,logging, jsonify
from datetime import datetime
from passlib.hash import sha256_crypt
from flask_marshmallow import Marshmallow
from functools	import wraps
from flask_bcrypt import Bcrypt
import json
import os
import jwt
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:refuge@localhost/python'

app..config['SECRET_KEY'] 'refuge'

db = SQLAlchemy(app)
ma = Marshmallow(app)


#Cheack if user loggged_in
def is_logged_in(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		if request.args.get('token')=='':
			return jsonify({"message": 'You need to first Login'})
		try:
			data=jwt.decode(request.args.get('token'), app.config['SECRET_KEY'])
		except:
			return jsonify({"Alert":'please login again'})
		return f(*args, **kwargs)
	return decorated

class Comments(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	comment = db.Column(db.String(500))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

	def __init__(self,comment):
		self.comment = comment
		#self.user_id = user_id
class CommentSchema(ma.Schema):
	class Meta:
		field = ('comment')

comm_schema = CommentSchema()
comm_schema = CommentSchema(many=True)

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
	user = Users(
		username = request.get_json()['username']
		password = request.get_json()['password']
		)
		if username == user[0]['username']:
			if password == user[0]['password']:
				token = jwt.encode({"username":username, "passwaord":password, "exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=20)},app.config['SECRET_KEY'])
				return  jsonify({"token":token.decode('utf-8')})
			else:
				return jsonify({"message": "Invalid credentials"})
		else:
			return jsonify({"message":"Invalid credentials"})
	
#post comments
@app.route('/api/v1/post_comment', methods=['POST'])
@is_logged_in
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
@is_logged_in
def veiw_post():
	all_comment = Comments.query.all()
	response = comm_schema.dump(all_comment)
	return jsonify(response.data)

#view Users details 
@app.route("/api/v1/get_all_user", methods=["GET"])
@is_logged_in
def get_all_user():
	all_users = Users.query.all()
	response = user_schema.dump(all_users)
	return jsonify(response.data)

#Delete Comment
@app.route('/api/v1/delete_comment/<id>', methods=['DELETE'])
#@is_logged_in
def delete_comment(id):
	comment = Comments.query.get(id)
	db.session.delete(comment)
	db.session.commit()
	return jsonify(comment)

if __name__ =="__main__":
	app.run()