# Generated by Django 2.2.1 on 2019-05-15 05:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wcg', '0005_auto_20190508_0716'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordcloudmodel',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
