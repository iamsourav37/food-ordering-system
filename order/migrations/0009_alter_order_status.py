# Generated by Django 3.2.7 on 2021-10-19 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Preparing', 'Preparing your order'), ('Dispatched', 'Your order is dispatched'), ('Delivered', 'Order is delivered successfully')], default='Preparing', max_length=100),
        ),
    ]
