import requests

# Använd filen app_secrets.py för att lagra hemligheter som inte ska upp till GitHub
import app_secrets

# app_secrets.py innehåller:
# nasa_api_key = 'din hemliga nyckel'

# Använd hemligheten
api_url = f"https://api.nasa.gov/planetary/apod?api_key={app_secrets.nasa_api_key}"

response = requests.get(api_url)

print('JSON response:', response.json()['url'])
print('Status Code:  ', response.status_code)
print('Content Type: ', response.headers["Content-Type"])
