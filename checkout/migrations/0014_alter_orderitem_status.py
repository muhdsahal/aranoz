# Generated by Django 4.2.1 on 2023-08-17 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0013_alter_orderitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Return', 'Return'), ('Processing', 'Processing'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('pending', 'pending')], default='pending', max_length=150),
        ),
    ]
