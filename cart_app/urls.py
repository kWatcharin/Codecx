from django.urls import path
from cart_app import views


app_name = 'cart_app'

urlpatterns = [
    path('cart_summary/', views.cart_summary, name='cart_summary'),
    path('cart_add/', views.cart_add, name='cart_add'),
]