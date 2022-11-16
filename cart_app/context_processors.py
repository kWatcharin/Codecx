from cart_app.cart import Cart


def cart(request):

    cart = Cart(request)

    book_type_qty_in_cart = []
    for book in cart:
        book_type_qty_in_cart.append(book['book_id']['quantity'])

    total_books_qty = sum(book_type_qty_in_cart)
        
    context = {
        "cart": cart,
        "total_books_qty": total_books_qty,
        }
    return context
