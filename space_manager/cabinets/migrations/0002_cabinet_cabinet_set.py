# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-11 19:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabinets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabinet',
            name='cabinet_set',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cabinets.CabinetSet'),
        ),
    ]
