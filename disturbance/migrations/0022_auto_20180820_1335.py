# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-20 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0021_auto_20180820_1120'),
    ]

    operations = [
        # migrations.AlterField(
        #     model_name='amendmentrequest',
        #     name='reason',
        #     field=models.CharField(choices=[(0, 'The information provided was insufficient'), (1, 'There was missing information'), (2, 'Other')], default=0, max_length=30, verbose_name='Reason'),
        # ),
        # migrations.AlterField(
        #     model_name='complianceamendmentrequest',
        #     name='reason',
        #     field=models.CharField(choices=[(0, 'The information provided was insufficient'), (1, 'There was missing information'), (2, 'Other')], default=0, max_length=30, verbose_name='Reason'),
        # ),
        migrations.AlterField(
            model_name='proposal',
            name='lodgement_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]