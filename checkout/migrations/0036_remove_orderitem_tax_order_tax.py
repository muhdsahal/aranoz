# Generated by Django 4.2.1 on 2023-09-02 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0035_remove_orderitem_coupon_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='tax',
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.IntegerField(null=True),
        ),
    ]
