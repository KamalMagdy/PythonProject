# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogersite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='user_email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_admin',
            new_name='user_is_admin',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_blocked',
            new_name='user_is_blocked',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='user_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='user_password',
        ),
    ]
