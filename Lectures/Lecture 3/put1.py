import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"

response = requests.get(api_url)
print('JSON response:', response.json())

new_todo = {
    "userId": 4,
    "title": "Wash car",
    "completed": True
}

response = requests.put(api_url, json=new_todo)

print('JSON response:', response.json())
print('Status Code:  ', response.status_code)
