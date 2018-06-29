from flask import Flask,jsonify,request,session
from register import Register_data
from post  import  Post_content
from  comment import Post_comment

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

app = Flask(__name__)

Register_data = Register_data()
Post_content = Post_content()
Post_content = Post_content()

@app.route('/')
def home():
    return "Register or Login"

@app.route('/register', methods=['POST'])
def register():
    """
    User Register"
    """
    reg = {
        'full_name': request.json['full_name'],
        'username':  request.json['username'],
        'email': request.json['email'],
        'password':request.json['password'],
        'confirm_password':request.json['confirm_password']        
    }
    if email in database:
        response = jsonify({
            'status':'error',
            'message':"Sorry the email is already taken"
            })
    database.append(reg)
    return jsonify({'reg': reg}), 201


@app.route('/login', methods=['POST'])
def login():
    """
    User Login
    """
    if resqust.json['username'] != ['username'] or request.json['password'] != ['password']:
        error = 'Invalid credentials. Please try again.'
    else:
        session['logged_in'] = True
        flash('You are just logged in')


@app.route('/post', methods=['POST'])
def post():
    """
    User Post content
    """
    data = {
        'user_id': user_id,
        'id': post_id,
        'title': request.json['title'],
        'content': request.json['content']
    }
    database.append(data)
    return jsonify({'data': data}),201

@app.route('/comment', methods=['POST'])
def comment():
    """
    User post comment
    """
    com = {
        'user_id': user_id,
        'post_id':post_id,
        'comment': resqust.json['comment']
    }
    database.append(com)
    return jsonify({'com': com}),201




if __name__=='__main__':
    app.run()