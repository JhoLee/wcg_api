# Generated by Django 2.2.1 on 2019-05-15 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wcg', '0004_auto_20190515_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordcloud',
            name='wordCloud',
            field=models.FilePathField(path='wordCloud/aaa'),
        ),
    ]
