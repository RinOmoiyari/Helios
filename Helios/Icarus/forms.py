from django import forms

from . import models

class Proj_NewForm(forms.ModelForm):

    class Meta:
        model = models.Projects
        fields = ('summary', 'description', 'status')

class WR_NewForm(forms.ModelForm):

    class Meta:
        model = models.WorkRequests
        fields = ('summary', 'description','fk_flow', 'status', 'fk_project', 'fk_course')

class Task_NewForm(forms.ModelForm):

    class Meta:
        model = models.Tasks
        fields = ('fk_work_req', 'fk_flow','fk_task_template', 'name', 'status', 'role')

class PF_NewForm(forms.ModelForm):

    class Meta:
        model = models.Flows
        fields = ('name', 'description')

class TT_NewForm(forms.ModelForm):

    class Meta:
        model = models.TaskTemplates
        fields = ('fk_flow','orderid','Trigger',  'role', 'name')

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
