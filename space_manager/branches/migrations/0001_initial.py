# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-15 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchnum', models.IntegerField()),
                ('region', models.CharField(max_length=140, null=True)),
                ('branch_name', models.CharField(max_length=140, null=True)),
                ('address', models.CharField(max_length=140, null=True)),
                ('detail_address', models.CharField(max_length=140, null=True)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='BranchConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('man_usable', models.BooleanField(default=True)),
                ('woman_usable', models.BooleanField(default=True)),
                ('girl_usable', models.BooleanField(default=True)),
                ('boy_usable', models.BooleanField(default=True)),
                ('other_usable', models.BooleanField(default=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='branches.Branch')),
            ],
        ),
    ]
