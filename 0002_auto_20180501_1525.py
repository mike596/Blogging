# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-01 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='body_text',
            field=models.TextField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.TextField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='optional_image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
