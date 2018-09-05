# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-07-03 06:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0011_auto_20180703_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvallogdocument',
            name='log_entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='disturbance.ApprovalLogEntry'),
        ),
    ]