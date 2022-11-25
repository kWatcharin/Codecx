from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from cart_app.cart import Cart
from cart_app.forms import CartAddBookForm
from store_app.models import Book


@login_required
def cart_summary(request):
    """Display the book that was chosen by the user."""
    cart = Cart(request)
    for item in cart:
        item['update_quantity'] = CartAddBookForm(
            initial={
                'quantity': item['quantity'],
                'override': True
            }
        )
    context = {
        'cart': cart
    }
    return render(request, 'cart_app/cart_summary.html', context)


@require_POST
def cart_add(request, id):

    cart = Cart(request)
    book = get_object_or_404(Book, id=id)
    qty_selection_form = CartAddBookForm(request.POST)

    if qty_selection_form.is_valid():
        qty_selection_form_cd = qty_selection_form.cleaned_data

        cart.add(
            book=book, quantity=qty_selection_form_cd['quantity'], 
            override_quantity=qty_selection_form_cd['override'])
    return redirect('cart_app:cart_summary')


@require_POST
def cart_remove(request, id):

    cart = Cart(request)
    book = get_object_or_404(Book, id=id)

    cart.remove(book)
    return redirect('cart_app:cart_summary')
