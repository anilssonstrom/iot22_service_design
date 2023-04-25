import requests

api_url = "https://jsonplaceholder.typicode.com/todos"
new_todo = {
    "userId": 1,
    "title": "Buy milk",
    "completed": False
}

response = requests.post(api_url, json=new_todo)

print('JSON response:', response.json())
print('Status Code:  ', response.status_code)
