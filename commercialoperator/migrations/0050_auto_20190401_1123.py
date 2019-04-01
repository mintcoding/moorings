# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-04-01 03:23
from __future__ import unicode_literals

import commercialoperator.components.compliances.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0049_auto_20190401_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communicationslogentry',
            name='type',
            field=models.CharField(choices=[('email', 'Email'), ('phone', 'Phone Call'), ('mail', 'Mail'), ('person', 'In Person'), ('onhold', 'On Hold'), ('onhold_remove', 'Remove On Hold'), ('with_qaofficer', 'With QA Officer'), ('with_qaofficer_completed', 'QA Officer Completed')], default='email', max_length=35),
        ),
        migrations.AlterField(
            model_name='compliancedocument',
            name='_file',
            field=models.FileField(upload_to=commercialoperator.components.compliances.models.update_proposal_complaince_filename),
        ),
    ]
