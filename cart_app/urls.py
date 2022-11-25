from django.urls import path
from cart_app import views


app_name = 'cart_app'

urlpatterns = [
    path('', views.cart_summary, name='cart_summary'),
    path('add/<int:id>/', views.cart_add, name='cart_add'),
    path('remove/<int:id>/', views.cart_remove, name='cart_remove'),
]
