# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogersite', '0004_auto_20180218_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reply_body', models.TextField()),
                ('reply_date', models.DateTimeField(default=datetime.datetime(2018, 2, 18, 14, 24, 52, 713618))),
                ('reply_comment_id', models.ForeignKey(blank=True, to='blogersite.Reply', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reply_comment_id',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 14, 24, 52, 712926)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 14, 24, 52, 711429)),
        ),
        migrations.AddField(
            model_name='reply',
            name='reply_post_id',
            field=models.ForeignKey(to='blogersite.Posts'),
        ),
        migrations.AddField(
            model_name='reply',
            name='reply_user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
