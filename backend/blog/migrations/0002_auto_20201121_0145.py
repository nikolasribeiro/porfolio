# Generated by Django 3.1.3 on 2020-11-21 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porfolio',
            name='img',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]
