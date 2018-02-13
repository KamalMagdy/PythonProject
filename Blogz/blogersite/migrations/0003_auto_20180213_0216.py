# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogersite', '0002_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
