import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(api_url)

json = response.json()
print('JSON response:', json)
print('Status Code:  ', response.status_code)
print('Content Type: ', response.headers["Content-Type"])


