# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogersite', '0003_auto_20180213_0216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_title', models.CharField(max_length=200)),
                ('post_content', models.TextField()),
                ('post_image', models.ImageField(upload_to=b'', blank=True)),
                ('post_date', models.DateTimeField(verbose_name=b'date')),
                ('post_catId', models.ForeignKey(to='blogersite.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='TagNames',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='forbiddenwords',
            name='forbiddenWord',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='posts',
            name='post_tags',
            field=models.ManyToManyField(to='blogersite.TagNames', blank=True),
        ),
    ]
