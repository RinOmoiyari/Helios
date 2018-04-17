from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Max
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from . import forms, models
import tablib
import csv
from import_export import resources

# Create your views here.
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

def WR_newproj(request, ProjID):
    if request.method == "POST":
        form = forms.WR_NewForm(request.POST)
        if form.is_valid():
            WR = form.save(commit=False)
            WR.create_by = 'unknown user'
            WR.save()
            return redirect('Proj_detail', pk=ProjID)
        else:
            form = forms.WR_NewForm(request.POST)
    else:
        data = {'fk_project':ProjID }
        form = forms.WR_NewForm(initial=data)

    return render(request, 'Icarus/WR/WR_new.html', {'form': form})


def WR_edit(request, pk):
    wrequest = get_object_or_404(models.WorkRequests, pk=pk)
    if request.method == "POST":
        form = forms.WR_EditForm(request.POST, instance=wrequest)
        if form.is_valid():
            wrequest = form.save(commit=False)
            wrequest.modified_date = timezone.now()
            wrequest.save()
            return redirect('WR_detail', pk=wrequest.pk)
    else:
        form = forms.WR_EditForm(instance=wrequest)
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
    if get_object_or_404(models.WorkRequests, pk=WRID).fk_flow:
        templates = models.TaskTemplates.objects.filter(fk_flow_id=PFID).order_by('orderid')

        for template in templates:
            task = models.Tasks()
            task.fk_work_req_id = WRID
            task.fk_flow_id = PFID
            task.fk_task_template_id = template.pk
            task.role_id = template.role.id
            task.name = template.name
            if template.trigger == 0:
                task.status = template.default_status
                if template.phase:
                    task.fk_work_req.phase = template.phase
                    task.fk_work_req.save()
            else:
                task.status = 'W'
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
            if request.POST['returnto']:
                return HttpResponseRedirect(request.POST['returnto'])
            else:
                return redirect('Task_detail', pk=task.pk)
    else:
        form = forms.Task_NewForm(instance=task)
    return render(request, 'Icarus/Task/Task_edit.html', {'form': form})

def Task_delete(request, pk):
    task = get_object_or_404(models.Tasks, pk=pk)
    WRID = task.fk_work_req_id
    task.delete()
    return redirect('WR_detail', pk=WRID)

def Task_sa(request, pk):
    user = request.user
    task = get_object_or_404(models.Tasks, pk=pk)
    task.selfassign(user)

    if request.GET['returnto']:
        return HttpResponseRedirect(request.GET['returnto'])
    else:
        return redirect('Task_detail', pk=task.pk)

def Task_hold(request, pk):
    task = get_object_or_404(models.Tasks, pk=pk)
    task.hold()

    if request.GET['returnto']:
        return HttpResponseRedirect(request.GET['returnto'])
    else:
        return redirect('Task_detail', pk=task.pk)


def Task_complete(request, pk):
    task = get_object_or_404(models.Tasks, pk=pk)
    task.complete()

    if task.fk_task_template:
        othertasksinWR = models.Tasks.objects.filter(fk_work_req_id=task.fk_work_req_id)

        for othertask in othertasksinWR:
            if othertask.fk_task_template:
                othertasktrigger = get_object_or_404(models.TaskTemplates, pk=othertask.fk_task_template.pk)
                if othertasktrigger.trigger == task.fk_task_template.orderid and othertask.status == 'W':
                    othertask.status = othertask.fk_task_template.default_status
                    if othertask.fk_task_template.phase:
                        task.fk_work_req.phase = othertask.fk_task_template.phase
                        task.fk_work_req.save()
                    othertask.save()

    return redirect('WR_detail', pk=task.fk_work_req_id)

#===== Process Flow Category Views ========

def PFC_all(request):
    ProcessFlowCats = models.PFCat.objects.all
    return render(request, 'Icarus/PFC/PFC_all.html', {'ProcessFlowCats':ProcessFlowCats})

def PFC_new(request):
    if request.method == "POST":
        form = forms.PFC_NewForm(request.POST)
        if form.is_valid():
            ProcessFlowCat = form.save(commit=False)
            ProcessFlowCat.create_by = 'unknown user'
            ProcessFlowCat.save()
            return redirect('PFC_detail', pk=ProcessFlowCat.pk)
        else:
            form = forms.PFC_NewForm(request.POST)
    else:
        form = forms.PFC_NewForm()

    return render(request, 'Icarus/PFC/PFC_new.html', {'form':form})

