from django.contrib import admin
from store_app.models import Publisher, Contributor, Artist, LanguagesLightnovel
from store_app.models import StockStatus, LightnovelCategory, Lightnovel

# Register your models here.

class PublisherAdmin(admin.ModelAdmin):
    """A class for admin's publisher."""

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


class LanguageLightnovelAdmin(admin.ModelAdmin):
    """A class for admin's language lightnovel."""

    language_lightnovel_admin = (
        'language_lightnovel_select',
    )

admin.site.register(LanguagesLightnovel, LanguageLightnovelAdmin)


class LightnovelCategoryAdmin(admin.ModelAdmin):
    """A class for admin's lightnovel category."""

    lightnovel_category_admin = (
        'lightnovel_1st_category',
        'lightnovel_2nd_category',
        'lightnovel_3rd_category',
        'lightnovel_4th_category',
        'lightnovel_5th_category',
        'lightnovel_tag_label'
        )

admin.site.register(LightnovelCategory, LightnovelCategoryAdmin)


class StockStatusAdmin(admin.ModelAdmin):
    """A class for admin's stock status."""

    stock_status_admin = (
        'stock_status',
    )

admin.site.register(StockStatus, StockStatusAdmin)

class LightnovelAdmin(admin.ModelAdmin):
    """A class for admin's book."""

    book_admin_display_list = (
        'image'
        'lightnovel_title_eng', 
        'lightnovel_title_jp',
        'volume_no'
        'contributor',
        'artist'
    )

admin.site.register(Lightnovel, LightnovelAdmin)
