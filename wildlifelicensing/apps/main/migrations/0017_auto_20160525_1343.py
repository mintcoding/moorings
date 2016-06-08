# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-25 05:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20160517_1735'),
        ('main', '0016_wildlifelicence_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wildlifelicence',
            name='document',
        ),
        migrations.AddField(
            model_name='wildlifelicence',
            name='cover_letter_document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cover_letter_document', to='accounts.Document'),
        ),
        migrations.AddField(
            model_name='wildlifelicence',
            name='cover_letter_message',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='wildlifelicence',
            name='licence_document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='licence_document', to='accounts.Document'),
        ),
    ]