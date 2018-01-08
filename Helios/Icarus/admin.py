from django.contrib import admin
from .models import Flows, WorkRequests, Tasks, TaskTemplates, Roles
from import_export.admin import ImportExportModelAdmin
from Helios import resources

class RoleAdmin(ImportExportModelAdmin):
    resource_class = resources.RoleResource

class TTAdmin(ImportExportModelAdmin):
    resource_class = resources.TTResource


# Register your models here.
admin.site.register(Flows)
admin.site.register(WorkRequests)
admin.site.register(Roles, RoleAdmin)
admin.site.register(TaskTemplates, TTAdmin)
admin.site.register(Tasks)
