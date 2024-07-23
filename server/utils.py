
from datetime import datetime 
import requests
import keys


def convert_time():
    unformatted_time = datetime.now()
    formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
    return formatted_time