# Generated by Django 2.2.1 on 2019-05-16 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wcg', '0005_order_ordered_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
