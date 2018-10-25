# Generated by Django 2.1.2 on 2018-10-25 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(blank=True, max_length=100, null=True)),
                ('specialisation', models.CharField(blank=True, max_length=45, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('available_from', models.TimeField(blank=True, null=True)),
                ('available_till', models.TimeField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45, null=True)),
                ('modified_at', models.DateField(blank=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
    ]
