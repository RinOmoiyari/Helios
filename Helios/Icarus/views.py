from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from . import forms, models

# Create your views here.
def home(request):
    return render(request, 'Icarus/home.html')

def WR_all(request):
    wrequests = models.WorkRequests.objects.all
    return render(request, 'Icarus/WR/WR_all.html', {'wrequests':wrequests})

def WR_detail(request, pk):
    wrequest = models.WorkRequests.objects.get(pk=pk)
    tasks = models.Tasks.objects.filter(fk_work_req=wrequest.pk)
    return render(request, 'Icarus/WR/WR_detail.html', {'wrequest':wrequest, 'tasks':tasks})

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

    return render(request, 'Icarus/WR/WR_new.html', {'form':form})

def WR_edit(request, pk):
    wrequest = get_object_or_404(models.WorkRequests, pk=pk)
    if request.method == "POST":
        form = forms.WR_NewForm(request.POST, instance=wrequest)
        if form.is_valid():
            wrequest = form.save(commit=False)
            wrequest.modified_date = timezone.now()
            wrequest.save()
            return redirect('WR_detail', pk=wrequest.pk)
    else:
        form = forms.WR_NewForm(instance=wrequest)
    return render(request, 'Icarus/WR/WR_edit.html', {'form': form})

def Task_all(request):
    tasks = models.Tasks.objects.all
    return render(request, 'Icarus/Task/Task_all.html', {'tasks':tasks})

def Task_new(request, WRID):
    if request.method == "POST":
        form = forms.Task_NewForm(request.POST)
        if form.is_valid():
            Task = form.save(commit=False)
            Task.create_by = 'unknown user'
            Task.save()
            return redirect('WR_detail', pk=WRID)
        else:
            form = forms.Tasks_NewForm(request.POST)
    else:
        data = {'fk_work_req':WRID }
        form = forms.Task_NewForm(initial=data)

    return render(request, 'Icarus/Task/Task_new.html', {'form': form})

def Task_initialtasks(request, WRID, PFID):
    templates = models.TaskTemplates.objects.filter(fk_flow_id=PFID)

    for template in templates:
        task = models.Tasks()
        task.fk_work_req_id = WRID
        task.fk_flow_id = PFID
        task.fk_task_template_id = template.pk
        task.role_id = template.role.id
        task.name = template.name
        task.save()

    return redirect('WR_detail', pk=WRID)

def Task_detail(request, pk):
    task = models.Tasks.objects.get(pk=pk)
    return render(request, 'Icarus/Task/Task_detail.html', {'task':task})

def Task_edit(request, pk):
    task = get_object_or_404(models.Tasks, pk=pk)
    if request.method == "POST":
        form = forms.Task_NewForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.modified_date = timezone.now()
            task.save()
            return redirect('Task_detail', pk=task.pk)
    else:
        form = forms.Task_NewForm(instance=task)
    return render(request, 'Icarus/Task/Task_edit.html', {'form': form})

def Task_delete(request, pk):
    task = get_object_or_404(models.Tasks, pk=pk)
    task.delete()



    return redirect('Task_all')

def Task_complete(request, pk):
    task = get_object_or_404(models.Tasks, pk=pk)
    task.complete()

    if task.fk_task_template:
        othertasksinWR = models.Tasks.objects.filter(fk_work_req_id=task.fk_work_req_id)

        for othertask in othertasksinWR:
            if othertask.fk_task_template:
                othertasktrigger = get_object_or_404(models.TaskTemplates, pk=othertask.fk_task_template.pk)
                if othertasktrigger.Trigger == task.fk_task_template.orderid and othertask.status == 'P':
                    othertask.status = 'A'
                    othertask.save()

    return redirect('WR_detail', pk=task.fk_work_req_id)

def PF_all(request):
    ProcessFlows = models.Flows.objects.all
    return render(request, 'Icarus/PF/PF_all.html', {'ProcessFlows':ProcessFlows})

