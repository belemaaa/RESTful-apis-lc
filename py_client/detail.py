import requests

endpoint = "http://localhost:8000/api/products/2"

get_response = requests.get(endpoint, json={'title': 'Hello world', 'content': 'a good day'})
print(get_response.json())