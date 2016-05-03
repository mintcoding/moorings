# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-03 04:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('licence', '0004_auto_20160503_1145'),
        ('accounts', '0014_merge'),
        ('main', '0014_auto_20160428_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='WildlifeLicence',
            fields=[
                ('licence_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='licence.Licence')),
                ('sequence_number', models.IntegerField(default=1)),
                ('purpose', models.TextField(blank=True)),
                ('previous_licence', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.WildlifeLicence')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
            options={
                'abstract': False,
            },
            bases=('licence.licence',),
        ),
        migrations.AddField(
            model_name='assessorgroup',
            name='purpose',
            field=models.BooleanField(default=False),
        ),
    ]
