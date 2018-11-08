# Generated by Django 2.1.2 on 2018-11-08 05:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.CharField(max_length=1000)),
                ('roll', models.CharField(max_length=11)),
                ('student_first_name', models.CharField(max_length=50)),
                ('student_middle_name', models.CharField(max_length=50)),
                ('student_last_name', models.CharField(max_length=50)),
                ('student_dob', models.DateTimeField()),
                ('student_gender', models.CharField(max_length=5)),
                ('student_email', models.EmailField(max_length=254)),
                ('student_mobile', models.CharField(max_length=14)),
                ('student_blood_group', models.CharField(max_length=3)),
                ('student_mother_tongue', models.CharField(max_length=50)),
                ('student_registered_year', models.DateField(default=datetime.date.today)),
                ('student_registered_degree', models.CharField(max_length=50)),
                ('student_registered_degree_duration', models.CharField(max_length=1)),
                ('student_cur_yearofstudy', models.CharField(max_length=1)),
                ('student_cur_sem', models.CharField(max_length=1)),
                ('student_academic_status', models.CharField(max_length=20)),
                ('bio', models.CharField(blank=True, max_length=100, null=True)),
                ('is_hostel_admin', models.BooleanField(default=False)),
                ('is_mess_admin', models.BooleanField(default=False)),
                ('is_medical_admin', models.BooleanField(default=False)),
                ('avatar', models.ImageField(default='images/default.png', upload_to='images/')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45, null=True)),
                ('modified_at', models.DateField(blank=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=45, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
