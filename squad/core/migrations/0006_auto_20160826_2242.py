# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='metric',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
