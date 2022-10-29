from django.forms import ModelForm
from general_app.models import ContactMessage


class ContactMessageForm(ModelForm):
    """The model of contact message from the contact person in about page."""

    class Meta:
        model = ContactMessage
        exclude = ['time_contact_message']

    