def PFC_detail(request, pk):
    ProcessFlowCat = models.PFCat.objects.get(pk=pk)
    ProcessFlows = models.Flows.objects.filter(fk_PFCat=ProcessFlowCat.pk).order_by('-pk')
    return render(request, 'Icarus/PFC/PFC_detail.html', {'ProcessFlowCat':ProcessFlowCat, 'ProcessFlows':ProcessFlows})

def PFC_edit(request, pk):
    processflowcat = get_object_or_404(models.PFCat, pk=pk)
    if request.method == "POST":
        form = forms.PFC_NewForm(request.POST, instance=processflowcat)
        if form.is_valid():
            processflowcat = form.save(commit=False)
            processflowcat.modified_date = timezone.now()
            processflowcat.save()
            return redirect('PFC_detail', pk=processflowcat.pk)
    else:
        form = forms.PFC_NewForm(instance=processflowcat)
    return render(request, 'Icarus/PFC/PFC_edit.html', {'form': form})


#===== Process Flow Views ========
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

def PF_newfromexisting(request, frompk):
    if frompk:
        pass
        return render(request, 'Icarus/PF/PF_new.html')
    else:
        frompf = get_object_or_404(models.Flows, pk=frompk)
        pfcat = frompf.fk_pfcat
        duration = frompf.duration
        return render(request, 'Icarus/PF/PF_new.html', {'pfcat':pfcat, 'duration':duration })

def PF_detail(request, pk):
    ProcessFlow = models.Flows.objects.get(pk=pk)
    tasktemplates = models.TaskTemplates.objects.filter(fk_flow=ProcessFlow.pk).order_by('orderid')
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

        if models.TaskTemplates.objects.filter(fk_flow=PFID).order_by('-orderid').exists():
            pftask = models.TaskTemplates.objects.filter(fk_flow=PFID).order_by('-orderid').first()
            taskorderid = pftask.orderid + 1
        else:
            taskorderid = 1
        data = {'fk_flow':PFID, 'orderid':taskorderid}
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
            if request.POST['returnto']:
                return HttpResponseRedirect(request.POST['returnto'])
            else:
                return redirect('TT_detail', pk=tasktemplate.pk)
    else:
        form = forms.TT_NewForm(instance=tasktemplate)
    return render(request, 'Icarus/TT/TT_edit.html', {'form': form})

def Role_all(request):
    Roles = models.Roles.objects.order_by('name')
    return render(request, 'Icarus/Role/Role_all.html', {'Roles':Roles})

def Role_new(request):
    if request.method == "POST":
        if request.POST['Name'] and request.POST['Acronym']:
            role = models.Roles()
            role.name = request.POST['Name']
            role.acronym = request.POST['Acronym']
            role.save()
            return redirect('Role_all')
        else:
            errormsg = 'Missing required fields.'
            name = request.POST['Name']
            acronym = request.POST['Acronym']
            return render(request, 'Icarus/Role/Role_new.html', {'error':errormsg, 'name':name, 'acronym':acronym})
    else:
        return render(request, 'Icarus/Role/Role_new.html')

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

def Inst_all(request):
    Institutions = models.Institutions.objects.order_by('name')
    return render(request, 'Icarus/Inst/Inst_all.html', {'Institutions':Institutions})

def Inst_new(request):
    if request.method == "POST":
        form = forms.Inst_NewForm(request.POST)
        if form.is_valid():
            Institution = form.save(commit=False)
            Institution.create_by = 'unknown user'
            Institution.save()
            return redirect('Inst_all')
        else:
            form = forms.Inst_NewForm(request.POST)
    else:
        form = forms.Inst_NewForm()

    return render(request, 'Icarus/Inst/Inst_new.html', {'form':form})

def Inst_detail(request, pk):
    Institution = models.Institutions.objects.get(pk=pk)
    Colleges = models.Colleges.objects.filter(fk_institution=Institution.pk)
    return render(request, 'Icarus/Inst/Inst_detail.html', {'Institution':Institution, 'Colleges':Colleges})

def Inst_edit(request, pk):
    Institution = get_object_or_404(models.Institutions, pk=pk)
    if request.method == "POST":
        form = forms.Inst_NewForm(request.POST, instance=Institution)
        if form.is_valid():
            Institution = form.save(commit=False)
            Institution.modified_date = timezone.now()
            Institution.save()
            return redirect('Inst_detail', pk=Institution.pk)
    else:
        form = forms.Inst_NewForm(instance=Institution)
    return render(request, 'Icarus/Inst/Inst_edit.html', {'form': form})


