import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "this is an addition to the database"
}
get_response = requests.get(endpoint, json=data)
print(get_response.json())