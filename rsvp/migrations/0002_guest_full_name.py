# Generated by Django 4.0 on 2022-02-02 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='full_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
