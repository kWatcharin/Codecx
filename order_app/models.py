from django.db import models
from django.conf import settings

from store_app.models import Book


ORDER_STATUS = [
     ('Created', 'created'),
     ('Already Paid', 'already paid'),
     ('Preparing', 'preparing'),
     ('Out of shiped', 'out of shiped'),
     ('Cancel', 'cancel'),
     ('Completed', 'completed')
]


TRANSPORTATION_METHOD = [
     ('Courier delivery', 'courier delivery'),
     ('Recipient pickup', 'recipient pickup')
]


class Order(models.Model):

     user = models.ForeignKey(
          settings.AUTH_USER_MODEL, 
          on_delete=models.CASCADE,
          related_name='user_order'
          )
     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     email = models.EmailField()
     mobile_numbers = models.CharField(max_length=15)
     address1 = models.CharField(max_length=250)
     address2 = models.CharField(max_length=250, blank=True, null=True)
     postral_code = models.CharField(max_length=20)
     city = models.CharField(max_length=100)
     total_paid = models.DecimalField(max_digits=6, decimal_places=2)
     is_paid = models.BooleanField(default=False)
     time_created = models.DateTimeField(auto_now_add=True)
     time_update = models.DateTimeField(auto_now=True)
     order_status = models.CharField(max_length=20, choices=ORDER_STATUS, default='Created')
     order_note = models.TextField(null=True, blank=True)
     transport = models.CharField(max_length=20, choices=TRANSPORTATION_METHOD, default='Courier delivery')
     transport_cost = models.DecimalField(max_digits=5, decimal_places=2)

     class Meta:
          ordering = ['-time_created']
    
     def __str__(self):
          return f"""
          {self.first_name},
          {self.email},
          {self.time_created}
          """

     def get_total_cost(self):
          total_cost = sum(item.get_cost() for item in self.items.all())
          total_cost += self.transport_cost
          return total_cost


class OrderItem(models.Model):

     order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
     book = models.ForeignKey(Book, related_name='order_items', on_delete=models.CASCADE)
     price = models.DecimalField(max_digits=6, decimal_places=2)
     quantity= models.PositiveIntegerField(default=1)

     def __str__(self):
          return f"{self.id}"
     
     def get_cost(self):
          return self.price * self.quantity