def Col_all(request):
    Colleges = models.Colleges.objects.order_by('name')
    return render(request, 'Icarus/Col/Col_all.html', {'Colleges':Colleges})

def Col_new(request):
    if request.method == "POST":
        form = forms.Col_NewForm(request.POST)
        if form.is_valid():
            College = form.save(commit=False)
            College.create_by = 'unknown user'
            College.save()
            return redirect('Col_all')
        else:
            form = forms.Col_NewForm(request.POST)
    else:
        form = forms.Col_NewForm()

    return render(request, 'Icarus/Col/Col_new.html', {'form':form})

def Col_newfrominst(request, IID):
    if request.method == "POST":
        form = forms.Col_NewForm(request.POST)
        if form.is_valid():
            College = form.save(commit=False)
            College.save()
            return redirect('Inst_detail', pk=IID)
        else:
            form = forms.Col_NewForm(request.POST)
    else:
        data = {'fk_institution': IID}
        form = forms.Col_NewForm(initial=data)

    return render(request, 'Icarus/Col/Col_new.html', {'form': form})

def Col_detail(request, pk):
    College = models.Colleges.objects.get(pk=pk)
    Schools = models.Schools.objects.filter(fk_college=College.pk)
    return render(request, 'Icarus/Col/Col_detail.html', {'College':College, 'Schools':Schools})

def Col_edit(request, pk):
    College = get_object_or_404(models.Colleges, pk=pk)
    if request.method == "POST":
        form = forms.Col_NewForm(request.POST, instance=College)
        if form.is_valid():
            College = form.save(commit=False)
            College.modified_date = timezone.now()
            College.save()
            return redirect('Col_detail', pk=College.pk)
    else:
        form = forms.Col_NewForm(instance=College)
    return render(request, 'Icarus/Col/Col_edit.html', {'form': form})


def Sch_all(request):
    Schools = models.Schools.objects.order_by('name')
    return render(request, 'Icarus/Sch/Sch_all.html', {'Schools':Schools})

def Sch_new(request):
    if request.method == "POST":
        form = forms.Sch_NewForm(request.POST)
        if form.is_valid():
            School = form.save(commit=False)
            School.create_by = 'unknown user'
            School.save()
            return redirect('Sch_all')
        else:
            form = forms.Sch_NewForm(request.POST)
    else:
        form = forms.Sch_NewForm()

    return render(request, 'Icarus/Sch/Sch_new.html', {'form':form})

def Sch_newfromcol(request, CID):
    if request.method == "POST":
        form = forms.Sch_NewForm(request.POST)
        if form.is_valid():
            School = form.save(commit=False)
            School.save()
            return redirect('Col_detail', pk=CID)
        else:
            form = forms.Col_NewForm(request.POST)
    else:
        data = {'fk_college': CID}
        form = forms.Sch_NewForm(initial=data)

    return render(request, 'Icarus/Sch/Sch_new.html', {'form': form})

def Sch_detail(request, pk):
    School = models.Schools.objects.get(pk=pk)
    Courses = models.Courses.objects.filter(fk_school=School.pk)
    return render(request, 'Icarus/Sch/Sch_detail.html', {'School':School, 'Courses':Courses})

def Sch_edit(request, pk):
    School = get_object_or_404(models.Schools, pk=pk)
    if request.method == "POST":
        form = forms.Sch_NewForm(request.POST, instance=School)
        if form.is_valid():
            School = form.save(commit=False)
            School.modified_date = timezone.now()
            School.save()
            return redirect('Sch_detail', pk=School.pk)
    else:
        form = forms.Sch_NewForm(instance=School)
    return render(request, 'Icarus/Sch/Sch_edit.html', {'form': form})


def Crs_all(request):
    Courses = models.Courses.objects.all
    return render(request, 'Icarus/Crs/Crs_all.html', {'Courses':Courses})

def Crs_new(request):
    if request.method == "POST":
        form = forms.Crs_NewForm(request.POST)
        if form.is_valid():
            Course = form.save(commit=False)
            Course.create_by = 'unknown user'
            Course.save()
            return redirect('Crs_all')
        else:
            form = forms.Crs_NewForm(request.POST)
    else:
        form = forms.Crs_NewForm()

    return render(request, 'Icarus/Crs/Crs_new.html', {'form':form})

