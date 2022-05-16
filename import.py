import requests

endpoint = "http://localhost:8000/books/import"

data = {
    "author":"konopnicka"
}

get_response = requests.post(endpoint, json = data)
print(get_response.json())