# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cat_name', models.CharField(max_length=200)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ForbiddenWords',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('forbiddenWord', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_title', models.CharField(max_length=200)),
                ('post_content', models.TextField()),
                ('post_image', models.ImageField(default=b'1.png', upload_to=b'./static/', blank=True)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('post_cat', models.ForeignKey(to='blogersite.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='TagNames',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='post_tags',
            field=models.ManyToManyField(to='blogersite.TagNames', blank=True),
        ),
    ]
