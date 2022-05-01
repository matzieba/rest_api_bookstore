import requests

book_id = input("what is the book id you want to use?\n")

try:
    book_id = int(book_id)
except:
    book_id = None
    print(f"{book_id} is not valid")

if book_id:
    endpoint =f"http://localhost:8000/api/books/{book_id}/delete/"
    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code==204)
