# Generated by Django 4.2.3 on 2023-08-11 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_alter_orderitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('pending', 'pending'), ('Return', 'Return'), ('Cancelled', 'Cancelled'), ('Processing', 'Processing'), ('Shipped', 'Shipped')], default='pending', max_length=150),
        ),
    ]
