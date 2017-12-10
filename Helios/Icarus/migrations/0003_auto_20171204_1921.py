# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 01:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Icarus', '0002_auto_20171204_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='fk_flow',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.Flows'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='fk_task_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.TaskTemplates'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='fk_work_req',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.WorkRequests'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.Roles'),
        ),
    ]