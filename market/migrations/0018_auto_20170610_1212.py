# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-10 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0017_auto_20170608_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compositesheettype',
            name='price_huge',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c (\u0440/\u043c2) \u043e\u0442 3000'),
            preserve_default=False,
        ),
    ]
