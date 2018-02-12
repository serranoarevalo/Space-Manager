# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-12 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0016_onlyyou'),
        ('cabinets', '0002_cabinet_cabinet_set'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cabinet',
            name='branch',
        ),
        migrations.AddField(
            model_name='usecabinet',
            name='is_clean',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usecabinet',
            name='pay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.PaymentHistory'),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='cabinet_set',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cabinets', to='cabinets.CabinetSet'),
        ),
    ]
