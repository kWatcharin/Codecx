from cart_app.cart import Cart


def cart(request):

    cart = Cart(request)
    item_quantity = []
    item_price = []
    
    for item in cart:
        item_quantity.append(item['quantity'])
        item_price.append(item['total_price'])

    total_books_qty = sum(item_quantity)
    total_books_price = sum(item_price)

    context = {
        "cart": cart,
        "total_books_qty": total_books_qty, # แสดงผลทั้งหมดของจำนวน items session ที่ user ได้เลือกไว้ ออกไปยัง template 
        "total_books_price": total_books_price, # แสดงผลราคารวมทั้งหมด items session ที่ user ได้เลือกไว้ ออกไปยัง template 
    }
    return context
