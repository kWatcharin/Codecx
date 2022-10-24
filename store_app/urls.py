from django.urls import path
from store_app import views


# The varible for the argument in codecx/urls.py; namespace.
app_name = 'store_app'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('books/', views.books_list, name='books_list'),
    path('book/<slug:slug>/', views.book_detail, name='book_detail'),
]
