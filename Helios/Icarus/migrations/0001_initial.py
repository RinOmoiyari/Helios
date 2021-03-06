# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-14 19:27
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookstoreGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=50)),
                ('modified_by', models.CharField(blank=True, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=50)),
                ('modified_by', models.CharField(blank=True, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('acronym', models.CharField(max_length=10)),
                ('contact', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=50)),
                ('modified_by', models.CharField(blank=True, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
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
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=50)),
                ('modified_by', models.CharField(blank=True, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('authsys_vers', models.CharField(blank=True, max_length=254, null=True)),
                ('courseroom_temp', models.CharField(blank=True, max_length=254, null=True)),
                ('date_start', models.DateTimeField(blank=True, null=True)),
                ('date_end', models.DateTimeField(blank=True, null=True)),
                ('fk_bkstgroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.BookstoreGroups')),
                ('fk_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='Flows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_by', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.CharField(blank=True, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('selectable', models.BooleanField(default=False)),
                ('duration', models.CharField(choices=[('PRM', 'Permanent'), ('TMP', 'Temporary')], default='TMP', max_length=3)),
                ('instigator', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=50)),
                ('modified_by', models.CharField(blank=True, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('acronym', models.CharField(max_length=10)),
                ('contact', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PFCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_by', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.CharField(blank=True, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('selectable', models.BooleanField(default=False)),
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
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=50)),
                ('modified_by', models.CharField(blank=True, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('acronym', models.CharField(max_length=10)),
                ('ps_code', models.CharField(blank=True, max_length=5, null=True)),
                ('contact', models.CharField(blank=True, max_length=254, null=True)),
                ('fk_college', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.Colleges')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=50)),
                ('modified_by', models.CharField(blank=True, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('W', 'Waiting on Previous Tasks'), ('P', 'Pre-Planning'), ('A', 'Assignable'), ('I', 'In Progress'), ('H', 'Hold'), ('C', 'Completed'), ('X', 'Canceled')], default='P', max_length=1)),
                ('name', models.CharField(max_length=36)),
                ('assigned_to', models.CharField(blank=True, max_length=50, null=True)),
                ('percent_complete', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('adjusted_time', models.SmallIntegerField(blank=True, null=True)),
                ('fk_flow', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.Flows')),
            ],
        ),
        migrations.CreateModel(
            name='TaskTemplates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=50)),
                ('modified_by', models.CharField(blank=True, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('orderid', models.IntegerField()),
                ('trigger', models.IntegerField()),
                ('default_status', models.CharField(choices=[('P', 'Pre-Planning'), ('A', 'Assignable'), ('I', 'In Progress'), ('H', 'Hold'), ('C', 'Completed'), ('X', 'Canceled')], default='P', max_length=1)),
                ('phase', models.CharField(blank=True, max_length=36, null=True)),
                ('name', models.CharField(max_length=36)),
                ('self_assign', models.BooleanField(default=False)),
                ('est_capacity', models.SmallIntegerField(blank=True, null=True)),
                ('resolve_WR', models.BooleanField(default=False)),
                ('fk_flow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Icarus.Flows')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.Roles')),
            ],
        ),
        migrations.CreateModel(
            name='WorkRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_by', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.CharField(blank=True, max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('use_parent_details', models.BooleanField(default=False)),
                ('requestor', models.CharField(max_length=255, null=True)),
                ('department', models.CharField(max_length=255, null=True)),
                ('add_contacts', models.CharField(max_length=255, null=True)),
                ('billing', models.CharField(choices=[('1', 'Urgent'), ('2', 'High'), ('3', 'Mid'), ('4', 'Low')], max_length=3)),
                ('pri', models.CharField(choices=[('1', 'Urgent'), ('2', 'High'), ('3', 'Mid'), ('4', 'Low')], max_length=1)),
                ('summary', models.CharField(max_length=255)),
                ('impacted_loc', models.TextField(blank=True, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('date_start', models.DateTimeField(blank=True, null=True)),
                ('date_due', models.DateTimeField(blank=True, null=True)),
                ('date_launch', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('DR', 'Draft'), ('BA', 'Backlog'), ('RE', 'Requested'), ('AP', 'Approved'), ('DE', 'Denied'), ('IP', 'In Progress'), ('CX', 'Closed - Canceled'), ('CC', 'Closed - Complete'), ('CP', 'Closed - Project')], default='DR', max_length=2)),
                ('review_notes', models.TextField(blank=True, null=True)),
                ('phase', models.CharField(default='Draft', max_length=255, null=True)),
                ('health', models.CharField(choices=[('G', 'Green'), ('Y', 'Yellow'), ('R', 'Red'), ('C', 'Critical')], default='G', max_length=1)),
                ('pwa', models.CharField(max_length=255, null=True)),
                ('progress_notes', models.TextField(blank=True, null=True)),
                ('date_closed', models.DateTimeField(blank=True, null=True)),
                ('fk_courseversion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.CourseVersions')),
                ('fk_flow', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.Flows')),
                ('fk_work_req', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.WorkRequests')),
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
            model_name='flows',
            name='fk_PFCat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.PFCat'),
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
