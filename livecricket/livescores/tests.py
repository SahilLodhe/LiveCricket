from django.test import TestCase
import requests

# BASE_URL='http://127.0.0.8000' <<< Url with port malformed
BASE_URL='http://127.0.0.1:8000'
ENDPOINT='api/'
def get_resource():
    # resp=requests.get(BASE_URL+ENDPOINT)  <<< Request url malformed
    resp=requests.get(BASE_URL+"/"+ENDPOINT)
    print(resp.status_code)
    print(resp.json())
get_resource()
# Create your tests here.
