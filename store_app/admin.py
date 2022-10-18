from django.contrib import admin
from store_app.models import Publisher, Contributor, Artist, BookLanguage
from store_app.models import StockStatus, BookCategory, Book


class PublisherAdmin(admin.ModelAdmin):
    """A model admin for admin's publisher."""

    publisher_admin = (
        'publisher_title',
        'website',
        'email',
    )

admin.site.register(Publisher, PublisherAdmin)


class ContrbutorAdmin(admin.ModelAdmin):
    """A class for admin's contributor."""

    contributor_admin = (
        'contributor_title',
    )

admin.site.register(Contributor, ContrbutorAdmin)


class ArtistAdmin(admin.ModelAdmin):
    """A class for admin's artist."""

    artist_admin = (
        'artist_title',
    )

admin.site.register(Artist, ArtistAdmin)


class BookLanguageAdmin(admin.ModelAdmin):
    """A class for admin's language of book."""

    book_language_admin = (
        'book_language_select',
    )

admin.site.register(BookLanguage, BookLanguageAdmin)


class BookCategoryAdmin(admin.ModelAdmin):
    """A class for admin's category of the book."""

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
    """A class for admin's stock status."""

    stock_status_admin = (
        'stock_status',
    )

admin.site.register(StockStatus, StockStatusAdmin)

class BookAdmin(admin.ModelAdmin):
    """A class for admin's book(lightnovel)."""

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
