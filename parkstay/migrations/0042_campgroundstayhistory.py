# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 01:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parkstay', '0041_auto_20170125_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampgroundStayHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('min_days', models.SmallIntegerField(default=1)),
                ('max_days', models.SmallIntegerField(default=28)),
                ('min_dba', models.SmallIntegerField(default=0)),
                ('max_dba', models.SmallIntegerField(default=180)),
                ('details', models.TextField(blank=True, null=True)),
                ('range_start', models.DateField(blank=True, null=True)),
                ('range_end', models.DateField(blank=True, null=True)),
                ('campground', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stay_history', to='parkstay.Campground')),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkstay.MaximumStayReason')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]