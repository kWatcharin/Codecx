from django.urls import path
from store_app import views

urlpatterns = [
    path('', views.store_base_app, name='store_base_app'),
    path('show_static/', views.show_static, name='show_static')
]

