import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"

username = input('what is your username? \n')
password = getpass('what is your passowrd? \n')
auth_response = requests.post(auth_endpoint, json={
    'username': username,
    'password': password
})
print(auth_response.json())

if auth_response.status_code == 200:
    endpoint = "http://localhost:8000/api/products/"
    token = auth_response.json()['token']

    data = {
        "title": "this is an addition to the database"
    }
    headers = {
        'Authorization': f'Token {token}'
    }
    get_response = requests.get(endpoint, json=data, headers=headers)
    print(get_response.json())