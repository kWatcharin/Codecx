from django.shortcuts import render


def about_us(request):
    return render(request, 'general_app/about_us.html')