import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos"
new_todo = {
    "userId": 1,
    "title": "Buy milk",
    "completed": False
}
headers = {"Content-Type": "application/json"}

response = requests.post(api_url,
                         data=json.dumps(new_todo),
                         headers=headers)

print('JSON response:', response.json())
print('Status Code:  ', response.status_code)
