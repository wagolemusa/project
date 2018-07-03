from flask import Flask, jsonify, make_response
import requests
from requests.auth import HTTPBasicAuth
import datetime
import time
import base64


app = Flask(__name__)


@app.route('/mpesa', methods= ['POST'])
def api_message():
      data = request.data
      print(data)
      return "already run"

phone = 254725696042 #phone number
amount = 1            #amout
business_short_code = 174379 # busines short code
timestamp = str(time.strftime('%Y%m%d%H%M%S'))  #generating current time and date

# generating password
def password_generater(word):
      return base64.b64encode(word,'utf-8')
password_generater('174379' + 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919' + timestamp)

# Get access token
consumer_key = "c5g00mKWmkcQBbm8TgANJBIqWAwKgsWS"
consumer_secret = "kdazijKoybDgp0GH"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key,consumer_secret))
print(r.text)

access_token = "{}".format(r.text)
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = { "Authorization": "Bearer %s" % access_token }

request = {
      "BusinessShortCode": "business_short_code",
      "Password": "password_generater",
      "Timestamp": "timestamp",
      "TransactionType": "CustomerPayBillOnline",
      "Amount": "amount",
      "PartyA": "phone",
      "PartyB": "business_short_code",
      "PhoneNumber": "phone",
      "CallBackURL": "http://mpesa-requestbin.herokuapp.com/umieoxum",
      "AccountReference": "musa",
      "TransactionDesc": "musa"
}

response = requests.post(api_url, json = request, headers=headers)



if __name__ == '__main__':
app.run()