import requests


endpoint = "http://localhost:8000/api/books/1"


get_response = requests.get(endpoint, json = {"title":'kupa'})

print(get_response.json())