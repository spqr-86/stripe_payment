# Generated by Django 4.1 on 2023-02-12 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_item_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='currency',
        ),
    ]
