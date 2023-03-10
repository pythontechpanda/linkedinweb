# Generated by Django 4.1.5 on 2023-01-12 13:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Supplier', '0003_alter_createpost_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='createpost',
            name='helpful',
            field=models.ManyToManyField(blank=True, default=None, related_name='blog_help', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='createpost',
            name='insightful',
            field=models.ManyToManyField(blank=True, default=None, related_name='blog_insight', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='createpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 12, 18, 34, 16, 744596)),
        ),
        migrations.CreateModel(
            name='HelpPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valuehelp', models.CharField(choices=[('Helpful', 'Helpful'), ('Unhelpful', 'Unhelpful')], default='Like', max_length=10)),
                ('posthelp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supplier.createpost')),
                ('userhelp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
