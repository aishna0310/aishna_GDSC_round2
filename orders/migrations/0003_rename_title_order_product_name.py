# Generated by Django 4.2.6 on 2023-10-27 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='title',
            new_name='product_name',
        ),
    ]
