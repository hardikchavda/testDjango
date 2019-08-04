# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-08-03 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0003_auto_20190803_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='stud',
            name='raddress',
            field=models.TextField(blank=True, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='stud',
            name='rujobless',
            field=models.BooleanField(default=True, verbose_name='Jobless'),
        ),
    ]