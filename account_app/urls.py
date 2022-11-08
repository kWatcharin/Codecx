from django.urls import path
from account_app import views

app_name ='account_app'

urlpatterns = [
    path('register/', views.account_register, name='register'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
   
]