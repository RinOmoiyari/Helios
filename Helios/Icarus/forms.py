from django import forms

from . import models

class WR_NewForm(forms.ModelForm):

    class Meta:
        model = models.WorkRequests
        fields = ('summary', 'description',)
