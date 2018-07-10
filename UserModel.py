import datetime
class User(db.Model):
	user_id = db.Column(db.Integer, primary_key=True)
	full_name = db.Column(db.String(30), unique=True)
	username = db.Column(db.String(30), unique=True)
	email = db.Column(db.String(120), unique=True)
	password = db.Column(db.String(120), nullable=True)
	created_at = db.Column(db.Datetime)
	
	