def Crs_detail(request, pk):
    Course = models.Courses.objects.get(pk=pk)
    CourseVersions = models.CourseVersions.objects.filter(fk_course=Course.pk)
    return render(request, 'Icarus/Crs/Crs_detail.html', {'Course':Course, 'CourseVersions':CourseVersions})

def Crs_edit(request, pk):
    Course = get_object_or_404(models.Courses, pk=pk)
    if request.method == "POST":
        form = forms.Crs_NewForm(request.POST, instance=Course)
        if form.is_valid():
            Course = form.save(commit=False)
            Course.modified_date = timezone.now()
            Course.save()
            return redirect('Crs_detail', pk=Course.pk)
    else:
        form = forms.Crs_NewForm(instance=Course)
    return render(request, 'Icarus/Crs/Crs_edit.html', {'form': form})

def Cvs_all(request):
    CourseVersions = models.CourseVersions.objects.order_by('name')
    return render(request, 'Icarus/Cvs/Cvs_all.html', {'CourseVersions':CourseVersions})

def Cvs_new(request):
    if request.method == "POST":
        form = forms.Cvs_NewForm(request.POST)
        if form.is_valid():
            CourseVersion = form.save(commit=False)
            CourseVersion.create_by = 'unknown user'
            CourseVersion.save()
            return redirect('Cvs_all')
        else:
            form = forms.Cvs_NewForm(request.POST)
    else:
        form = forms.Cvs_NewForm()

    return render(request, 'Icarus/Cvs/Cvs_new.html', {'form':form})

def Cvs_detail(request, pk):
    CourseVersion = models.CourseVersions.objects.get(pk=pk)
    wrequests = models.WorkRequests.objects.filter(fk_course=CourseVersion.pk)
    return render(request, 'Icarus/Cvs/Cvs_detail.html', {'CourseVersion':CourseVersion, 'wrequests':wrequests})

def Cvs_edit(request, pk):
    CourseVersion = get_object_or_404(models.CourseVersions, pk=pk)
    if request.method == "POST":
        form = forms.Cvs_NewForm(request.POST, instance=CourseVersion)
        if form.is_valid():
            CourseVersion = form.save(commit=False)
            CourseVersion.modified_date = timezone.now()
            CourseVersion.save()
            return redirect('Cvs_detail', pk=CourseVersion.pk)
    else:
        form = forms.Cvs_NewForm(instance=CourseVersion)
    return render(request, 'Icarus/Cvs/Cvs_edit.html', {'form': form})

def Bkst_all(request):
    BookstoreGroups = models.BookstoreGroups.objects.order_by('name')
    return render(request, 'Icarus/Bkst/Bkst_all.html', {'BookstoreGroups':BookstoreGroups})

def Bkst_new(request):
    if request.method == "POST":
        form = forms.Bkst_NewForm(request.POST)
        if form.is_valid():
            BookstoreGroup = form.save(commit=False)
            BookstoreGroup.create_by = 'unknown user'
            BookstoreGroup.save()
            return redirect('Bkst_all')
        else:
            form = forms.Bkst_NewForm(request.POST)
    else:
        form = forms.Bkst_NewForm()

    return render(request, 'Icarus/Bkst/Bkst_new.html', {'form':form})

def Bkst_detail(request, pk):
    BookstoreGroup = models.BookstoreGroups.objects.get(pk=pk)
    return render(request, 'Icarus/Bkst/Bkst_detail.html', {'BookstoreGroup':BookstoreGroup})

def Bkst_edit(request, pk):
    BookstoreGroup = get_object_or_404(models.BookstoreGroups, pk=pk)
    if request.method == "POST":
        form = forms.Bkst_NewForm(request.POST, instance=BookstoreGroup)
        if form.is_valid():
            BookstoreGroup = form.save(commit=False)
            BookstoreGroup.modified_date = timezone.now()
            BookstoreGroup.save()
            return redirect('Bkst_detail', pk=BookstoreGroup.pk)
    else:
        form = forms.Bkst_NewForm(instance=BookstoreGroup)
    return render(request, 'Icarus/Bkst/Bkst_edit.html', {'form': form})

def Role_exp(request):
    role_resource = resources.RoleResource()
    dataset = role_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="roles.csv"'
    return response

def Role_imp(request):
    if request.method == 'POST':
        roles_resource = resources.modelresource_factory(model=models.Roles)()
        dataset = tablib.Dataset()
        dataset.csv = request.FILES['myfile'].read()

        result = roles_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            roles_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'Icarus/Role/Role_imp.html')
