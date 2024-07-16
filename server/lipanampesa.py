import base64
from datetime import datetime 


import requests

import keys



unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
# print(formatted_time)
# 20240716152601

data_to_encode = keys.business_shortCode +  keys.lipa_na_mpesa_passkey + formatted_time

encoded_string = base64.b64encode(data_to_encode.encode())
# print(encoded_string) b'MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjQwNzE2MTU0MjM2'

decoded_password= encoded_string.decode('utf-8')
print(decoded_password)





response = requests.request("GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers = { 'Authorization': 'Basic NHNncFp0ZHM3TWlkakxHUGFkQXFSVmlSYzhvYU9QZUR4aThaVVcyVWVFMFJFWVQ4OndIRUk0cW9ERzB1R2N6cXhIdlhpSnJ1eTZDMlJhN2UySnNIR0FJOENzQWtRbTJvTnRRcnZjYldjOERUSFliMzQ=' })

# print(response.json())
 

json_response = response.json() # {'access_token': 'ojslQT7okiHLKofeCVidWASwok2G', 'expires_in': '3599'}
my_access_token = json_response['access_token']

# print(my_access_token)

def lipa_na_mpesa():   

    access_token = my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {"Authorization": "Bearer %s" % access_token}

    request = {
        "BusinessShortCode": keys.business_shortCode,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": keys.phone_number,
        "PartyB": keys.business_shortCode,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://mikempesatst.com/",
        "AccountReference": "12345678",
        "TransactionDesc": "Pay School Fees",
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)


lipa_na_mpesa()



