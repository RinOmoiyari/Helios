from django.shortcuts import render, redirect
from . import forms, models

# Create your views here.
def home(request):
    return render(request, 'Icarus/home.html')

def WR_all(request):
    wrequests = models.WorkRequests.objects.all
    return render(request, 'Icarus/WR_all.html', {'wrequests':wrequests})

def WR_detail(request, pk):
    wrequest = models.WorkRequests.objects.get(pk=pk)
    tasks = models.Tasks.objects.filter(fk_work_req=wrequest.pk)
    return render(request, 'Icarus/WR_detail.html', {'wrequest':wrequest, 'tasks':tasks})


def WR_new(request):
    if request.method == "POST":
        form = forms.WR_NewForm(request.POST)
        if form.is_valid():
            wrequest = form.save(commit=False)
            wrequest.create_by = 'unknown user'
            wrequest.save()
            return redirect('WR_all')
        else:
            form = forms.WR_NewForm(request.POST)
    else:
        form = forms.WR_NewForm()

    return render(request, 'Icarus/WR_new.html', {'form':form})

def Tasks_all(request):
    tasks = models.Tasks.objects.all
    return render(request, 'Icarus/Tasks_all.html', {'tasks':tasks})

def Tasks_new(request):
    if request.method == "POST":
        form = forms.Tasks_NewForm(request.POST)
        if form.is_valid():
            Task = form.save(commit=False)
            Task.create_by = 'unknown user'
            Task.save()
            return redirect('Tasks_all')
        else:
            form = forms.Tasks_NewForm(request.POST)
    else:
        form = forms.Tasks_NewForm()

    return render(request, 'Icarus/Tasks_new.html', {'form':form})

def Tasks_detail(request, pk):
    task = models.Tasks.objects.get(pk=pk)
    return render(request, 'Icarus/Tasks_detail.html', {'task':task})
