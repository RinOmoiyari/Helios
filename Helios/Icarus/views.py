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
    return render(request, 'Icarus/WR_detail.html', {'wrequest':wrequest})


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
