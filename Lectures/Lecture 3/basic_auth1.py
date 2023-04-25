import requests

api_url = "https://postman-echo.com/basic-auth"
username = "postman"
password = "password"
response = requests.get(api_url, auth=(username, password))

print(response.json())
print(response.status_code)
