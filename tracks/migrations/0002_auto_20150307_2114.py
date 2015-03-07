# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapoint',
            name='app_version',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datapoint',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 7, 21, 14, 23, 848545), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datapoint',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 7, 21, 14, 23, 848516), auto_now=True),
            preserve_default=True,
        ),
    ]
