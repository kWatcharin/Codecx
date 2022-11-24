from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from store_app.models import Book
from apis.serializers import BookSerializer


class BooksListApi(APIView):
    """
    API endpoint that allow users to be views.
    """
    
    def get(self, request, format=None, *args, **kwargs):

        books = Book.objects.all().filter(is_active=True)
        books_serializer = BookSerializer(books, many=True)
        return Response(books_serializer.data)


    def post(self, request, format=None, *args, **kwargs):

        request_serializer = BookSerializer(data=request.data)
        if request_serializer.is_valid():
            request_serializer.save()
            return Response(request_serializer.data, status=status.HTTP_201_CREATED)

        return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailApi(APIView):
    """
    API endpoint that allow users to be views.
    """

    def get(self, request, id):

        book = get_object_or_404(Book, id=id)
        book_detail_serializer = BookSerializer(book)

        return Response(book_detail_serializer.data)

    








