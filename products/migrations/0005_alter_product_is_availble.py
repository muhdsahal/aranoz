# Generated by Django 4.2.1 on 2023-07-22 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_is_availble'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_availble',
            field=models.BooleanField(default=True),
        ),
    ]
