import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={
    "name": "grace",
})
print(get_response.json())