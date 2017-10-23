# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-13 00:30
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_remove_oracleinterfacesystem_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='oracleinterfacesystem',
            name='percentage',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(1)]),
        ),
    ]