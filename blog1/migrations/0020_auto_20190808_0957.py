# Generated by Django 2.2.3 on 2019-08-08 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0019_auto_20190806_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studinfo',
            name='rphone',
            field=models.IntegerField(null=True, verbose_name='Contact Number'),
        ),
    ]
