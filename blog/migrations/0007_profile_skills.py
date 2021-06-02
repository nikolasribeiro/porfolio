# Generated by Django 3.1.3 on 2020-12-16 20:19

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201121_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('full_name', models.CharField(default='', max_length=350)),
                ('profile_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('profession', models.CharField(default='', max_length=250)),
                ('living_addres', models.CharField(default='', max_length=250)),
                ('actual_mail', models.CharField(default='', max_length=250)),
                ('github_profile', models.CharField(default='', max_length=250)),
                ('linkedin_profile', models.URLField(default='', max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_skill', models.CharField(default='', max_length=100)),
                ('skill_percent', models.CharField(default='', max_length=3)),
            ],
        ),
    ]