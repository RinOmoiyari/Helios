from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Max
from django.http import HttpResponse, HttpResponseRedirect
from Icarus import models
import tablib
import csv
from import_export import resources

# Create your views here.
def home(request):
    wrcount = models.WorkRequests.objects.count()
    wrdrafts = models.WorkRequests.objects.filter(status='DR').count()
    wrrequested = models.WorkRequests.objects.filter(status='RE').count()
    wrapproved = models.WorkRequests.objects.filter(status='AP').count()
    wrinprog = models.WorkRequests.objects.filter(status='IP').count()
    wrcomplete = models.WorkRequests.objects.filter(status='CC').count()
    return render(request, 'Helios/home.html', {'wrcount':wrcount, 'wrdrafts': wrdrafts, 'wrrequested':wrrequested, 'wrapproved':wrapproved, 'wrinprog':wrinprog, 'wrcomplete':wrcomplete})
