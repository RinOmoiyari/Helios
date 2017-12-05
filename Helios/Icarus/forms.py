from django import forms

from . import models

class WR_NewForm(forms.ModelForm):

    class Meta:
        model = models.WorkRequests
        fields = ('summary', 'description',)

class Tasks_NewForm(forms.ModelForm):

    class Meta:
        model = models.Tasks
        fields = ('fk_work_req', 'name', 'status')
