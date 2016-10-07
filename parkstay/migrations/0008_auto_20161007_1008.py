# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-07 02:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parkstay', '0007_auto_20160922_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('abbreviation', models.CharField(max_length=16, null=True, unique=True)),
                ('ratis_id', models.IntegerField(default=-1)),
            ],
        ),
        migrations.AddField(
            model_name='park',
            name='ratis_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='region',
            name='abbreviation',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='region',
            name='ratis_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='parkstay.Region'),
        ),
    ]
