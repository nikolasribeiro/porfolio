# Generated by Django 3.1.3 on 2020-12-16 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201216_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='porfolio',
            name='category',
        ),
        migrations.AddField(
            model_name='porfolio',
            name='category',
            field=models.ManyToManyField(default='', to='blog.Category'),
        ),
    ]