# Generated by Django 2.2.10 on 2021-02-07 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20210207_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributer',
            name='created_on',
            field=models.DateTimeField(),
        ),
    ]