# Generated by Django 3.2.7 on 2021-10-19 01:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_order_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_at',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='order',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
