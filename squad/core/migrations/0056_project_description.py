# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_emailtemplate_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
