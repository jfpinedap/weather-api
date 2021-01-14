# Generated by Django 3.1.5 on 2021-01-13 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=255)),
                ('temperature', models.CharField(max_length=255)),
                ('wind', models.CharField(max_length=255)),
                ('cloudiness', models.CharField(max_length=255)),
                ('pressure', models.CharField(max_length=255)),
                ('humidity', models.CharField(max_length=255)),
                ('sunrise', models.CharField(max_length=255)),
                ('sunset', models.CharField(max_length=255)),
                ('geo_coordinates', models.CharField(max_length=255)),
                ('requested_time', models.CharField(max_length=255)),
                ('forecast', models.JSONField()),
            ],
            options={
                'managed': False,
            },
        ),
    ]