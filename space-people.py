# # JSON can be a mix of lists and dictionaries
# # JSON Format to exhange data to/from a web server
# # HTTP request ---------->
# # HTTP response <---------------
# # API
# # Python Package Index

# # requests package
# import requests

# # GET request
# response = requests.get('http://api.open-notify.org/astros.json')

# # decode the JSON from the response, convert JSON to Dictionary
# json = response.json()

# # print(json)


# print('People in space currently: ')
# # people - key
# for person in json['people']:
#     print(person['name'])  # name - value
