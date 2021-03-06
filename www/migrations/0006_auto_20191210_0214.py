# Generated by Django 2.2.4 on 2019-12-10 01:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0005_auto_20191210_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/images/2019/12/10/'),
        ),
        migrations.AlterField(
            model_name='season',
            name='ending_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 18, 1, 14, 42, 855590, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='week',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 17, 1, 14, 42, 857214, tzinfo=utc)),
        ),
    ]
