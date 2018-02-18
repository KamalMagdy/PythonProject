# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogersite', '0005_auto_20180218_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 14, 27, 11, 79362)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 14, 27, 11, 78011)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 14, 27, 11, 80020)),
        ),
    ]
