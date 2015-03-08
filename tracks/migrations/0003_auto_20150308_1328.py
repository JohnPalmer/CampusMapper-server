# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0002_auto_20150307_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllowedIPs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('IP_address', models.GenericIPAddressField()),
                ('name', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='datapoint',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 8, 13, 28, 37, 689755), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datapoint',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 8, 13, 28, 37, 689726), auto_now=True),
            preserve_default=True,
        ),
    ]
