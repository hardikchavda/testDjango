# Generated by Django 2.2.3 on 2019-08-06 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0018_auto_20190806_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studinfo',
            name='rphone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Contact Number'),
        ),
    ]
