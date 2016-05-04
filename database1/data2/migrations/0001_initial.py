# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-22 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('fid', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('fname', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'faculty',
                'managed': False,
            },
        ),
    ]