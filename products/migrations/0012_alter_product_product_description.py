# Generated by Django 4.2.1 on 2023-08-08 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_product_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(),
        ),
    ]
