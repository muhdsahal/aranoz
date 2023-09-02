# Generated by Django 4.2.1 on 2023-08-12 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0005_category_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='is_active',
        ),
        migrations.AddField(
            model_name='category',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='categories_image',
            field=models.ImageField(default='No Image available', upload_to='categories_images/'),
        ),
    ]
