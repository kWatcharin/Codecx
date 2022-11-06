from django.shortcuts import render, get_object_or_404

from cart_app.cart import Cart
from store_app.models import Book

def cart_summary(request):
    return render(request, 'cart_app/cart_summary.html')


def cart_add(request):
    
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        book_id = int(request.POST.get('bookid'))
        book = get_object_or_404(Book, book_id)
        cart.add(book=book)
