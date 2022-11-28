from store_app.models import Book, Publisher


def publishers(request):
    """ฟังก์ชันสำหรับเรียกใช้งาน แสดงผล objects สำนักพิมพ์ทั้งหมดใน template อื่นๆ"""
    return {
        'publishers': Publisher.objects.all()
    }


def books(request):
    """ฟังก์ชันสำหรับเรียกใช้งาน แสดงผล objects หนังสือทั้งหมดใน template อื่นๆ"""
    return {
        'books': Book.objects.all()
    }