# Generated by Django 3.1.5 on 2021-05-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_auto_20210518_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='headline',
            field=models.TextField(max_length=20),
        ),
    ]