# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-29 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0096_build_keep_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildPlaceholder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=100)),
                ('build_deleted_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='build_placeholders', to='core.Project')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='buildplaceholder',
            unique_together=set([('project', 'version')]),
        ),
    ]
