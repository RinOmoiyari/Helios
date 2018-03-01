# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.conf import settings

# Create your models here.
class PFCat(models.Model):
    #Generic Fields
    create_by = models.CharField(max_length=50, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=50, blank=True)
    modified_date = models.DateTimeField(auto_now=True)

    #Data
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField()

    #Status
    selectable = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Flows(models.Model):
    FLOW_DUR = (
        ("PRM", "Permanent"),
        ("TMP", "Temporary"),
    )
    #Generic Fields
    create_by = models.CharField(max_length=50, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=50, blank=True)
    modified_date = models.DateTimeField(auto_now=True)

    #Data
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField()

    #Status
    selectable = models.BooleanField(default=False)
    duration = models.CharField(max_length=3, choices=FLOW_DUR, default="TMP")
    fk_PFCat = models.ForeignKey('PFCat', on_delete=models.SET_NULL, blank=True, null=True)
    instigator = models.CharField(max_length=255, blank=True, null=True) #Project or process that prompted creation of this process flow.

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

    REQ_PRI = (
        ("1", "Urgent"),
        ("2", "High"),
        ("3", "Mid"),
        ("4", "Low"),
    )

    REQ_HEALTH = (
        ("G", "Green"),
        ("Y", "Yellow"),
        ("R", "Red"),
        ("C", "Critical"),
    )

    REQ_BILLING = (
        ("CAP", "Capitalized"),
        ("EXP", "Expense"),
    )
    #Generic Fields
    create_by = models.CharField(max_length=50, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=50, blank=True)
    modified_date = models.DateTimeField(auto_now=True)


    #Request Details
    fk_work_req = models.ForeignKey('WorkRequests', on_delete=models.SET_NULL, blank=True, null=True)
    use_parent_details = models.BooleanField(default=False)
    requestor = models.CharField(max_length=255, null=True)
    department = models.CharField(max_length=255, null=True)
    add_contacts = models.CharField(max_length=255, null=True)
    billing = models.CharField(max_length=3, choices=REQ_PRI)
    pri = models.CharField(max_length=1, choices=REQ_PRI)
    summary = models.CharField(max_length=255, blank=False)
    impacted_loc = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)

    #files field here
    date_start = models.DateTimeField(blank=True, null=True)
    date_due = models.DateTimeField(blank=True, null=True)
    date_launch = models.DateTimeField(blank=True, null=True)

    #Review
    fk_flow = models.ForeignKey('Flows', on_delete=models.SET_NULL,blank=True, null=True)
    status = models.CharField(max_length=2, choices=REQ_STATES, default="DR")
    review_notes = models.TextField(blank=True, null=True)

    #Work
    phase = models.CharField(max_length=255, null=True, default='Draft')
    health = models.CharField(max_length=1, choices=REQ_HEALTH, default="G")
    pwa = models.CharField(max_length=255, null=True)
    fk_courseversion = models.ForeignKey('CourseVersions', on_delete=models.SET_NULL,blank=True, null=True)
    progress_notes = models.TextField(blank=True, null=True)
    date_closed = models.DateTimeField(blank=True, null=True)

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

    #Generic Fields
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, blank=False)
    modified_by = models.CharField(max_length=50, blank=True)
    modified_date = models.DateTimeField(auto_now=True)
    #Order
    fk_flow = models.ForeignKey('Flows', on_delete=models.CASCADE)
    orderid = models.IntegerField(blank=False)
    trigger = models.IntegerField(blank=False)
    #Defaults
    default_status = models.CharField(max_length=1, choices=TEMPLATE_STATUSES, default='P')
    phase = models.CharField(max_length=36, blank=True, null=True)
    name = models.CharField(max_length=36, blank=False)
    role = models.ForeignKey('Roles',on_delete=models.SET_NULL,blank=True, null=True)
    self_assign = models.BooleanField(default=False)
    est_capacity = models.SmallIntegerField(blank=True, null=True)
    #Actions
    resolve_WR = models.BooleanField(default=False) #Should the completion of this task trigger the completion of the related Work Request?


    def __str__(self):
        return self.name

