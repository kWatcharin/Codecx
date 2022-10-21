from django.shortcuts import render, get_object_or_404
from store_app.models import Book, Publisher, BookCategory



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
    book_categories = BookCategory.objects.all()
    return render(request, 'store_app/homepage.html', {'book_categories': book_categories})


def books_list(request):
    return render(request, 'store_app/books_list.html')


def book_detail(request, slug):
    books = get_object_or_404(Book, slug=slug)
    return render(request, 'store_app/books_list.html')







