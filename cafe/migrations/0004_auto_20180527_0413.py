# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-26 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0003_auto_20180526_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fcm_token',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='comment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
