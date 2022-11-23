from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response


from store_app.models import Book
from apis.serializers import BookSerializers


class BooksListApi(APIView):
    
    def get(self, request):

        books = Book.objects.all().filter(is_active=True)
        data_pattern = BookSerializers(books, many=True).data

        return Response(data_pattern)


class BookDetailApi(APIView):

    def get(self, request, id):

        book = get_object_or_404(Book, id=id)
        data_pattern = BookSerializers(book).data

        return Response(data_pattern)

