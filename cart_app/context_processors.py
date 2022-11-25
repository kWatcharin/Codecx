from cart_app.cart import Cart


def cart(request):

    cart = Cart(request)
    item_quantity = []
    
    for item in cart:
        item_quantity.append(item['quantity'])

    total_books_qty = sum(item_quantity)
        
    context = {
        "cart": cart,
        "total_books_qty": total_books_qty,
    }
    return context
