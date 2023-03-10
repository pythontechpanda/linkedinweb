# Generated by Django 4.1.5 on 2023-01-12 09:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='users',
            field=models.ManyToManyField(blank=True, help_text='user who are connected to the chat', to=settings.AUTH_USER_MODEL),
        ),
    ]
