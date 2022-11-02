from django.contrib import admin

from general_app.models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    """A model admin for admin's ContactMessage."""
    
    contact_message_admin = (
        'contact_person_first_name',
        'contact_person_last_name',
        'contact_person_email',
        'contact_perpose_message',
        'contact_message_detail',
        'time_contact_message',
    )

admin.site.register(ContactMessage, ContactMessageAdmin)