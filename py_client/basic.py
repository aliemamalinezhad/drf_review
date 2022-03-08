import requests
import json

endpoint = "http://localhost:8000/api/"


get_response = requests.get(endpoint, json={"query": "Hello World"})



print(get_response.json())
