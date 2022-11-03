from django.shortcuts import render


def cart_summary(request):
    return render(request, 'cart_app/cart_summary.html')


def cart_add(request):
    return render(request, 'cart_app/cart_add.html')
