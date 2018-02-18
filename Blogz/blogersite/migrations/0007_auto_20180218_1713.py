# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogersite', '0006_auto_20180218_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='post_comment',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 17, 13, 37, 430496)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 17, 13, 37, 428470)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 17, 13, 37, 431339)),
        ),
    ]
