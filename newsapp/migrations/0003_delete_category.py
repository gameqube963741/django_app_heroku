# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 09:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_auto_20170621_1700'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
