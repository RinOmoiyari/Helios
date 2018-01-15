# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-15 02:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Icarus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workrequests',
            name='status',
            field=models.CharField(choices=[('DR', 'Draft'), ('BA', 'Backlog'), ('RE', 'Requested'), ('AP', 'Approved'), ('DE', 'Denied'), ('IP', 'In Progress'), ('CX', 'Closed - Canceled'), ('CC', 'Closed - Complete')], default='DR', max_length=2),
        ),
    ]
