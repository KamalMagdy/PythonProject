# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogersite', '0003_auto_20180217_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_body', models.TextField()),
                ('comment_date', models.DateTimeField(default=datetime.datetime(2018, 2, 18, 11, 58, 47, 555428))),
            ],
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 11, 58, 47, 554085)),
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
        migrations.AddField(
            model_name='comment',
            name='reply_comment_id',
            field=models.ForeignKey(blank=True, to='blogersite.Comment', null=True),
        ),
    ]
