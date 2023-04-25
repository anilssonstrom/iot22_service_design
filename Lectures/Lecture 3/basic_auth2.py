import requests

api_url = "https://postman-echo.com/basic-auth"
header = {"Authorization": "Basic cG9zdG1hbjpwYXNzd29yZA=="}
response = requests.get(api_url, headers=header)

print(response.status_code)
if response.status_code == 200:
    print(response.json())
else:
    print("oops")
