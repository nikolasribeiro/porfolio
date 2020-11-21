# Generated by Django 3.1.3 on 2020-11-21 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Porfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_project', models.CharField(default='', max_length=250)),
                ('github_url', models.URLField(default='')),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]
