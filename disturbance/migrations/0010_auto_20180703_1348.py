# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-07-03 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0009_auto_20180621_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approval',
            name='issue_date',
            field=models.DateTimeField(),
        ),
    ]
