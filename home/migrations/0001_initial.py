# Generated by Django 2.2.10 on 2021-02-05 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributer_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('profile_picture', models.FileField(blank=True, upload_to='uploads/')),
                ('profession', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=60)),
                ('facebook', models.URLField(blank=True, max_length=60)),
                ('about_me', models.TextField(blank=True)),
                ('total_money', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contributer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]