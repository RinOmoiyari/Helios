# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Flows(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    active = models.BooleanField(default=True)
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

    status = models.CharField(max_length=2, choices=REQ_STATES, default="DR")
    summary = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    fk_flow = models.ForeignKey('Flows', on_delete=models.CASCADE,blank=True, null=True)
    fk_course = models.ForeignKey('Courses', on_delete=models.CASCADE,blank=True, null=True)

    fk_project = models.ForeignKey('Projects', on_delete=models.CASCADE,blank=True, null=True)
    PWA = models.CharField(max_length=255, null=True)
    proj_PWA = models.BooleanField(default=True)
    requestor = models.CharField(max_length=255, null=True)
    proj_requestor = models.BooleanField(default=True)


    create_by = models.CharField(max_length=50, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=50, blank=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.summary

class Roles(models.Model):
    name = models.CharField(max_length=50, blank=False)
    acronym = models.CharField(max_length=10, blank=False)

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
    role = models.ForeignKey('Roles',on_delete=models.CASCADE,blank=True, null=True)
    self_assign = models.BooleanField(default=False)
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
    fk_work_req = models.ForeignKey('WorkRequests', on_delete=models.CASCADE, blank=True, null=True)
    fk_flow = models.ForeignKey('Flows', on_delete=models.CASCADE, blank=True, null=True)
    fk_task_template = models.ForeignKey('TaskTemplates', on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUSES, default="P")
    name = models.CharField(max_length=36, blank=False)
    role = models.ForeignKey('Roles',on_delete=models.CASCADE, blank=True, null=True)
    assigned_to = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, blank=False)
    modified_by = models.CharField(max_length=50, blank=True)
    modified_date = models.DateTimeField(auto_now=True)

    def complete(self):
        self.status = 'C'
        self.save()

    def __str__(self):
        return self.name

class Projects(models.Model):
    PROJ_STATES = (
        ("DR", "Draft"),
        ("BA", "Backlog"),
        ("RE", "Requested"),
        ("AP", "Approved"),
        ("DE", "Denied"),
        ("IP", "In Progress"),
        ("CX", "Closed - Canceled"),
        ("CC", "Closed - Complete"),
    )

    status = models.CharField(max_length=2, choices=PROJ_STATES, default="DR")
    summary = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    requestor = models.CharField(max_length=255)
    PWA = models.CharField(max_length=255)
    create_by = models.CharField(max_length=50, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=50, blank=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.summary

class Institutions(models.Model):
    name = models.CharField(max_length=255, blank=False)
    acronym = models.CharField(max_length=10, blank=False)
    contact = models.CharField(max_length=254, blank=True, null=True)
    def __str__(self):
        return self.name

class Colleges(models.Model):
    name = models.CharField(max_length=255, blank=False)
    acronym = models.CharField(max_length=10, blank=False)
    fk_institution = models.ForeignKey('Institutions', on_delete=models.CASCADE, blank=True, null=True)
    contact = models.CharField(max_length=254, blank=True, null=True)
    def __str__(self):
        return self.name

class Schools(models.Model):
    name = models.CharField(max_length=255, blank=False)
    acronym = models.CharField(max_length=10, blank=False)
    fk_college = models.ForeignKey('Colleges', on_delete=models.CASCADE, blank=True, null=True)
    contact = models.CharField(max_length=254, blank=True, null=True)
    def __str__(self):
        return self.name

class Courses(models.Model):
    course_id = models.CharField(max_length=10, blank=False)
    course_pre = models.CharField(max_length=255, blank=True, null=True)
    course_num = models.CharField(max_length=255, blank=True, null=True)
    date_launched = models.DateTimeField(blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    fk_school = models.ForeignKey('Schools', on_delete=models.CASCADE, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.course_id

class CourseVersions(models.Model):
    fk_course = models.ForeignKey('Courses', on_delete=models.CASCADE, blank=True, null=True)
    fk_bkstgroup = models.ForeignKey('BookstoreGroups', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    authsys_vers = models.CharField(max_length=254, blank=True, null=True)
    courseroom_temp = models.CharField(max_length=254, blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

class BookstoreGroups(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
