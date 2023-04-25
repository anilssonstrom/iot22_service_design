import requests
import dotenv  # Kommer från paketet "python-dotenv"
import os

# Laddar in filen ".env" och gör att de miljövariablerna går att nå
dotenv.load_dotenv()

# Läs in miljövariabeln "NASA_API_KEY" från operativsystemet
API_KEY = os.getenv('NASA_API_KEY')

api_url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
response = requests.get(api_url)

print('JSON response:', response.json()['url'])
print('Status Code:  ', response.status_code)
print('Content Type: ', response.headers["Content-Type"])
