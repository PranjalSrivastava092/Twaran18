# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-15 21:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='snookers_boys',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='snookers_girls',
        ),
    ]