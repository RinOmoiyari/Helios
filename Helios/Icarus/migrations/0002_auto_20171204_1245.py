# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 18:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Icarus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workrequests',
            name='fk_flow',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.Flows'),
        ),
    ]
