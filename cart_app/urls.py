from django.urls import path
from cart_app import views


app_name = 'cart_app'

urlpatterns = [
    path('summary/', views.cart_summary, name='cart_summary'),
    path('add/', views.cart_add, name='cart_add'),
]