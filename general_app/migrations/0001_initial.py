# Generated by Django 4.1.1 on 2022-10-29 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_person_first_name', models.CharField(blank=True, help_text='The first name of the contact person.', max_length=25, null=True)),
                ('contact_person_last_name', models.CharField(blank=True, help_text='The first name of the contact person.', max_length=25, null=True)),
                ('contact_person_email', models.EmailField(blank=True, help_text='The email of the contact person.', max_length=254, null=True)),
                ('perpose_message', models.CharField(blank=True, help_text='The perpose of the message tha contact person need to contact us.', max_length=50, null=True)),
                ('message_detail', models.TextField(blank=True, help_text='Th detail of the message for contact.', null=True)),
            ],
        ),
    ]
