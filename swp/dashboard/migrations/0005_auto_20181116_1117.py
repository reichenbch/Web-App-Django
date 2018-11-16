# Generated by Django 2.1.2 on 2018-11-16 05:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20181115_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importantcontacts',
            name='delete',
        ),
        migrations.AlterField(
            model_name='hostelannouncements',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 5, 47, 18, 368176, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='medicalannouncements',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 5, 47, 18, 369544, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='messannouncements',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 5, 47, 18, 368836, tzinfo=utc)),
        ),
    ]
