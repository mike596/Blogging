# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-01 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0003_auto_20180501_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(max_length=100),
        ),
    ]
