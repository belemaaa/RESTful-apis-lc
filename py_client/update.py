import requests

endpoint = "http://localhost:8000/api/products/2/update/"

data = {
    "title": "an updated item",
    "price": 5.88
}
get_response = requests.put(endpoint, json=data)
print(get_response.json())