from flask import Flask,jsonify,request

app = Flask(__name__)

database = [{}]

@app.route('/register', methods=['post'])
def register():
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


if __name__=='__main__':
    app.run()