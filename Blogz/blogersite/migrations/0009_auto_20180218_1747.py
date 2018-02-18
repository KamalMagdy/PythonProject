# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blogersite', '0008_auto_20180218_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 17, 47, 19, 805384)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_user_id',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 17, 47, 19, 803555)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 17, 47, 19, 806126)),
        ),
    ]
