# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogersite', '0004_auto_20180213_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='post_catId',
            new_name='post_cat',
        ),
    ]
