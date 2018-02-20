# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogersite', '0006_auto_20180218_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_body', models.TextField()),
                ('comment_date', models.DateTimeField(default=datetime.datetime(2018, 2, 20, 21, 0, 36, 648904))),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reply_body', models.TextField()),
                ('reply_date', models.DateTimeField(default=datetime.datetime(2018, 2, 20, 21, 0, 36, 649486))),
                ('reply_comment_id', models.ForeignKey(blank=True, to='blogersite.Comment', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 20, 21, 0, 36, 647022)),
        ),
        migrations.AddField(
            model_name='reply',
            name='reply_post_id',
            field=models.ForeignKey(to='blogersite.Posts'),
        ),
        migrations.AddField(
            model_name='reply',
            name='reply_user_id',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_post_id',
            field=models.ForeignKey(to='blogersite.Posts'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
