# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiskies', '0009_auto_20160509_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
