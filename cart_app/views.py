from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from cart_app.cart import Cart
from cart_app.forms import CartAddBookForm
from store_app.models import Book


@login_required
def cart_summary(request):
    """
    Template แสดง รายการ items ที่ user ทำการเลือกไว้ ต้องมีการ login อินเข้ามาถึงจะแสดงผลหน้านี้ให้ user เห็น
    """
    cart = Cart(request)
    context = {
        'cart': cart
    }
    return render(request, 'cart_app/cart_summary.html', context)


@require_POST
def cart_add(request, id):
    """
    สำหรับรับ Session ที่ user ส่งเข้ามาเพื่อบันทึก items ที่ user เลือกไว้ลงในตะกร้า
    """
    cart = Cart(request)
    book = get_object_or_404(Book, id=id)
    qty_selection_form = CartAddBookForm(request.POST)

    # ตรวจสอบและบันทึก
    if qty_selection_form.is_valid():
        qty_selection_form_cd = qty_selection_form.cleaned_data

        cart.add(
            book=book, quantity=qty_selection_form_cd['quantity'], 
            override_quantity=qty_selection_form_cd['override'])
    return redirect('cart_app:cart_summary')


@require_POST
def cart_remove(request, id):
    """
    สำหรับลบ Session ที่บันทึก items ไว้ในตะกร้า
    """
    cart = Cart(request)
    book = get_object_or_404(Book, id=id)

    cart.remove(book)
    return redirect('cart_app:cart_summary')
