from django.urls import path
from general_app import views


# The varible for the attribute in codecx/urls.py; namespace.
app_name = 'general_app'

urlpatterns = [
    path('about_us/', views.about_us, name='about_us'),
]