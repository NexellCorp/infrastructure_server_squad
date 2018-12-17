# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-17 01:17
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings


SQL = """
UPDATE core_status
SET has_metrics = (1>0)
FROM core_metric
WHERE core_metric.test_run_id = core_status.test_run_id
AND core_metric.suite_id = core_status.suite_id
"""


SQLITE = 'sqlite3' in settings.DATABASES['default']['ENGINE']


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0081_status_has_metrics'),
    ]

    if SQLITE:
        operations = []
    else:
        operations = [
            migrations.RunSQL(SQL, reverse_sql=migrations.RunSQL.noop),
        ]
