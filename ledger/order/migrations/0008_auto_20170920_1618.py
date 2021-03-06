# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-20 08:18
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20170106_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='deduction_details',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'bpay': {}, 'card': {}, 'cash': {}}),
        ),
        migrations.AddField(
            model_name='line',
            name='payment_details',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'bpay': {}, 'card': {}, 'cash': {}}),
        ),
        migrations.AddField(
            model_name='line',
            name='refund_details',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'bpay': {}, 'card': {}, 'cash': {}}),
        ),
        migrations.AlterField(
            model_name='line',
            name='partner_line_notes',
            field=models.TextField(blank=True, null=True, verbose_name='Partner Notes'),
        ),
        migrations.AlterField(
            model_name='line',
            name='partner_line_reference',
            field=models.CharField(blank=True, help_text='This is the item number that the partner uses within their system', max_length=128, null=True, verbose_name='Partner reference'),
        ),
        migrations.AlterField(
            model_name='line',
            name='partner_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Partner name'),
        ),
        migrations.AlterField(
            model_name='line',
            name='partner_sku',
            field=models.CharField(max_length=128, null=True, verbose_name='Partner SKU'),
        ),
    ]
