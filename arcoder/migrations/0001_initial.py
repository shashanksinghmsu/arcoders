# Generated by Django 3.0.8 on 2021-05-30 20:17

import arcoder.models
import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('category', models.CharField(default='', max_length=500)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(default='', upload_to='files/images/languages')),
                ('about', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='user_detail',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('dob', models.CharField(blank=True, max_length=10)),
                ('about', models.CharField(blank=True, default='NO DESCRIPTION ADDED', max_length=300)),
                ('image', models.ImageField(default='user.png', upload_to=arcoder.models.user_image_path)),
                ('otp', models.CharField(default='150302', max_length=6)),
                ('url_otp', models.CharField(blank=True, max_length=10)),
                ('profile_created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('otp_created_at', models.DateTimeField(auto_now=True, null=True)),
                ('privacy', models.BooleanField(default=True)),
            ],
        ),
    ]
