# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('acronym', models.CharField(max_length=10)),
                ('contact', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=10)),
                ('course_pre', models.CharField(blank=True, max_length=255, null=True)),
                ('course_num', models.CharField(blank=True, max_length=255, null=True)),
                ('date_launched', models.DateTimeField(blank=True, null=True)),
                ('date_retired', models.DateTimeField(blank=True, null=True)),
                ('contact', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseVersions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('authsys_vers', models.CharField(blank=True, max_length=254, null=True)),
                ('courseroom_temp', models.CharField(blank=True, max_length=254, null=True)),
                ('date_start', models.DateTimeField(blank=True, null=True)),
                ('date_end', models.DateTimeField(blank=True, null=True)),
                ('fk_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='Flows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('create_by', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.CharField(blank=True, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('acronym', models.CharField(max_length=10)),
                ('contact', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('DR', 'Draft'), ('BA', 'Backlog'), ('RE', 'Requested'), ('AP', 'Approved'), ('DE', 'Denied'), ('IP', 'In Progress'), ('CX', 'Closed - Canceled'), ('CC', 'Closed - Complete')], default='DR', max_length=2)),
                ('summary', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('requestor', models.CharField(max_length=255)),
                ('PWA', models.CharField(max_length=255)),
                ('create_by', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.CharField(blank=True, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('acronym', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('acronym', models.CharField(max_length=10)),
                ('contact', models.CharField(blank=True, max_length=254, null=True)),
                ('fk_college', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.Colleges')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'Pre-Planning'), ('A', 'Assignable'), ('I', 'In Progress'), ('H', 'Hold'), ('C', 'Completed'), ('X', 'Canceled')], default='P', max_length=1)),
                ('name', models.CharField(max_length=36)),
                ('assigned_to', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=50)),
                ('modified_by', models.CharField(blank=True, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('fk_flow', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.Flows')),
            ],
        ),
        migrations.CreateModel(
            name='TaskTemplates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.IntegerField()),
                ('Trigger', models.IntegerField()),
                ('name', models.CharField(max_length=36)),
                ('self_assign', models.BooleanField(default=False)),
                ('default_status', models.CharField(choices=[('P', 'Pre-Planning'), ('A', 'Assignable'), ('I', 'In Progress'), ('H', 'Hold'), ('C', 'Completed'), ('X', 'Canceled')], default='P', max_length=1)),
                ('fk_flow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Icarus.Flows')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.Roles')),
            ],
        ),
        migrations.CreateModel(
            name='WorkRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('DR', 'Draft'), ('BA', 'Backlog'), ('RE', 'Requested'), ('AP', 'Approved'), ('DE', 'Denied'), ('IP', 'In Progress'), ('CX', 'Closed - Canceled'), ('CC', 'Closed - Complete')], default='DR', max_length=2)),
                ('summary', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('PWA', models.CharField(max_length=255, null=True)),
                ('proj_PWA', models.BooleanField(default=True)),
                ('requestor', models.CharField(max_length=255, null=True)),
                ('proj_requestor', models.BooleanField(default=True)),
                ('create_by', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.CharField(blank=True, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('fk_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.Courses')),
                ('fk_flow', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.Flows')),
                ('fk_project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.Projects')),
            ],
        ),
        migrations.AddField(
            model_name='tasks',
            name='fk_task_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.TaskTemplates'),
        ),
        migrations.AddField(
            model_name='tasks',
            name='fk_work_req',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.WorkRequests'),
        ),
        migrations.AddField(
            model_name='tasks',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.Roles'),
        ),
        migrations.AddField(
            model_name='courses',
            name='fk_school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.Schools'),
        ),
        migrations.AddField(
            model_name='colleges',
            name='fk_institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.Institutions'),
        ),
    ]
