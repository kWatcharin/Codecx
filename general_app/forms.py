from django import forms
from django.utils.translation import gettext_lazy as _

from general_app.models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    """The model of contact message from the contact person in about page."""

    class Meta:
        model = ContactMessage
        exclude = ['time_contact_message']
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'email': _('E-Mail'),
            'message': _('Topic-Message'),
            'message_detail': _('Message Detail')
        }


    def clean_first_name(self):

        first_name_data = self.cleaned_data['first_name'].title()
        if not first_name_data:
            raise forms.ValidationError(
                'Enter your "First name field!"'
                )
        
        return first_name_data


    def clean_last_name(self):

        last_name_data = self.cleaned_data['last_name'].title()
        if not last_name_data:
            raise forms.ValidationError(
                'Enter your "Last name field!"'
                )
        
        return last_name_data


    def clean_email(self):

        email_data = self.cleaned_data['email'].lower()
        if not email_data:
            raise forms.ValidationError(
                'Enter your "E-mail field!"'
            )

        return email_data

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'First Name'}
        )
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Last Name'}
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-Mail'}
        )
        self.fields['message'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Topic-Message'}
        )
        self.fields['message_detail'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Message Detail'}
        )