def PF_new(request):
    if request.method == "POST":
        form = forms.PF_NewForm(request.POST)
        if form.is_valid():
            ProcessFlow = form.save(commit=False)
            ProcessFlow.create_by = 'unknown user'
            ProcessFlow.save()
            return redirect('PF_detail', pk=ProcessFlow.pk)
        else:
            form = forms.PF_NewForm(request.POST)
    else:
        form = forms.PF_NewForm()

    return render(request, 'Icarus/PF/PF_new.html', {'form':form})

def PF_detail(request, pk):
    ProcessFlow = models.Flows.objects.get(pk=pk)
    tasktemplates = models.TaskTemplates.objects.filter(fk_flow=ProcessFlow.pk)
    return render(request, 'Icarus/PF/PF_detail.html', {'ProcessFlow':ProcessFlow, 'tasktemplates':tasktemplates})

def PF_edit(request, pk):
    processflow = get_object_or_404(models.Flows, pk=pk)
    if request.method == "POST":
        form = forms.PF_NewForm(request.POST, instance=processflow)
        if form.is_valid():
            processflow = form.save(commit=False)
            processflow.modified_date = timezone.now()
            processflow.save()
            return redirect('PF_detail', pk=processflow.pk)
    else:
        form = forms.PF_NewForm(instance=processflow)
    return render(request, 'Icarus/PF/PF_edit.html', {'form': form})

def TT_all(request):
    tasktemplates = models.TaskTemplates.objects.all
    return render(request, 'Icarus/TT/TT_all.html', {'tasktemplates':tasktemplates})

def TT_new(request, PFID):
    if request.method == "POST":
        form = forms.TT_NewForm(request.POST)
        if form.is_valid():
            TaskTemplate = form.save(commit=False)
            TaskTemplate.create_by = 'unknown user'
            TaskTemplate.save()
            return redirect('PF_detail', pk=PFID)
        else:
            form = forms.TT_NewForm(request.POST)
    else:
        data = {'fk_flow':PFID }
        form = forms.TT_NewForm(initial=data)

    return render(request, 'Icarus/TT/TT_new.html', {'form':form})

def TT_detail(request, pk):
    tasktemplate = models.TaskTemplates.objects.get(pk=pk)
    return render(request, 'Icarus/TT/TT_detail.html', {'tasktemplate':tasktemplate})

def TT_edit(request, pk):
    tasktemplate = get_object_or_404(models.TaskTemplates, pk=pk)
    if request.method == "POST":
        form = forms.TT_NewForm(request.POST, instance=tasktemplate)
        if form.is_valid():
            tasktemplate = form.save(commit=False)
            tasktemplate.modified_date = timezone.now()
            tasktemplate.save()
            return redirect('TT_detail', pk=tasktemplate.pk)
    else:
        form = forms.TT_NewForm(instance=tasktemplate)
    return render(request, 'Icarus/TT/TT_edit.html', {'form': form})

def Role_all(request):
    Roles = models.Roles.objects.order_by('name')
    return render(request, 'Icarus/Role/Role_all.html', {'Roles':Roles})

def Role_new(request):
    if request.method == "POST":
        form = forms.Role_NewForm(request.POST)
        if form.is_valid():
            Role = form.save(commit=False)
            Role.create_by = 'unknown user'
            Role.save()
            return redirect('Role_all')
        else:
            form = forms.TT_NewForm(request.POST)
    else:
        form = forms.Role_NewForm()

    return render(request, 'Icarus/Role/Role_new.html', {'form':form})

def Role_detail(request, pk):
    Role = models.Roles.objects.get(pk=pk)
    return render(request, 'Icarus/Role/Role_detail.html', {'Role':Role})

def Role_edit(request, pk):
    role = get_object_or_404(models.Roles, pk=pk)
    if request.method == "POST":
        form = forms.Role_NewForm(request.POST, instance=role)
        if form.is_valid():
            role = form.save(commit=False)
            role.modified_date = timezone.now()
            role.save()
            return redirect('Role_detail', pk=role.pk)
    else:
        form = forms.Role_NewForm(instance=role)
    return render(request, 'Icarus/Role/Role_edit.html', {'form': form})
