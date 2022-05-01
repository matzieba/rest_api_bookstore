from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

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


# List
class BookListAPIVIew(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


book_list_view = BookListAPIVIew.as_view()

# Details

# class BookDetailAPIVIew(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'pk'
#
# book_detail_view = BookDetailAPIVIew.as_view()

# Update

class BookUpdateAPIVIew(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

    def perform_update(self,serializer):
        instance = serializer.save()

book_update_view = BookUpdateAPIVIew.as_view()

#Delete

class BookDestroyAPIVIew(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

book_destroy_view = BookDestroyAPIVIew.as_view()

