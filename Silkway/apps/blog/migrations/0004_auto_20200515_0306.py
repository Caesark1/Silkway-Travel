# Generated by Django 3.0.6 on 2020-05-14 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200515_0303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='url',
            new_name='slug',
        ),
    ]
