import requests

city = 'London'
url = 'http://api.weatherapi.com/v1/current.json?key=311e6e4b91e142fcada73858232510&q='+city+'&aqi=no'
response = requests.get(url)
weather_json = response.json()
status_code = response.status_code


try:
    data = response.json()
except ValueError:
    print('Response content is not valid JSON')

# print(f'HTTP Status Code: {status_code}')

'''
if status_code == 200:

    try:
        data = response.json() 
        print('JSON data received', data)
        print('Request was successful.')

    except requests.exceptions.JSONDecodeError:
        print('Response is not valid JSON')

else:
    print(f'Request was not succesful. Status Code: {status_code}')
'''

# print('JSON Response: ')
print(weather_json)









'''
if response.status_code == 200:
    # Check if the response contains data before trying to parse it
    if response.text:
        try:
            # Try to parse the JSON response
            data = response.json()
            print('JSON data received:', data)
        except ValueError:
            # Handle the case where the response is not valid JSON
            print('Response is not valid JSON')
    else:
        print('Response is empty')
else:
    # Handle other HTTP status codes (e.g., 404, 500)
    print(f'Request was not successful. Status code: {response.status_code}')
'''