# Generated by Django 2.2.8 on 2020-05-04 14:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0006_auto_20191210_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emission',
            name='cover',
            field=models.ImageField(null=True, upload_to='uploads/images/2020/05/04/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/images/2020/05/04/'),
        ),
        migrations.AlterField(
            model_name='season',
            name='ending_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 13, 14, 4, 9, 155057, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='week',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 11, 14, 4, 9, 157933, tzinfo=utc)),
        ),
    ]
