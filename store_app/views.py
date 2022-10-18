from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'store_app/homepage.html')


def books_list(request):
    return render(request, 'store_app/books-list.html')


