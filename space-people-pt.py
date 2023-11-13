# JSON can be a mix of lists and dictionaries
# JSON Format to exhange data to/from a web server
# HTTP request ----------> 
# HTTP response <---------------
# API
# Python Package Index

# requests package
import requests
import json

# GET request
response = requests.get('http://api.open-notify.org/astros.json')

# decode the JSON from the response, convert JSON to Dictionary
response_dict = response.json()

# Status Code
status_code = requests.status_codes

pretty_print = json.dumps(response_dict, indent=4, sort_keys=True)

# Pretty Printing JSON string back
# print(json.dumps(response_dict, indent=4, sort_keys=True))

print('JSON: ')
print(status_code)
print(pretty_print)

