from django import forms

from . import models

class WR_NewForm(forms.ModelForm):

    class Meta:
        model = models.WorkRequests
        fields = ('summary', 'description','fk_flow')

class Task_NewForm(forms.ModelForm):

    class Meta:
        model = models.Tasks
        fields = ('fk_work_req', 'name', 'status', 'role')

class PF_NewForm(forms.ModelForm):

    class Meta:
        model = models.Flows
        fields = ('name', 'description')

class TT_NewForm(forms.ModelForm):

    class Meta:
        model = models.TaskTemplates
        fields = ('fk_flow','name', 'role', 'orderid', 'Trigger')

class Role_NewForm(forms.ModelForm):

    class Meta:
        model = models.Roles
        fields = ('name', 'acronym')
