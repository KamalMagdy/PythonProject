# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogersite', '0010_auto_20180218_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userslike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.IntegerField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 19, 15, 13, 43, 187311)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 19, 15, 13, 43, 185924)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_comment_id',
            field=models.ForeignKey(blank=True, to='blogersite.Comment', null=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 19, 15, 13, 43, 187945)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_user_id',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userslike',
            name='like_post_id',
            field=models.ForeignKey(to='blogersite.Posts'),
        ),
        migrations.AddField(
            model_name='userslike',
            name='like_user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
