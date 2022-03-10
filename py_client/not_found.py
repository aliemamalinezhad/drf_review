import requests
import json

endpoint = "http://localhost:8000/api/products/4444444444/"


get_response = requests.get(endpoint)

print(get_response.json())
