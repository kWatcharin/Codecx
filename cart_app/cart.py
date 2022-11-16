from decimal import Decimal
from django.conf import settings

from store_app.models import Book


class Cart():

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if settings.CART_SESSION_ID not in request.session:
            cart = request.session[settings.CART_SESSION_ID] = {}

        self.cart = cart


    def add(self, book, quantity, override_quantity=False):
        """Add a product to the cart or update its quantity."""

        book_id = str(book.id)
        if book_id not in self.cart:
            self.cart[book_id] = {'quantity': 0, 'price': book.premium_price}
        
        if override_quantity:
            self.cart[book_id]['quantity'] = quantity
        else:
            self.cart[book_id['qauntity']] += quantity

        self.save()


    def save(self):
        """Mark the session as "modified" to make sure if gets saved."""

        self.cart.modified = True
        

    def remove(self, book):
        """Remove the book from the cart."""

        book_id = str(book.id)
        if book_id in self.cart:
            del self.cart['book_id']
            self.save()


    def __iter__(self):
        """
        Ierate over the items in the carrt and get the books
        from the database.
        """

        book_ids = self.cart.keys()
        # Get the book objects and add them to cart.
        books = Book.objects.filter(id__in=book_ids)
        cart = self.cart.copy()

        for book in books:
            cart[str(book.id)]['book'] = book

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

        
    def __len__(self):
        """
        Count all item in the cart.
        """

        return sum(item['quantity'] for item in self.cart.values())


    def get_total_price(self):
        
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())


    def clear(self):
        """Remove cart form session."""

        del self.session[settings.CART_APP_ID]
        self.save()

    


        