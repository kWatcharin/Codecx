from django.shortcuts import render, get_object_or_404
from store_app.models import Book, Publisher



def publishers(request):
    """The function for retrieve the Publisher model for all the templates."""
    return {
        'publishers': Publisher.objects.all()
    }


def books(request):
    """The function for retrieve the Book model for all the templates."""
    return {
        'books': Book.objects.all()
    }


def homepage(request):
    return render(request, 'store_app/homepage.html')


def books_list(request):
    return render(request, 'store_app/books_list.html')


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'store_app/books_list.html')







