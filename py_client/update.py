import requests
import json

endpoint = "http://localhost:8000/api/products/2/update/"

data = {
    "title": "Hello world my friend",
    "price": 42.99,

}
get_response = requests.put(endpoint, json=data)

print(get_response.json())
