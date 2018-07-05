# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-01 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('published', models.DateField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to='profile_image')),
            ],
        ),
    ]
