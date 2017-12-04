# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Flows(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    active = models.NullBooleanField(default=True)
    create_by = models.CharField(max_length=50, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=50, blank=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class WorkRequests(models.Model):
    REQ_STATES = (
        ("DR", "Draft"),
        ("BA", "Backlog"),
        ("RE", "Requested"),
        ("AP", "Approved"),
        ("DE", "Denied"),
        ("IP", "In Progress"),
        ("CX", "Closed - Canceled"),
        ("CC", "Closed - Complete"),
    )

    summary = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    create_by = models.CharField(max_length=50, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=50, blank=True)
    modified_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=REQ_STATES, default="DR")
    fk_flow = models.ForeignKey('Flows', on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.summary

class Roles(models.Model):
    name = models.CharField(max_length=50, blank=False)
    acronym = models.CharField(max_length=5, blank=False)

    def __str__(self):
        return self.name


class TaskTemplates(models.Model):
    TEMPLATE_STATUSES = (
        ("P", "Pre-Planning"),
        ("A", "Assignable"),
        ("I", "In Progress"),
        ("H", "Hold"),
        ("C", "Completed"),
        ("X", "Canceled"),
    )
    fk_flow = models.ForeignKey('Flows', on_delete=models.CASCADE)
    orderid = models.IntegerField(blank=False)
    Trigger = models.IntegerField(blank=False)
    name = models.CharField(max_length=36, blank=False)
    role = models.ForeignKey('Roles',on_delete=models.CASCADE)
    self_assign = models.NullBooleanField(default=False)
    default_status = models.CharField(max_length=1, choices=TEMPLATE_STATUSES, default="P")

    def __str__(self):
        return self.name

class Tasks(models.Model):
    STATUSES = (
        ("P", "Pre-Planning"),
        ("A", "Assignable"),
        ("I", "In Progress"),
        ("H", "Hold"),
        ("C", "Completed"),
        ("X", "Canceled"),
    )
    fk_work_req = models.ForeignKey('WorkRequests', on_delete=models.CASCADE)
    fk_flow = models.ForeignKey('Flows', on_delete=models.CASCADE)
    fk_task_template = models.ForeignKey('TaskTemplates', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUSES, default="P")
    name = models.CharField(max_length=36, blank=False)
    role = models.ForeignKey('Roles',on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, blank=False)
    modified_by = models.CharField(max_length=50, blank=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
