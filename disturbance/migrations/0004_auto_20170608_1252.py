# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-08 04:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0003_organisationrequestdeclineddetails_organisationrequestuseraction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisationrequestuseraction',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action_logs', to='disturbance.OrganisationRequest'),
        ),
    ]
