# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 20:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_projectstatus_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectstatus',
            name='build',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='core.Build'),
        ),
    ]
