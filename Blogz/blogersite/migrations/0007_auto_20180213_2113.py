# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogersite', '0006_auto_20180213_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_image',
            field=models.ImageField(default=b'images/1.png', upload_to=b'./images/', blank=True),
        ),
    ]
