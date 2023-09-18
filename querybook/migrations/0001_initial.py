# Generated by Django 3.0.8 on 2021-02-14 17:40

import ckeditor.fields
import ckeditor_uploader.fields
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
            name='Query',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('query', models.CharField(max_length=500)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('language', models.CharField(max_length=50)),
                ('slug', models.CharField(blank=True, default='', max_length=300)),
                ('answer', models.IntegerField(default=0)),
                ('time_stamp', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='query_form',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('query', models.CharField(max_length=255)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='solution_form',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('solution', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Solutions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('solution', ckeditor_uploader.fields.RichTextUploadingField()),
                ('time_stamp', models.DateField(auto_now_add=True)),
                ('url', models.URLField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('like', models.ManyToManyField(blank=True, related_name='solution_like', to=settings.AUTH_USER_MODEL)),
                ('query', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='querybook.Query')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
