# Generated by Django 3.2.7 on 2021-10-19 01:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
