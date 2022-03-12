import requests
import json

headers = {
    'Authorization': 'Bearer 94da9a0e8e4d2afe6f7b876367d49b2df0f22e4c'
}

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This is mt new title",
    "price":32.99,
    
}
get_response = requests.post(endpoint, json = data, headers = headers)

print(get_response.json())
