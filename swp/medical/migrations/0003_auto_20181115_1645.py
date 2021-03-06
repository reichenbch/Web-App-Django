# Generated by Django 2.1.2 on 2018-11-15 16:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0002_auto_20181115_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='modified_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 16, 45, 10, 432247, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='medicalappointment',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicalappointment',
            name='modified_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicalappointment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 16, 45, 10, 433014, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='medicalleave',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicalleave',
            name='modified_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicalleave',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 16, 45, 10, 431389, tzinfo=utc)),
        ),
    ]
