# Generated by Django 3.0.8 on 2021-02-23 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('querybook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='solution_rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(blank=True)),
                ('solution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='querybook.Solutions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
