# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0002_sets'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='class_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scores',
            name='class_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
