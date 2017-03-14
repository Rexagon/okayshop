# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 19:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_compositetype_application'),
    ]

    operations = [
        migrations.CreateModel(
            name='Texture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='\u0410\u0440\u0442\u0438\u043a\u0443\u043b')),
                ('image', models.ImageField(upload_to=b'', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0442\u0435\u043a\u0441\u0442\u0443\u0440\u0430',
                'verbose_name_plural': '\u0422\u0435\u043a\u0441\u0442\u0443\u0440\u044b',
            },
        ),
        migrations.CreateModel(
            name='TexturesGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0433\u0440\u0443\u043f\u043f\u0430 \u0442\u0435\u043a\u0441\u0442\u0443\u0440',
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u044b \u0442\u0435\u043a\u0441\u0442\u0443\u0440',
            },
        ),
        migrations.AddField(
            model_name='texture',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.TexturesGroup'),
        ),
    ]