# Generated by Django 3.0.6 on 2020-06-15 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transport',
            name='slug',
        ),
    ]
