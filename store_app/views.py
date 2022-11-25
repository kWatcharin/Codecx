from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from store_app.models import Book
from cart_app.forms import CartAddBookForm


def homepage(request):
    """
    Homepage
    """
    new_books = Book.objects.all().filter(is_active=True).order_by('-id')[0:4]
    top_hit_books = Book.objects.all().filter(is_active=True).order_by('id')[0:3]
    cart_book_form = CartAddBookForm()
    
    context = {
        'new_books': new_books,
        'top_hit_books': top_hit_books,
        'cart_book_form': cart_book_form
    }
    return render(request, 'store_app/homepage.html', context)


def books_list(request):
    """
    List of the book that is actived.
    """
    is_actived_novels = Book.objects.all().filter(is_active=True).order_by('-id')
    all_novels = Book.objects.filter(is_active=True).count()
    cart_book_form = CartAddBookForm()

    paginator = Paginator(is_actived_novels, 12)
    page = request.GET.get('page', 1)
    try:
        novels = paginator.page(page)
    except PageNotAnInteger:
        novels = paginator.page(1)
    except EmptyPage:
        novels = paginator.page(paginator.num_pages)
   
    context = {
        'all_novels': all_novels,
        'novels': novels,
        'cart_book_form': cart_book_form
        }
    return render(request, 'store_app/books_list.html', context)


def book_detail(request, id, slug):
    """
    Detail page of the book object.
    """
    book = get_object_or_404(Book, id=id, slug=slug, is_active=True)
    cart_book_form = CartAddBookForm()

    conntext = {
        'book': book,
        'cart_book_form': cart_book_form
        }
    return render(request, 'store_app/book_detail.html', conntext)


