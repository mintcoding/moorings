# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-07-24 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mooring', '0139_auto_20200724_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='VesselDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rego_no', models.CharField(max_length=200)),
                ('vessel_name', models.CharField(max_length=400)),
                ('vessel_size', models.DecimalField(decimal_places=2, default='0.00', max_digits=8)),
                ('vessel_draft', models.DecimalField(decimal_places=2, default='0.00', max_digits=8)),
                ('vessel_beam', models.DecimalField(decimal_places=2, default='0.00', max_digits=8)),
                ('vessel_weight', models.DecimalField(decimal_places=2, default='0.00', max_digits=8)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Vessel Details',
            },
        ),
        migrations.AlterModelOptions(
            name='registeredvessels',
            options={'verbose_name': 'Registered Vessel (Lotus)', 'verbose_name_plural': 'Registered Vessels (Lotus)'},
        ),
    ]