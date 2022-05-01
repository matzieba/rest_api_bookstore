import requests
import datetime

endpoint = "http://localhost:8000/api/books/"

data = {
    "title":"this is title",
    "authors":"this is author",
    "acquired":False,
    "published_year": '2001'
}

get_response = requests.post(endpoint, json = data)
print(get_response.json())

