# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-23 17:37
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180522_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.get_file_path),
        ),
    ]
