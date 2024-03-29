# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-08 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0012_compositesheetoption_compositesheettype'),
    ]

    operations = [
        migrations.AddField(
            model_name='compositesheettype',
            name='price_high',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c (\u0440/\u043c2) \u043e\u0442 500 \u043c2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compositesheettype',
            name='price_low',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c (\u0440/\u043c2)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compositesheettype',
            name='price_middle',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c (\u0440/\u043c2)\u043e\u0442 100 \u043c2 \u0434\u043e 500 \u043c2'),
            preserve_default=False,
        ),
    ]
