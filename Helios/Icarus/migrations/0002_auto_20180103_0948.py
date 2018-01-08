# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-03 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Icarus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasktemplates',
            old_name='Trigger',
            new_name='trigger',
        ),
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('W', 'Waiting on Previous Tasks'), ('P', 'Pre-Planning'), ('A', 'Assignable'), ('I', 'In Progress'), ('H', 'Hold'), ('C', 'Completed'), ('X', 'Canceled')], default='P', max_length=1),
        ),
    ]