class Tasks(models.Model):
    STATUSES = (
        ("W", "Waiting on Previous Tasks"),
        ("P", "Pre-Planning"),
        ("A", "Assignable"),
        ("I", "In Progress"),
        ("H", "Hold"),
        ("C", "Completed"),
        ("X", "Canceled"),
    )
    #Generic Fields
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, blank=False)
    modified_by = models.CharField(max_length=50, blank=True)
    modified_date = models.DateTimeField(auto_now=True)
    #References
    fk_work_req = models.ForeignKey('WorkRequests', on_delete=models.CASCADE, blank=True, null=True)
    fk_flow = models.ForeignKey('Flows', on_delete=models.SET_NULL, blank=True, null=True)
    fk_task_template = models.ForeignKey('TaskTemplates', on_delete=models.SET_NULL, blank=True, null=True)
    #Tracking
    status = models.CharField(max_length=1, choices=STATUSES, default="P")
    name = models.CharField(max_length=36, blank=False)
    role = models.ForeignKey('Roles',on_delete=models.SET_NULL, blank=True, null=True)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    percent_complete = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    adjusted_time = models.SmallIntegerField(blank=True, null=True)

    def initiate(self):
        self.status = 'I'
        self.save()

    def hold(self):
        if self.status == 'H':
            self.status = 'I'
        else:
            self.status = 'H'
        self.save()

    def selfassign(self, user):
        self.assigned_to = user
        self.save()

    def complete(self):
        self.status = 'C'
        self.save()

    def __str__(self):
        displayname = f"WR {self.fk_work_req_id}: {self.name}"
        return displayname

class Institutions(models.Model):
    #Generic Fields
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, blank=False)
    modified_by = models.CharField(max_length=50, blank=True)
    modified_date = models.DateTimeField(auto_now=True)
    #Data
    name = models.CharField(max_length=255, blank=False)
    acronym = models.CharField(max_length=10, blank=False)
    contact = models.CharField(max_length=254, blank=True, null=True)
    def __str__(self):
        return self.name

class Colleges(models.Model):
    #Generic Fields
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, blank=False)
    modified_by = models.CharField(max_length=50, blank=True)
    modified_date = models.DateTimeField(auto_now=True)
    #Data
    name = models.CharField(max_length=255, blank=False)
    acronym = models.CharField(max_length=10, blank=False)
    fk_institution = models.ForeignKey('Institutions', on_delete=models.SET_NULL, blank=True, null=True)
    contact = models.CharField(max_length=254, blank=True, null=True)
    def __str__(self):
        return self.name

class Schools(models.Model):
    #Generic Fields
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, blank=False)
    modified_by = models.CharField(max_length=50, blank=True)
    modified_date = models.DateTimeField(auto_now=True)
    #Data
    name = models.CharField(max_length=255, blank=False)
    acronym = models.CharField(max_length=10, blank=False)
    ps_code = models.CharField(max_length=5, blank=True, null=True)
    fk_college = models.ForeignKey('Colleges', on_delete=models.SET_NULL, blank=True, null=True)
    contact = models.CharField(max_length=254, blank=True, null=True)
    def __str__(self):
        return self.name

class Courses(models.Model):
    #Generic Fields
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, blank=False)
    modified_by = models.CharField(max_length=50, blank=True)
    modified_date = models.DateTimeField(auto_now=True)
    #Data
    course_id = models.CharField(max_length=10, blank=False)
    course_pre = models.CharField(max_length=255, blank=True, null=True)
    course_num = models.CharField(max_length=255, blank=True, null=True)
    date_launched = models.DateTimeField(blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    fk_school = models.ForeignKey('Schools', on_delete=models.SET_NULL, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.course_id

class CourseVersions(models.Model):
    #Generic Fields
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, blank=False)
    modified_by = models.CharField(max_length=50, blank=True)
    modified_date = models.DateTimeField(auto_now=True)
    #What is it?
    fk_course = models.ForeignKey('Courses', on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    #Where is it in our various systems?
    fk_bkstgroup = models.ForeignKey('BookstoreGroups', on_delete=models.SET_NULL, blank=True, null=True)
    authsys_vers = models.CharField(max_length=254, blank=True, null=True)
    courseroom_temp = models.CharField(max_length=254, blank=True, null=True)
    #Activity timeline
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

class BookstoreGroups(models.Model):
    #Generic Fields
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, blank=False)
    modified_by = models.CharField(max_length=50, blank=True)
    modified_date = models.DateTimeField(auto_now=True)
    #Data
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
