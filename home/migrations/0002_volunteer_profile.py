# Generated by Django 2.2.10 on 2021-02-05 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('profile_picture', models.FileField(blank=True, upload_to='uploads/')),
                ('address', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=60)),
                ('facebook', models.URLField(blank=True, max_length=60)),
                ('about_me', models.TextField(blank=True)),
                ('total_points', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='volunteer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
