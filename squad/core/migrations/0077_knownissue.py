# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-12 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0076_patch_builds'),
    ]

    operations = [
        migrations.CreateModel(
            name='KnownIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('test_name', models.CharField(max_length=1024)),
                ('url', models.URLField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('intermittent', models.BooleanField(default=False)),
                ('environment', models.ManyToManyField(to='core.Environment')),
            ],
        ),
    ]
