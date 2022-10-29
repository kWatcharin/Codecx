from django.db import models


class ContactMessage(models.Model):
    """The models of contaction from the contact person."""

    contact_person_first_name = models.CharField(max_length=25, null=True, blank=True)
    contact_person_last_name = models.CharField(max_length=25, null=True, blank=True)
    contact_person_email = models.EmailField(null=True, blank=True)
    contact_perpose_message = models.CharField(max_length=50, null=True, blank=True)
    contact_message_detail = models.TextField(null=True, blank=True)
    time_contact_message = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"""
            {self.contact_person_first_name},
            {self.contact_perpose_message},
            {self.contact_person_email},
            {self.time_contact_message},
        """