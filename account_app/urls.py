from django.urls import path
from django.contrib.auth import views as auth_views

from account_app import views
from account_app.forms import UserLoginForm

app_name ='account_app'

urlpatterns = [
    path('register/', views.account_register, name='register'),
    path('login/', auth_views.LoginView.as_view(
                                                template_name='account_app/registration/login.html',
                                                form_class=UserLoginForm), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
   
]