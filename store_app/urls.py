from django.urls import path

from store_app import views


app_name = 'store_app'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('books/', views.books_list, name='books_list'),
    path('book_id:<int:id>/<slug:slug>/', views.book_detail, name='book_detail'),
]
    
