# Generated by Django 3.0.6 on 2020-06-14 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('img', models.ImageField(upload_to='MediaCar/')),
                ('slug', models.SlugField(blank=True, max_length=100)),
            ],
        ),
    ]
