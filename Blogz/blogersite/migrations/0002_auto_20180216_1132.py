# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogersite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 16, 11, 32, 26, 420277)),
        ),
    ]
