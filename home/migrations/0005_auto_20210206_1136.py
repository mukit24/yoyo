# Generated by Django 2.2.10 on 2021-02-06 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210206_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributer_profile',
            name='profile_picture',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
