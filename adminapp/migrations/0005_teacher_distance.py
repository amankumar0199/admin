# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-16 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_auto_20200216_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='distance',
            field=models.CharField(default=-14.1414, max_length=1000),
            preserve_default=False,
        ),
    ]