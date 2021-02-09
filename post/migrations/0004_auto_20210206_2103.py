# Generated by Django 2.2.10 on 2021-02-06 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0003_auto_20210206_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='react',
            name='quantity',
        ),
        migrations.AddField(
            model_name='react',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
