# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('password', models.IntegerField()),
                ('email', models.CharField(max_length=20)),
                ('is_blocked', models.CharField(max_length=20)),
                ('is_admin', models.CharField(max_length=20)),
            ],
        ),
    ]
