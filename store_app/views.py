from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from store_app.models import Book


def homepage(request):

    books = Book.objects.all()

    # For new books and top hit books.
    return render(request, 'store_app/homepage.html')


def books_list(request):

    novels_list = Book.objects.all().order_by('-id').filter(is_active=True)
    all_novels = Book.objects.count()

    paginator = Paginator(novels_list, 12)
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
        }
    return render(request, 'store_app/books_list.html', context)


def book_detail(request, id, slug):

    book = get_object_or_404(Book, id=id, slug=slug)

    conntext = {'book': book}
    return render(request, 'store_app/book_detail.html', conntext)


