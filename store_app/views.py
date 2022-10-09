from django.shortcuts import render


# Create your views here.
def store_base_app(request):
    return render(request, 'store_app/components/store_app_base.html')


def show_static(request):
    return render(request, 'store_app/show_static.html')



