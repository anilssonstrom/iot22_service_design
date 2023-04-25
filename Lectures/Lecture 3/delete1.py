import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"

response = requests.delete(api_url)

print('JSON response:', response.json())
print('Status Code:  ', response.status_code)
