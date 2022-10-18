from django.urls import path
from store_app import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('books/', views.books_list, name='books'),
]

