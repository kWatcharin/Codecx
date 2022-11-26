from django.contrib import admin

from order_app.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):

     model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

     list_display = [
          'id',
          'user',
          'first_name',
          'email',
          'address1',
          'address2',
          'postral_code',
          'city',
          'total_paid',
          'is_paid',
          'order_status',
          'order_note',
          'transport',
          'transport_cost'
     ]

     list_filter = [
          'time_created',
          'time_update',
     ]

     inlines = [OrderItemInline]
