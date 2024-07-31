from access_token import generate_access_token
import requests
import keys 

def register_url():
    

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"

    headers = {"Authorization": "Bearer %s" % generate_access_token()}

    request = {
        "ShortCode": keys.short_code,
        "ResponseType": "Completed",
        "ConfirmationURL":"https://mikeconfirmation.com",
        "ValidationURL":"https://mikevalidation.com"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

# register_url()   #registering urls once with daraja

def simulate_c2b_transaction():
    

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"

    headers = {"Authorization": "Bearer %s" % generate_access_token()}

    request = {
        "ShortCode": keys.short_code,
        "CommandID": "CustomerPayBillOnline",
        "Amount":"1",
        "Msisdn":keys.test_msisdn,
        "BillRefNumber":"12345678"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

simulate_c2b_transaction()