# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-14 00:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parkstay', '0006_auto_20161114_0840'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampsiteBookingRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True, help_text='Used to check if the start and end dated were changed')),
                ('min_days', models.SmallIntegerField(default=1)),
                ('max_days', models.SmallIntegerField(default=28)),
                ('min_dba', models.SmallIntegerField(default=0)),
                ('max_dba', models.SmallIntegerField(default=180)),
                ('status', models.SmallIntegerField(choices=[(0, 'Open'), (1, 'Closed due to natural disaster'), (2, 'Closed for maintenance'), (3, 'Other')], default=0)),
                ('details', models.TextField(blank=True, null=True)),
                ('range_start', models.DateField(blank=True, null=True)),
                ('range_end', models.DateField(blank=True, null=True)),
                ('campsite', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='booking_ranges', to='parkstay.Campsite')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
