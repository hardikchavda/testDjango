# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-08-03 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0006_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='m1',
            field=models.IntegerField(default=0, verbose_name='Django'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='m2',
            field=models.IntegerField(default=0, verbose_name='Ionic'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='m3',
            field=models.IntegerField(default=0, verbose_name='Prog. In R'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='per',
            field=models.FloatField(verbose_name='Percentage'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='res',
            field=models.CharField(max_length=20, verbose_name='Result'),
        ),
    ]
