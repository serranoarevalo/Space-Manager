# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-21 08:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paymenthistory',
            options={'ordering': ['-created_at']},
        ),
    ]
