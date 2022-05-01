import requests

endpoint = "http://localhost:8000/api/books/list"



get_response = requests.get(endpoint)
print(get_response.json())