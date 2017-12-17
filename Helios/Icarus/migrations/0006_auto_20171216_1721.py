# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-16 23:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Icarus', '0005_auto_20171216_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('acronym', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Institutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('acronym', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('acronym', models.CharField(max_length=5)),
                ('fk_college', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.Colleges')),
            ],
        ),
        migrations.AddField(
            model_name='colleges',
            name='fk_institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icarus.Institutions'),
        ),
    ]