from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from apis.views import BooksListApi, BookDetailApi


app_name = 'apis'

urlpatterns =[
    path('books_list/', BooksListApi.as_view(), name='books_list_api'),
    path('book_id/<int:id>/', BookDetailApi.as_view(), name='book_detail_api'),
]

urlpatterns = format_suffix_patterns(urlpatterns) 