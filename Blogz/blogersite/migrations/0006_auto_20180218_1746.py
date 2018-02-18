# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogersite', '0005_auto_20180218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userslike',
            name='date',
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 17, 46, 58, 231556)),
        ),
    ]
