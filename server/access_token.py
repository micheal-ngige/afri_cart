

from requests.auth import HTTPBasicAuth

import requests

import keys





def generate_access_token():

    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(api_url, auth= HTTPBasicAuth(consumer_key, consumer_secret))

    # print(response.json())
    

    json_response = response.json() # {'access_token': 'ojslQT7okiHLKofeCVidWASwok2G', 'expires_in': '3599'}
    my_access_token = json_response['access_token'] 

  
    return my_access_token
