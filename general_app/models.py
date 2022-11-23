from django.db import models


class ContactMessage(models.Model):
    """The models of contaction from the contact person."""

    first_name = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.CharField(max_length=50, null=True, blank=True)
    message_detail = models.TextField(null=True, blank=True)
    time_contact_message = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"""
            {self.first_name},
            {self.last_name},
            {self.message},
            {self.email},
            {self.time_contact_message},
        """