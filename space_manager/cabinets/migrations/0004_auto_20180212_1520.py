# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-12 15:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabinets', '0003_auto_20180212_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usecabinet',
            old_name='pay',
            new_name='payment',
        ),
    ]
