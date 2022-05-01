import requests

endpoint ="http://localhost:8000/api/books/1/update/"

data = {
    "title":"Hello world",
    "authors": "My old friend",
    "acquired": True,
    "published_year" : "2018"

}
get_response = requests.put(endpoint, json = data)

print(get_response.json())
