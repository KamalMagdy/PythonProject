# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogersite', '0002_auto_20180213_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_is_admin',
            new_name='is_admin',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_is_blocked',
            new_name='is_blocked',
        ),
    ]
