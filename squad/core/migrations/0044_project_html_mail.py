# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_project_status_build'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='html_mail',
            field=models.BooleanField(default=True),
        ),
    ]
