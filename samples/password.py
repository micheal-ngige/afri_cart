import base64
import keys

def generate_password(formatted_time):

 

    data_to_encode = keys.business_shortCode +  keys.lipa_na_mpesa_passkey + formatted_time

    encoded_string = base64.b64encode(data_to_encode.encode())
    # print(encoded_string) b'MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjQwNzE2MTU0MjM2'

    decoded_password= encoded_string.decode('utf-8')
    # print(decoded_password)
     
    return decoded_password