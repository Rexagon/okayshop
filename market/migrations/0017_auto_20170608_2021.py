# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-08 17:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0016_compositesheettype_price_huge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='item',
            name='object_id',
        ),
    ]
