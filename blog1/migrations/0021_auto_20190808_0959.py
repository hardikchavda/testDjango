# Generated by Django 2.2.3 on 2019-08-08 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0020_auto_20190808_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studinfo',
            name='rphone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Contact Number'),
        ),
    ]