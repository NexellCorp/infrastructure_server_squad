# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20160826_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='testrun',
            name='data_processed',
            field=models.BooleanField(default=False),
        ),
    ]
