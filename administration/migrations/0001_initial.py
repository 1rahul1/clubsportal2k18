# Generated by Django 2.1.2 on 2018-11-16 13:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Onpollclub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.CharField(max_length=25)),
                ('club_name', models.CharField(max_length=200)),
                ('club_info', models.TextField(max_length=20000)),
                ('club_logo', models.ImageField(upload_to='media_/club_logo')),
                ('release_date', models.TimeField(default=datetime.datetime(2018, 11, 16, 18, 55, 51, 802536))),
            ],
        ),
    ]
