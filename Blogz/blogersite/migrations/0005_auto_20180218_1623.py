# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogersite', '0004_auto_20180218_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='userslike',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 16, 23, 29, 751483)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 16, 23, 29, 750056)),
        ),
    ]
