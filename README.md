# rest_api_bookstore
Django REST API
## made wtih django rest framework

### DOCU
GET
make a GET  request an /books to get the list of all books in DB
make a GET  request an /books/{id} to get the detailed info about book
make a GET  request an /books providing following params:
    author,date of publisching from, date of publisching to, acquired
to filter the resoults according to specyfication

PATCH
make a PATCH request an /books/{id} to update data in DB

DELETE
make a PATCH request an /books/{id} to delete a book

POST
make a POST request an /books/import providing following params:
  'author':'desiredauthorname'
to import or/and update the posisions in your DB
