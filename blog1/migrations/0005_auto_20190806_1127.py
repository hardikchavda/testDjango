# Generated by Django 2.2.3 on 2019-08-06 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0004_auto_20190806_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studinfo',
            name='rname',
            field=models.CharField(max_length=150, verbose_name='Student Name'),
        ),
    ]
