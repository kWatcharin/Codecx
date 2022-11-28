from django.contrib import admin

from store_app.models import (
    Publisher, Contributor, Artist, BookLanguage, StockStatus, BookCategory, Book
)
 

class PublisherAdmin(admin.ModelAdmin):
    """ModelAdmin: สำนักพิมพ์"""
    publisher_admin = (
        'publisher_title',
        'website',
        'email',
    )
admin.site.register(Publisher, PublisherAdmin)


class ContrbutorAdmin(admin.ModelAdmin):
    """ModelAdmin: ผู้แต่ง"""
    contributor_admin = (
        'contributor_title',
    )
admin.site.register(Contributor, ContrbutorAdmin)


class ArtistAdmin(admin.ModelAdmin):
    """ModelAdmin: อาร์ทติสค์"""

    artist_admin = (
        'artist_title',
    )
admin.site.register(Artist, ArtistAdmin)


class BookLanguageAdmin(admin.ModelAdmin):
    """ModelAdmin: ภาษา"""

    book_language_admin = (
        'book_language_select',
    )
admin.site.register(BookLanguage, BookLanguageAdmin)


class BookCategoryAdmin(admin.ModelAdmin):
    """ModelAdmin: ภาษา"""

    lightnovel_category_admin = (
        'book_category_tag_label',
        'book_category_tag_1st',
        'book_category_tag_2st',
        'book_category_tag_3st',
        'book_category_tag_4st',
        'book_category_tag_5st',
        )
admin.site.register(BookCategory, BookCategoryAdmin)


class StockStatusAdmin(admin.ModelAdmin):
    """ModelAdmin: สถานะ Stock"""

    stock_status_admin = (
        'stock_status',
    )
admin.site.register(StockStatus, StockStatusAdmin)


class BookAdmin(admin.ModelAdmin):
    """ModelAdmin: หนังสือ"""
    book_admin_display_list = (
        'image'
        'book_title_eng', 
        'book_title_jp',
        'volume_no'
        'contributor',
        'artist',
        'book_categories'
    )
admin.site.register(Book, BookAdmin)
