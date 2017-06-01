# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-01 01:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('disturbance', '0004_auto_20170601_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposaltype',
            name='site',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
            preserve_default=False,
        ),
    ]
