import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "this is an addition to the database"
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())