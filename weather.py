import requests

# End point
url = 'http://api.weatherapi.com/v1/current.json?key=311e6e4b91e142fcada73858232510&q=Manila&aqi=no'

# Response from API server
response = requests.get(url)

# resp_code = requests.Response.ok

# Stores Json
weather_json = response.json()

# temp = weather_json.get('current').get('temp_f')
# description = weather_json.get('current').get('condition').get('text')

# print("Today's weather in", city, 'is', description, 'and', temp, 'degrees')
temp_1 = requests.get('current')
temp_2 = requests.get('temp_f')



# print(weather_json)

print(temp_1)




