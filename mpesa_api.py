from flask import Flask, request, jsonify, make_response
from requests.auth import HTTPBasicAuth
import datetime
import time
import base64


app = Flask(__name__)


phone = 254725696042
amount = 1
business_short_code = 174379
timestamp = str(time.strftime('%Y%m%d%H%M%S'))


password = base64.b64encode(bytes(u'174379' + 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919' + timestamp, 'UTF-8'))

consumer_secret = "c5g00mKWmkcQBbm8TgANJBIqWAwKgsWS"
consumer_key = "kdazijKoybDgp0GH"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"


r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key,consumer_secret))
print(r.text)

access_token = "{}".format(r.text)
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = { "Authorization": "Bearer %s" % access_token }

payload = {
      "BusinessShortCode": "business_short_code",
      "Password": "password",
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