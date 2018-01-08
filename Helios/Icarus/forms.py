from django import forms

from . import models


class WR_NewForm(forms.ModelForm):

    class Meta:
        model = models.WorkRequests
        fields = ('status', 'fk_work_req', 'use_parent_details', 'requestor', 'department', 'add_contacts', 'pri', 'summary', 'impacted_loc', 'details', 'date_start', 'date_due', 'date_launch')



class WR_EditForm(forms.ModelForm):

    class Meta:
        model = models.WorkRequests
        fields = ('status', 'fk_work_req', 'use_parent_details', 'requestor', 'department', 'add_contacts', 'pri', 'summary', 'impacted_loc', 'details', 'date_start', 'date_due', 'date_launch', 'fk_flow', 'review_notes', 'phase', 'health', 'pwa', 'fk_courseversion', 'progress_notes', 'date_closed')

class Task_NewForm(forms.ModelForm):

    class Meta:
        model = models.Tasks
        fields = ('fk_work_req', 'fk_flow','fk_task_template', 'name', 'status', 'role', 'assigned_to')

class PF_NewForm(forms.ModelForm):

    class Meta:
        model = models.Flows
        fields = ('name', 'description')

class TT_NewForm(forms.ModelForm):

    class Meta:
        model = models.TaskTemplates
        fields = ('fk_flow','orderid','trigger',  'role', 'name', 'default_status', 'phase','self_assign', 'est_capacity')

class Role_NewForm(forms.ModelForm):

    class Meta:
        model = models.Roles
        fields = ('name', 'acronym')

class Inst_NewForm(forms.ModelForm):

    class Meta:
        model = models.Institutions
        fields = ('acronym', 'name')

class Col_NewForm(forms.ModelForm):

    class Meta:
        model = models.Colleges
        fields = ('fk_institution', 'acronym','name' )

class Sch_NewForm(forms.ModelForm):

    class Meta:
        model = models.Schools
        fields = ('fk_college', 'acronym','name')

class Crs_NewForm(forms.ModelForm):

    class Meta:
        model = models.Courses
        fields = ('fk_school', 'course_id', 'course_pre','course_num')

class Cvs_NewForm(forms.ModelForm):

    class Meta:
        model = models.CourseVersions
        fields = ('fk_course', 'name', 'authsys_vers', 'courseroom_temp')

class Bkst_NewForm(forms.ModelForm):

    class Meta:
        model = models.BookstoreGroups
        fields = ('code', 'name')
