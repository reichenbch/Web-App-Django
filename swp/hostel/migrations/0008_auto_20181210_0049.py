# Generated by Django 2.1.2 on 2018-12-09 19:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0007_auto_20181210_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintregister',
            name='comp_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/2018-12-10 00:49:32.456106'),
        ),
        migrations.AlterField(
            model_name='complaintregister',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 19, 19, 32, 456106, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 19, 19, 32, 457106, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hostelleave',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 19, 19, 32, 455106, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='selfhelpgroup',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 19, 19, 32, 458105, tzinfo=utc)),
        ),
    ]
