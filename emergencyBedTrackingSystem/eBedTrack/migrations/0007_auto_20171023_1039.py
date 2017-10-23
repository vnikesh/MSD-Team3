# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-23 15:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eBedTrack', '0006_auto_20171022_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='bed',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='nurse',
            name='created_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
