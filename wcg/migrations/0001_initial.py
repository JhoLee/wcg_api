# Generated by Django 2.2.1 on 2019-05-08 05:01

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WordCloud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('mask_image', models.ImageField(blank=True, upload_to='')),
                ('font', models.CharField(max_length=50)),
                ('data', models.TextField()),
                ('background_color', colorfield.fields.ColorField(default='#000000', max_length=18)),
            ],
        ),
    ]
