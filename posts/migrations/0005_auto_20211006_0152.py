# Generated by Django 3.2.7 on 2021-10-06 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20211006_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
