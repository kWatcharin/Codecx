from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from store_app.models import Book


def homepage(request):
    books = Book.objects.all()
    # For new books and top hit books.
    new_books = [books[6], books[7], books[8], books[9]]
    top_hit_books = [books[0], books[1], books[2]]
    return render(request, 'store_app/homepage.html', {'new_books': new_books, 'top_hit_books': top_hit_books})


def books_list(request):
    books = Book.objects.all()

    paginator = Paginator(books, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'store_app/books_list.html', {'page_obj': page_obj})


def book_detail(request, slug):
    books = get_object_or_404(Book, slug=slug)
    return render(request, 'store_app/book_detail.html', {'books': books})







