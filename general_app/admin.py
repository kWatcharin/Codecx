from django.contrib import admin

from general_app.models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    """A model admin for admin's ContactMessage."""
    
    contact_message_admin = (
        'first_name',
        'last_name',
        'email',
        'message',
        'message_detail',
        'time_contact_message',
    )

admin.site.register(ContactMessage, ContactMessageAdmin)