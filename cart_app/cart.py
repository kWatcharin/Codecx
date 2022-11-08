


class Cart():
    """A base cart class, provide some default that can be
    inherited or overrided, as necessary."""

    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('skey')
        
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        
        self.cart = cart

        self.session.modified = True

    def add(self, book):
        
        book_id = str(book.id)
        if book_id in self.cart:
            self.cart[book_id] = {'price': str(book.premium_price)}

        self.session.modified = True   
        