# Generated by Django 2.2.3 on 2019-08-06 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0006_auto_20190806_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='studinfo',
            name='rcity',
            field=models.CharField(choices=[('rkt', 'Rajkot'), ('amd', 'Ahemedabad'), ('sur', 'Surat')], default='Rajkot', max_length=50),
        ),
    ]
