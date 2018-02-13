# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogersite', '0005_auto_20180213_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_image',
            field=models.ImageField(upload_to=b'./static/images/', blank=True),
        ),
    ]
