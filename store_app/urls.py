from django.urls import path
from store_app import views

urlpatterns = [
    path('', views.index, name='index'),
]

