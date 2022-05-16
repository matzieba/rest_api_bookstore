from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from .models import Book
from .serializers import BookSerializer

# Create
class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        authors = serializer.validated_data.get('authors')
        acquired = serializer.validated_data.get('acquired')
        published_year = serializer.validated_data.get('published_year')
        serializer.save()

book_create_view = BookCreateAPIView.as_view()


# List + List filtering
class BookListAPIVIew(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        params = self.request.query_params
        if params:
            #setting up the filter values
            authors_list = Book.objects.values_list('authors', flat=True)
            filter_dict = {}
            if params.get('author'):
                author = params.get('author')[1:][:-1]
                filter_para_author =''
                for authors in authors_list:
                    if author in authors:
                        filter_para_author = authors
                filter_dict['authors'] = filter_para_author
            if params.get('from'):
                date_from = params.get('from')
                filter_dict['published_year__gte'] = date_from
            if params.get('to'):
                date_to = params.get('to')
                filter_dict['published_year__lte'] = date_to
            if params.get('acquired'):
                acquired = params.get('acquired').capitalize()
                filter_dict['acquired'] = acquired
            if params.get('title'):
                title = params.get('title')
                filter_dict['title'] = title
            queryset = Book.objects.filter(**filter_dict)
            return queryset
        else:
            return Book.objects.all()

book_list_view = BookListAPIVIew.as_view()


# Retrive, Update, Delete
class ProductMixinView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
    ):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

product_mixin_view = ProductMixinView.as_view()

# import + create/update

@api_view(['POST'])
def book_import_view(request):
    url = f'https://www.googleapis.com/books/v1/volumes?q={request.data}'
    response = requests.get(url)
    counter_new = 0
    authors = ""
    for item in response.json()['items']:
        try:
            for author in item['volumeInfo']['authors']:
                authors += author + " "
        except KeyError:
            continue
        try:
            book = {
                'title':item['volumeInfo']['title'],
                'authors':authors,
                'acquired':False,
                'published_year':int(item['volumeInfo']['publishedDate'][0:4])
            }
            authors = ""
        except KeyError:
            continue
        if Book.objects.filter(title=book['title']).exists():
            Book.objects.filter(title=book['title']).update(
                **book)
        else:
            serializer = BookSerializer(data=book)
            if (serializer.is_valid()):
                serializer.save()
                counter_new +=1
            else:
                return Response(serializer.errors)
    return Response({'imported':counter_new})

class ProductMixinView(
    generics.GenericAPIView
    ):
    def post(self, request):
        url = f'https://www.googleapis.com/books/v1/volumes?q={request.data}'
        response = requests.get(url)
        counter_new = 0
        authors = ""
        for item in response.json()['items']:
            try:
                for author in item['volumeInfo']['authors']:
                    authors += author + " "
            except KeyError:
                continue
            try:
                book = {
                    'title': item['volumeInfo']['title'],
                    'authors': authors,
                    'acquired': False,
                    'published_year': int(item['volumeInfo']['publishedDate'][0:4])
                }
                authors = ""
            except KeyError:
                continue
        if Book.objects.filter(title = book['title']).exists():
            Book.objects.filter(title = book['title']).update(
                    **book)
        else:
            serializer = BookSerializer(data=book)
        if (serializer.is_valid()):
            serializer.save()
            counter_new += 1
            return Response(True)
        else:
            return Response(serializer.errors)
        return Response({'imported': counter_new})


