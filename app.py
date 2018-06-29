from flask import Flask, jsonify, render_template, session, request, url_for, flash

from functools import wraps

app = Flask(__name__)

app.secrect_key = "my precious"


@app.route('/')
def home():
	return render_template('index.html')




if __name__ == '__main__':
	app.run(debug=True)