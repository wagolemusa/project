from flask import Flask, jsonify



@app.route('/')
def home():
	return render_template('index.html')

