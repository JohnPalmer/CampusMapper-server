# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_UUID', models.CharField(max_length=36)),
                ('user_code', models.CharField(max_length=8)),
                ('type', models.CharField(max_length=3)),
                ('encrypted_message', models.TextField()),
                ('last_modified', models.DateTimeField(default=datetime.datetime(2015, 3, 4, 16, 23, 19, 716087), auto_now=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2015, 3, 4, 16, 23, 19, 716117), auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
