# Generated by Django 4.0 on 2022-02-04 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0002_guest_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
