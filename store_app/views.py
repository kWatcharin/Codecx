from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from store_app.models import Book
from cart_app.forms import CartAddBookForm


def homepage(request):
    """
    Homepage
    """
    new_books = Book.objects.all().filter(is_active=True).order_by('-id')[0:4] #แสดงผลหนังสือใหม่ 4 เล่มล่าสุด
    top_hit_books = Book.objects.all().filter(is_active=True).order_by('id')[0:3] #ยกตัวอย่างแสดงผลหนังสือ จำนวน 3 เล่ม
    
    context = {
        'new_books': new_books,
        'top_hit_books': top_hit_books
    }
    return render(request, 'store_app/homepage.html', context)


def books_list(request):
    """
    Books list page.
    """
    is_actived_novels = Book.objects.all().filter(is_active=True).order_by('-id')
    all_novels = Book.objects.filter(is_active=True).count()

    # แบ่งจำนวนหน้าให้แสดงผล 12 objects ต่อ page
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
        }
    return render(request, 'store_app/books_list.html', context)


def book_detail(request, id, slug):
    """
    Book object's detail page.
    """
    #รับค่า id, slug ที่ส่งมาจาก url มา query หา object ที่เกี่ยวข้องในโมเดล แล้ว ส่งออกไปแสดงผล ใน template book_detail.html
    book = get_object_or_404(Book, id=id, slug=slug, is_active=True)
    cart_book_form = CartAddBookForm()

    conntext = {
        'book': book,
        'cart_book_form': cart_book_form
        }
    return render(request, 'store_app/book_detail.html', conntext)


