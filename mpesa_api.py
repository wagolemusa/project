#from flask import Flask, jsonify, make_response
import requests
from requests.auth import HTTPBasicAuth
import datetime
import time
import base64
import json


#app = Flask(__name__)

"""
@app.route('/mpesa', methods= ['POST'])
def api_message():
      data = request.data
      print(data)
      return "already run"
      """

phone = 254725696042 
amount = 1            
business_short_code = 174379 
timestamp = str(time.strftime('%Y%m%d%H%M%S'))  

# generating password
def password_generater(word):
      return base64.b64encode(word,'utf-8')
password_generater('174379' + 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919' + timestamp)

# Get access token
consumer_key = "c5g00mKWmkcQBbm8TgANJBIqWAwKgsWS"
consumer_secret = "kdazijKoybDgp0GH"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key,consumer_secret))



access_token=json.loads(r.text)['access_token']
print(access_token)
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = { "Authorization": "Bearer "+access_token}

request = {
      "BusinessShortCode": business_short_code,
      "Password": password_generater('174379' + 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919' + timestamp)
,
      "Timestamp": timestamp,
      "TransactionType": "CustomerPayBillOnline",
      "Amount": amount,
      "PartyA": phone,
      "PartyB": business_short_code,
      "PhoneNumber": phone,
      "CallBackURL": "http://mpesa-requestbin.herokuapp.com/1o3m1t31",
      "AccountReference": "musa",
      "TransactionDesc": "musa"
}

response = requests.post(api_url, json = request, headers=headers)

print (response.text)
"""
if __name__ == '__main__':
      app.run()
      """