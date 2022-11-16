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


    def add(self):
        pass
        
        