# Generated by Django 4.2.6 on 2023-10-27 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_rename_title_order_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='priority',
            field=models.CharField(max_length=50),
        ),
    ]
