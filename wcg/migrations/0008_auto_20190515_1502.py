# Generated by Django 2.2.1 on 2019-05-15 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wcg', '0007_auto_20190515_1450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wordcloud',
            old_name='datetime',
            new_name='uploaded_at',
        ),
    ]
