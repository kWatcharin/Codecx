# Generated by Django 4.1.1 on 2022-10-29 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_app', '0003_contactmessage_time_contact_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='time_contact_message',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]